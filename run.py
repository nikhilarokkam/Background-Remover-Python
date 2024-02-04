import cv2
import numpy as np

def remove_background(image_path, output_path):
    # Read the input image with an alpha channel
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

    # Convert the image to the HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define the lower and upper bounds for the color of the background
    lower_bound = np.array([0, 0, 100])
    upper_bound = np.array([179, 255, 255])

    # Create a mask to extract the background
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Invert the mask to keep the person (non-background) pixels
    inverted_mask = cv2.bitwise_not(mask)

    # Apply the mask to the original image
    result = cv2.bitwise_and(image, image, mask=inverted_mask)

    # Save the result with alpha channel in PNG format
    cv2.imwrite(output_path, result)

if __name__ == "__main__":
    # Replace these paths with your downloaded image and desired output path
    input_image_path = r"C:/Users/Admin/Downloads/nameLogo.png"
    output_image_path = r"C:/Users/Admin/Downloads/image_no_background.png"

    remove_background(input_image_path, output_image_path)
