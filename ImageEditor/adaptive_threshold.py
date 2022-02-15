import cv2 as cv
from pathlib import Path

# Applies adaptive threshold style to image
def adaptive_threshold_style():
    # Opens file from text document that specifies path to browsed image
    with Path("TextFiles/image_path.txt").open("r") as image_path:
        read_image = image_path.read()
        image = cv.imread(read_image, cv.IMREAD_COLOR)
        # Converts image to grayscale in order to appy adaptive thresholding
        gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        adaptive_thresh = cv.adaptiveThreshold(
            gray_image, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 15, 7
        )
        new_style_filename = "stylized.png"
        # Creates new file in root dir of stylized image
        cv.imwrite(new_style_filename, adaptive_thresh)
