import sys
sys.path.append("ImageEditor")
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg 
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from adaptive_threshold import adaptive_threshold_style
from cartoon_style import cartoonify_image

Ui_MainWindow, baseClass = uic.loadUiType("GuiV2.ui")

class Main(baseClass):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.left_label()
        self.right_label()
        self.browse_button()
        self.stage_button()
        self.delete_button()
        self.show()

    def left_label(self):
        self.background_color_css = "background-color: #D3D3D3;"
        self.border_css = "border: 1.5px dashed #F83212;"
        self.border_css_green = "border: 1.5px solid #7CF3A0;"
        self.font_size = "font-size: 22px;"
        self.font_family = "font-family: Candara;"
        # self.font_weight = "font-weight: bold;"

        self.left_label = self.ui.leftLabel
        self.left_label.setStyleSheet(
            self.background_color_css + self.border_css + self.font_family + 
            self.font_size 
        )
        self.left_label.setAlignment(qtc.Qt.AlignCenter)
        self.left_label.setText("Click the browse \nbutton to load image")
    
    def right_label(self):
        self.right_label = self.ui.rightLabel
        self.right_label.setStyleSheet(
            self.background_color_css + self.border_css + self.font_family + 
            self.font_size
        )
        self.right_label.setAlignment(qtc.Qt.AlignCenter)
        self.right_label.setText("Please stage an image \nin order to mint it")

    def browse_button(self):
        self.browse_btn = self.ui.browseButton
        self.browse_btn.clicked.connect(self.browse_image)

    def browse_image(self):
        #Change starting path location to varible name to something else later on
        path_delete_later = "C:/Users/Forre/Desktop/GuiPhotos/cool.jpg"
        fname = qtw.QFileDialog.getOpenFileName(self, "Open File", path_delete_later, "Image files (*jpg *.png)")
        imagePath = fname[0]
        with open("ImagePathTextFiles/image_path.txt", "w") as f:
            f.write(imagePath)
        print(f"file path is: {imagePath}")
        image = QPixmap(imagePath)
        self.left_label.setPixmap(image)
        self.left_label.setStyleSheet(
            self.background_color_css + self.border_css_green + self.font_family + 
            self.font_size 
        )
        print("Image set!")

    def stage_button(self):
        self.stage_button = self.ui.stageButton
        self.stage_button.clicked.connect(self.checked_checkbox)
        print("Stage button working")

#Applies the image style that the user specifes. The check box determines which
#Opencv style to run.
    def checked_checkbox(self):
        self.adaptive_TH_style_checkbox = self.ui.styleOneCheckBox
        self.cartoon_style_checkbox = self.ui.styleTwoCheckBox

        if self.adaptive_TH_style_checkbox.isChecked():
            adaptive_threshold_style()
            self.pass_image_to_minting_area()
            self.right_label.setStyleSheet(self.border_css_green)

        if self.cartoon_style_checkbox.isChecked():
            cartoonify_image()
            self.pass_image_to_minting_area()
            self.right_label.setStyleSheet(self.border_css_green)

    def pass_image_to_minting_area(self):
        #For now this is just the image but a path can be added later.
        self.styled_image_path = "stylized.jpg"
        self.styled_image = QPixmap(self.styled_image_path)
        self.right_label.setPixmap(self.styled_image)
        #Writes the file path of the edited image to txt folder
        #to be read by script to create URI 
        with open("ImagePathTextFiles/edited_image_result_path.txt", "w") as f:
            f.write(self.styled_image_path)
        print("Image passed to right image container")

        
    def delete_button(self):
        self.delete_button = self.ui.deleteButton
        self.delete_button.clicked.connect(self.remove_image_from_minting_area)
        print("Delete button working")
    
    def remove_image_from_minting_area(self):
        self.right_label.clear()
        self.right_label.setStyleSheet(
            self.background_color_css + self.border_css + self.font_family + 
            self.font_size 
        )
        self.right_label.setText("Please stage an image \nin order to mint it")

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    start = Main()
    sys.exit(app.exec_())