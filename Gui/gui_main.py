import sys

if "metadata_info" not in sys.path:
    sys.path.append("metadata_info")
from metadata_template import nft_metadata
from ImageEditor.adaptive_threshold import adaptive_threshold_style
from ImageEditor.cartoon_style import cartoonify_image
from scripts.pin_metadata_and_mint import upload_to_pinata
from scripts.upload_image_to_ipfs import ipfs_upload
from scripts.mint_tokens import mint_erc20_tokens
from PyQt5 import uic
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5.QtGui import QPixmap


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

    def checked_checkbox(self):
        # Applies style to selected image depening on which checkbox is checked
        if self.ui.styleOneCheckBox.isChecked():
            # Applies filter to image
            adaptive_threshold_style()
            self.pass_image()
        elif self.ui.styleTwoCheckBox.isChecked():
            # Applies filter to image
            cartoonify_image()
            self.pass_image()
        else:
            print("No style has been selected.")

    # Helper function that is run when a photo is staged, regardless of what style is applied.
    def pass_image(self):
        self.pass_image_to_minting_area()
        self.right_label.setStyleSheet(self.border_css_green)

    # Sets the right photo area with the freshly styled image.
    def pass_image_to_minting_area(self):
        if self.current_state == self.STATES[1]:
            # Establishes a path to image (which should be in the root of directory) and connects it with the gui
            self.styled_image_path = "stylized.png"
            self.styled_image = QPixmap(self.styled_image_path)
            self.right_label.setPixmap(self.styled_image)
            # Writes the file path of the edited image to txt file
            # to be read by script to create URI
            with open("TextFiles/edited_image_result_path.txt", "w") as f:
                f.write(self.styled_image_path)
            self.current_state = self.STATES[2]


# Removes the styled image from the gui so that a new
# style can be applied to the image and staged
class ClearImage:
    # Connects the GUI's delete button to it's functionality
    def delete_button(self):
        self.delete_btn = self.ui.deleteButton
        self.delete_btn.clicked.connect(self.remove_image_from_minting_area)

    # Resets the styling and state of the right gui label area
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


# Handles the GUI's MINT button functionality
class MintingFunctionality:
    # Connects the GUI's MINT button to it's functionality
    def mint_button(self):
        self.mint_btn = self.ui.mintButton
        self.mint_btn.clicked.connect(self.mint_functionality)

    def mint_functionality(self):
        if self.current_state == self.STATES[2]:
            # Sets python dictionary to be dumped into json file
            nft_metadata["name"] = self.ui.nameInputBox.text()
            nft_metadata["description"] = self.ui.descriptionInputBox.text()
            # Runs all three scripts, all of which can be found: ERC-721-ERC-20-TOKEN-MINTER-GUI/scripts
            ipfs_upload()
            upload_to_pinata()
            mint_erc20_tokens()


# loadUIType returns a tuple of the builder class, and the
# PyQt5.QtWidgets.QMainWindow class -> also known as the baseClass
Ui_MainWindow, baseClass = uic.loadUiType("GuiV2.ui")

# Set up class that inherifts all other classes.
class Main(
    baseClass,
    BrowseButtons,
    Labels,
    ImageStaging,
    ClearImage,
    MintingFunctionality,
):
    def __init__(self):
        super().__init__()
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


app = qtw.QApplication(sys.argv)
start = Main()
# Exits the execution of the gui
sys.exit(app.exec_())
