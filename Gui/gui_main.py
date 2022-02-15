import sys
from scripts.pin_metadata_and_mint import upload_to_pinata

sys.path.append("contracts")
sys.path.append("scripts")
sys.path.append("ImageEditor")
sys.path.append("metadata_info")
from upload_image_to_ipfs import ipfs_upload
from metadata_template import nft_metadata
from PyQt5 import uic
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5.QtGui import QPixmap
from adaptive_threshold import adaptive_threshold_style
from cartoon_style import cartoonify_image
from mint_tokens import mint_erc20_tokens
from dotenv import load_dotenv

load_dotenv()


class BrowseButtons:
    # Connects click action to browse image functionality
    def browse_button(self):
        self.browse_btn = self.ui.browseButton
        self.browse_btn.clicked.connect(self.browse_image)

    def browse_image(self):
        # Opens file explorer to the Users directory
        starting_path = "C:/Users"
        fname = qtw.QFileDialog.getOpenFileName(
            self, "Open File", starting_path, "Image files (*jpg *.png)"
        )
        imagePath = fname[0]
        # If user opens the browse dialogue but does not select anything, keep the same css styling.
        # Otherwise, set the pixmap with selected image.
        if imagePath != "":
            with open("TextFiles/image_path.txt", "w") as f:
                f.write(imagePath)
            print(f"file path is: {imagePath}")
            image = QPixmap(imagePath)
            self.left_label.setPixmap(image)
            self.left_label.setStyleSheet(
                self.background_color_css
                + self.border_css_green
                + self.font_family
                + self.font_size
            )
            self.current_state = self.STATES[1]
            print(f"  current state of Gui is {self.current_state}")
            print("  Image set!")
        else:
            print("  No image was selected")


class Labels:
    # Lays the initial styles for the QLabels
    def labels(self):
        if self.current_state == self.STATES[0]:
            # Defining CSS for right and left label
            self.background_color_css = "background-color: #D3D3D3;"
            self.border_css = "border: 1.5px dashed #F83212;"
            self.border_css_green = "border: 1.5px solid #7CF3A0;"
            self.font_size = "font-size: 22px;"
            self.font_family = "font-family: Courier;"
            # Assigning left label it's properties
            self.left_label = self.ui.leftLabel
            self.left_label.setStyleSheet(
                self.background_color_css
                + self.border_css
                + self.font_family
                + self.font_size
            )
            self.left_label.setAlignment(qtc.Qt.AlignCenter)
            self.left_label.setText("Click the browse \nbutton to load image")
            # Assigning the right label it's properties
            self.right_label = self.ui.rightLabel
            self.right_label.setStyleSheet(
                self.background_color_css
                + self.border_css
                + self.font_family
                + self.font_size
            )
            self.right_label.setAlignment(qtc.Qt.AlignCenter)
            self.right_label.setText("Please stage an image \nin order to mint it")


class ImageStaging:
    # Connect state button to checkbox functionality
    def stage_button(self):
        self.stage_btn = self.ui.stageButton
        self.stage_btn.clicked.connect(self.checked_checkbox)

    def test(self):
        self.pass_image_to_minting_area()
        self.right_label.setStyleSheet(self.border_css_green)

    def checked_checkbox(self):
        # Applies style to selected image depening on which checkbox is checked
        if self.ui.styleOneCheckBox.isChecked():
            adaptive_threshold_style()
            self.test()
            # self.pass_image_to_minting_area()
            # self.right_label.setStyleSheet(self.border_css_green)
        elif self.ui.styleTwoCheckBox.isChecked():
            cartoonify_image()
            self.test()
            # self.pass_image_to_minting_area()
            # self.right_label.setStyleSheet(self.border_css_green)
        else:
            print("No style has been selected.")

    # Applies the image style that the user specifes. The check box determines which
    # Opencv style to give the image
    def pass_image_to_minting_area(self):
        if self.current_state == self.STATES[1]:
            # Establishes a path to image (which should be in the root of directory) and inputs it into gui
            self.styled_image_path = "stylized.png"
            self.styled_image = QPixmap(self.styled_image_path)
            self.right_label.setPixmap(self.styled_image)
            # Writes the file path of the edited image to txt file
            # to be read by script to create URI
            with open("TextFiles/edited_image_result_path.txt", "w") as f:
                f.write(self.styled_image_path)
            self.current_state = self.STATES[2]


class ClearImage:
    def delete_button(self):
        self.delete_btn = self.ui.deleteButton
        self.delete_btn.clicked.connect(self.remove_image_from_minting_area)
        print("  Delete button working")

    def remove_image_from_minting_area(self):
        self.right_label.clear()
        self.right_label.setStyleSheet(
            self.background_color_css
            + self.border_css
            + self.font_family
            + self.font_size
        )
        self.right_label.setText("Please stage an image \nin order to mint it")
        self.current_state = self.STATES[1]
        print(f"  State updated to {self.current_state}")


class MintingFunctionality:
    def mint_button(self):
        self.mint_btn = self.ui.mintButton
        self.mint_btn.clicked.connect(self.mint_functionality)

    def mint_functionality(self):
        if self.current_state == self.STATES[2]:
            self.name_input_box = self.ui.nameInputBox
            self.description_input_box = self.ui.descriptionInputBox
            # Updates python dictionary to be dumped into json file
            nft_metadata["name"] = self.name_input_box.text()
            nft_metadata["description"] = self.description_input_box.text()
            ipfs_upload()
            upload_to_pinata()
            mint_erc20_tokens()


# loadUIType returns a tuple of the builder class, and the
# PyQt5.QtWidgets.QMainWindow class -> also known as the baseClass
Ui_MainWindow, baseClass = uic.loadUiType("GuiV2.ui")
print(baseClass)
print(Ui_MainWindow)


class Main(
    baseClass,
    BrowseButtons,
    Labels,
    ImageStaging,
    ClearImage,
    MintingFunctionality,
):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.STATES = ["Home", "Selected", "Staging", "Minting"]
        self.current_state = self.STATES[0]
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.labels()
        self.browse_button()
        self.stage_button()
        self.delete_button()
        self.mint_button()
        self.show()
        print(f"  Current state of Gui is {self.current_state}")


app = qtw.QApplication(sys.argv)
start = Main()
sys.exit(app.exec_())
