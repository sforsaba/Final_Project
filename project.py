

from simpleimage import SimpleImage
from PIL import Image, ImageDraw

DEFAULT_FILE = '../scene1.jpg'
INTENSITY_THRESHOLD = 1.6
BLUR_SIZE = 11   # Size of the box filter. Should be positive odd integer
BLUR_ITER = 15
RGB_MAX = 255


def main():
    # Initial Info / Welcome
    print("Welcome to the Image Editor")
    print("Edit options available are:")
    print("1.Crop your image")
    print("2.Reflection of an image")
    print("3.Rotate an image")
    print("4.Transpose an image")
    print("5.Increase or Decrease brightness of an image")
    print("6.Change Contrast of an Image")
    print("7.Apply filters to your image")

    # Get file and load image
    filename = get_file()
    image = SimpleImage(filename)
    image.show()

    # Asking user for what operation user wants to perform
    print("Would you like to edit an image? (press enter)")
    user_num = int(input("Press number 1 to 7 to perform an edit operation: "))



    # Show the image before the transform
    #image.show()

    # Assigning task to the number input by a user
    if user_num == 1:
        crop_image()
    if user_num == 2:
        reflection_image()
    if user_num == 3:
        rotate_image()
    if user_num == 4:
        transpose_image()
    if user_num == 5:
        brightness_image()
    if user_num == 6:
        contrast_image()
    if user_num == 7:
        filters_image(image)


def filters_image(filename):
    print("Filters available are:")
    print("1.Grey Scale")
    print("2.Invert image")
    print("3.Duo-tone filter")
    print("4.Gamma filter")
    print("5.Write text on your Image")
    print("Do you like to apply filter to your image?")
    user_filter_num = int(input("Press number 1 to 5 to perform an edit operation: "))
    # Show the image after the transform
    if user_filter_num == 1:
        gray = convert_to_gray(filename)
        gray.show()
    if user_filter_num == 2:
        gray = convert_to_gray(filename)
        inverted = invert_color(gray)
        inverted.show()
    if user_filter_num == 3:
        duo_tone = duo_tone_color(filename)
        duo_tone.show()
    if user_filter_num == 4:
        gamma_fil = gamma_filter(filename)
        gamma_fil.show()
    if user_filter_num == 5:
        text_image()
        image_text = SimpleImage('../sample1.jpg')
        image_text.show()



def text_image():
    text_image_input = Image.open('../scene1.jpg')
    d = ImageDraw.Draw(text_image_input)
    d.text((10, 10), "Hello World", fill=(255, 255, 0))
    text_image_input.save('../sample1.jpg')



def duo_tone_color(image):
    for pixel in image:
        R = pixel.red
        G = pixel.green
        B = pixel.blue
        pixel.red = R * 0.95
        pixel.green = G * 0.75
        pixel.blue = B * 0.25
    return image


def gamma_filter(image):
    for pixel in image:
        R = pixel.red
        G = pixel.green
        B = pixel.blue
        pixel.red = R ** 0.6
        pixel.green = G
        pixel.blue = B
    return image


# function to convert the image to gray scale


def convert_to_gray(image1):
    for pixel in image1:
        average = ((pixel.red + pixel.green + pixel.blue)/3)
        pixel.red = average
        pixel.green = average
        pixel.blue = average
    return image1


# For inverting the color of grayscale image
def invert_color(gray_image):
    """
    Returns a new SimplgeImage object, which is an inverted image
    of grayscale version of SimpleImage img.
    """
    for pixel in gray_image:
        old_red_value = pixel.red
        old_green_value = pixel.green
        old_blue_value = pixel.blue
        pixel.red = RGB_MAX - old_red_value
        pixel.green = RGB_MAX - old_green_value
        pixel.blue = RGB_MAX - old_blue_value
    return gray_image





def blur(image, num_iter, blur_size):
    """
    Returns a new SimplgeImage object, which is a blurred version
    of SimpleImage img. Uses box filters: box size is blur_size
    and the filtering is performed num_iter times. The implementation
    is not the most efficient, so long computing time may be expected
    for large image dimension, larger num_iter, or large blur_size.
    blur_size is a positive odd integer.
    num_iter is a positive integer.
    """
    ref = image
    for i in range(num_iter):
        blurred = copy_image(ref)
        for x in range(ref.width):
            for y in range(ref.height):
                blur_pixel(x, y, blurred, ref, blur_size)
        ref = blurred
    return blurred

def blur_pixel(x, y, blurred, ref, blur_size):
    """
    Update the RGB values of a pixel in SimpleImage 'blurred' at
    coordinates (x, y). The RGB value is the box average of pixels
    in SimpleImage 'ref'. The box is a square centered at (x, y)
    with side length blur_size.
    Note that 'blurred' is modified while 'ref' remains unchanged.
    These two images must have the same dimension.
    Parameters x, y are nonnegative integers within the boundary of
    the image. blur_size is a positive odd integer.
    """
    red = 0
    blue = 0
    green = 0
    count = 0
    r = (blur_size - 1) // 2
    for i in range(x - r, x + r + 1):
        for j in range(y - r, y + r + 1):
            if in_bound(i, j, ref.width, ref.height):
                count += 1
                px = ref.get_pixel(i, j)
                red += px.red
                blue += px.blue
                green += px.green
    pixel = blurred.get_pixel(x, y)
    pixel.red = red / count
    pixel.green = green / count
    pixel.blue = blue / count

def in_bound(x, y, width, height):
    """
    Returns True if the given pixel coordinates (x, y)
    is located inside the image with dimension (width, height).
    Returns False otherwise.
    All parameters are integers
    """
    if 0 <= x < width and 0 <= y < height:
        return True
    return False
def copy_image(img):
    """
    Returns a new SimpleImage object, which has the same
    pixel values as img, which is also a SimpleImage object
    """
    copy = SimpleImage.blank(img.width, img.height)
    for pixel in copy:
        x = pixel.x
        y = pixel.y
        copy.set_pixel(x, y, img.get_pixel(x, y))
    return copy







def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename
if __name__ == '__main__':
    main()
