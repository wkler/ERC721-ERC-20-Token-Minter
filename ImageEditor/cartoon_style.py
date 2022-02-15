import cv2 as cv
from pathlib import Path

# Applies cartoon style to image
def cartoonify_image():
    # Reads image taken from the image path
    with Path("TextFiles/image_path.txt").open("r") as image_path:
        read_image = image_path.read()
        image = cv.imread(read_image, cv.IMREAD_COLOR)
        # Converts image to gray in order to apply adaptive thresholding
        convert_img_to_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        # Blurs image
        convert_img_to_gray = cv.medianBlur(convert_img_to_gray, 5)
        adaptive_threshold = cv.adaptiveThreshold(
            convert_img_to_gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 7, 7
        )
        dst = cv.edgePreservingFilter(image, flags=2, sigma_s=64, sigma_r=0.5)
        complete_style = cv.bitwise_and(dst, dst, mask=adaptive_threshold)

        new_style_filename = "stylized.png"
        cv.imwrite(new_style_filename, complete_style)
