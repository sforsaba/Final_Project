

from simpleimage import SimpleImage
from PIL import Image, ImageDraw, ImageFont

DEFAULT_FILE = '../Original_pic.jpg'
INTENSITY_THRESHOLD = 1.6
BLUR_SIZE = 11   # Size of the box filter. Should be positive odd integer
BLUR_ITER = 15
RGB_MAX = 255


def main():
    # Initial Info / Welcome
    print("")
    print("Welcome to the Image Editor")
    print("")


    # Get file and load image
    filename = get_file()
    image = SimpleImage(filename)
    print("")
    #image.show()

    # Asking user for what operation user wants to perform

    user_num = 10
    while user_num != 0:
        print("Edit options available are:")
        print("1.Crop your image")
        print("2.Reflection of an image (Horizontal/Vertical)")
        print("3.Rotate an image (Clockwise/Anticlockwise)")
        print("4.Write text on your image")
        print("5.Apply filters to your image")
        print("")
        print("Would you like to edit an image? (press enter) or exit (type 0)")
        user_num = int(input("Press number 1 to 5 to perform an edit operation:"))




        # Show the image before the transform
        #image.show()

        # Assigning task to the number input by a user
        if user_num == 1:
            trim_crop_size = int(input("How many pixels would you like to trim from each side? "))
            trimmed_img = trim_crop_image(image, trim_crop_size)
            trimmed_img.show()
        if user_num == 2:
            reflection_type = str(input("Press 'H' for Horizontal reflection or 'V' for Vertical reflection:"))
            if reflection_type == 'H':
                h_reflection = horizontal_reflection(image)
                h_reflection.show()
            else:
                v_reflection = vertical_reflection(image)
                v_reflection.show()
        if user_num == 3:
            rotation_type = str(input("Press 'C' for Clockwise rotation or 'A' for Anticlockwise rotation:"))
            if rotation_type == 'C':
                c_rotation = clockwise_rotation(image)
                c_rotation.show()
            else:
                a_rotation = anti_clockwise_rotation(image)
                a_rotation.show()
        if user_num == 4:
            text_image()
            image_text = SimpleImage('../sample2.png')
            image_text.show()
        if user_num == 5:
            filters_image(image)


# This function perform left to right mirror reflection
def horizontal_reflection(without_ref_img_1):
    height = without_ref_img_1.height
    width = without_ref_img_1.width
    reflection = SimpleImage.blank(2 * width, height)
    for y in range(height):
        for x in range(width):
            pixel = without_ref_img_1.get_pixel(x, y)
            reflection.set_pixel(x, y, pixel)
            reflection.set_pixel((2 * width) - (x + 1), y, pixel)
    return reflection


# This function perform top to bottom mirror reflection
def vertical_reflection(without_ref_img_2):
    height = without_ref_img_2.height
    width = without_ref_img_2.width
    reflection = SimpleImage.blank(width, 2 * height)
    for y in range(height):
        for x in range(width):
            pixel = without_ref_img_2.get_pixel(x, y)
            reflection.set_pixel(x, y, pixel)
            reflection.set_pixel(x, (height * 2) - (y + 1), pixel)
    return reflection


def clockwise_rotation(without_ref_img_3):
    height = without_ref_img_3.height
    print(height)
    width = without_ref_img_3.width
    print(width)
    rotation = SimpleImage.blank(width, height)
    #rotation.show()
    for y in range(height):
        for x in range(width):
            pixel = without_ref_img_3.get_pixel(x, y)
            rotation.set_pixel(width - (y + 1), x, pixel)
    return rotation


def anti_clockwise_rotation(without_ref_img_4):
    img_4 = without_ref_img_4
    height = img_4.height
    print(height)
    width = img_4.width
    print(width)
    anti_rotation = SimpleImage.blank(width, height)
    # rotation.show()
    for y in range(height):
        for x in range(width):
            pixel = img_4.get_pixel(x, y)
            anti_rotation.set_pixel(y, height - (x + 1), pixel)
    return anti_rotation




# This function crop an image
def trim_crop_image(original_img, trim_size):
    width = original_img.width
    height = original_img.height
    crop_img = SimpleImage.blank((width - (2 * trim_size)), (height - (2 * trim_size)))
    for y in range(0, height - (2 * trim_size)):
        for x in range(0, width - (2 * trim_size)):
            pixel = original_img.get_pixel(x + trim_size, y + trim_size)
            crop_img.set_pixel(x, y, pixel)
    return crop_img


def text_image():
    text_image_input = Image.open('../Original_pic.jpg')
    quote = str(input("Type your text (max. 22 char): "))
    if len(quote) < 28:
        print("")
        print("Colors available are: red, green, yellow, pink, black, blue, purple")
        text_color = str(input("Type color of your text from the above options: "))
        get_color = get_rgb(text_color)
        print("Jacksilver")
        print("Lovingyou")
        print("Charming")
        print("Sundaybest")
        fnt_typ = str(input("Type font_type from the above options: "))
        print("")
        fnt = adjust_size(fnt_typ)
        #font_size = int(input("Type font size: "))
        #fnt = ImageFont.truetype("../Fonts/" + fnt_typ + ".ttf", 80)
        print("")
        #quote = str(input("Type your text: "))
        d = ImageDraw.Draw(text_image_input)
        d.text((80, 80), quote, font=fnt, fill=get_color)
        text_image_input.save('../sample2.png')
    else:
        print("You entered character more than 22")
        print("Please type your text again")

def adjust_size(font_type):
    if font_type == "Jacksilver":
        fnt = ImageFont.truetype("../Fonts/" + font_type + ".ttf", 80)
    if font_type == "Lovingyou":
        fnt = ImageFont.truetype("../Fonts/" + font_type + ".ttf", 130)
    if font_type == "Charming":
        fnt = ImageFont.truetype("../Fonts/" + font_type + ".ttf", 110)
    if font_type == "Sundaybest":
        fnt = ImageFont.truetype("../Fonts/" + font_type + ".ttf", 40)
    return fnt



def filters_image(filename):
    print("")
    print("Filters available are:")

    print("1.Grey Scale")
    print("2.Sepia filter")
    print("3.Duo-tone filter")
    print("4.Gamma filter")
    print("5.Invert image")
    print("")
    user_filter_num = 10
    while user_filter_num != 0:
        print("Do you like to apply filter to your image?")
        user_filter_num = int(input("Press number 1 to 5 to apply any of the above filters or 0 to exit: "))
        # Show the image after the transform
        if user_filter_num == 1:
            gray = convert_to_gray(filename)
            gray.show()
        if user_filter_num == 2:
            sepia = convert_to_sepia(filename)
            sepia.show()
        if user_filter_num == 3:
            duo_tone = duo_tone_color(filename)
            duo_tone.show()
        if user_filter_num == 4:
            gamma_fil = gamma_filter(filename)
            gamma_fil.show()
        if user_filter_num == 5:
            gray = convert_to_gray(filename)
            inverted = invert_color(gray)
            inverted.show()


def convert_to_sepia(img_5):
    for pixel in img_5:
        R = pixel.red
        G = pixel.green
        B = pixel.blue
        pixel.red = (R * 0.393 + G * 0.769 + B * 0.189)
        pixel.green = (R * 0.349 + G * 0.686 + B * 0.168)
        pixel.blue = (R * 0.272 + G * 0.534 + B * 0.131)
    return img_5


def get_rgb(color):
    if color == "blue":
        return (0,0,255)
    if color == "red":
        return (255,0,0)
    if color == "yellow":
        return (255,255,0)
    if color == "green":
        return (0,255,0)
    if color == "pink":
        return (255,51,153)
    if color == "purple":
        return (102,0,204)
    if color == "black":
        return (0,0,0)





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







def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename
if __name__ == '__main__':
    main()
