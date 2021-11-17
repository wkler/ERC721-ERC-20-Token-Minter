import cv2 as cv

def cartoonify_image():
    image_path = "TextFiles/image_path.txt"
    file = open(image_path, "r")
    image_string = file.read()
    image = cv.imread(image_string, cv.IMREAD_COLOR)

    edges1 = cv.bitwise_not(cv.Canny(image, 100, 200))
    convert_img_to_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    convert_img_to_gray = cv.medianBlur(convert_img_to_gray, 5)

    adaptive_threshold = cv.adaptiveThreshold(
        convert_img_to_gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 7, 7
    )
    dst = cv.edgePreservingFilter(image, flags=2, sigma_s=64, sigma_r=0.25)
    complete_style = cv.bitwise_and(dst, dst, mask=adaptive_threshold)

    new_style_filename = "stylized.jpg"
    cv.imwrite(new_style_filename, complete_style)