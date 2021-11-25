import cv2 as cv

def adaptive_threshold_style():
    #reads file from text document that specifies path to browsed image
    image_path = "TextFiles/image_path.txt"
    file = open(image_path, "r")
    image_string = file.read()
    image = cv.imread(image_string, cv.IMREAD_COLOR)

    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    adaptive_thresh = cv.adaptiveThreshold(gray_image, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.
    THRESH_BINARY, 15, 7)

    new_style_filename = "stylized.png"
    cv.imwrite(new_style_filename, adaptive_thresh)
