"""Get the newly choosen image and apply the template."""

# OS
import os

# Pillow
import PIL.Image as Image
import PIL.ImageFont as ImageFont
import PIL.ImageDraw as ImageDraw
import PIL.ImageEnhance as ImageEnhance

# Define the font used
font = f"{os.getcwd()}/fonts/SirinStencil-Regular.ttf"

# Define the template image file
background_img = f"{os.getcwd()}/facebook/template.png"

# Define the used colors
black = (0, 0, 0)
pink = (255, 183, 195)

# Set the working directory to the current dirrectory
os.environ["PATH"] += os.getcwd()


def apply_template(image_file):
    """Apply the template to the choosen image file."""
    # Define the sizes of the fonts
    font_size_title = 70
    font_size_code = 35

    # Define the needed fonts
    font_title = ImageFont.truetype(font, font_size_title)
    font_code = ImageFont.truetype(font, font_size_code)

    # Product image dimensions
    # and pasting coordinates on the template image
    # (309, 348)          Width:624
    #    ############################################
    #    #                                          #
    #    #                                          #
    #    #                                          #
    #    #                                          # Height: 430
    #    #                                          #
    #    #                                          #
    #    ############################################
    #

    # Define the product image dimensions
    product_image_width = 624
    product_image_height = 430

    # Define the product image coordinates to paste the image on the
    # template background image
    product_image_x_coordinate = 309
    product_image_y_coordinate = 348

    # Product detail box dimensions
    # and pasting coordinates on the template image
    # (105, 199)          Width:721
    #    ############################################
    #    #                                          #
    #    #                                          #
    #    #                                          #
    #    #                                          # Height: 111
    #    #                                          #
    #    #                                          #
    #    ############################################
    #

    # Define the product detail box dimensions
    product_detail_box_width = 721
    product_detail_box_height = 111

    # Product detail box pasting cordinates on
    # the template image
    product_detail_box_x_cordinate = 105
    product_detail_box_y_cordinate = 199

    # Get the details (title, code and extension) from the given image
    title, code, _ = os.path.basename(image_file).split(os.extsep, 2)

    # Open the background image with pillow
    background = Image.open(background_img)
    # Open the product image with pillowe
    product = Image.open(
        f"/home/vinukakodituwakku/Downloads/wallpapers/{image_file}")

    # Resize the product image
    product = product.resize(
        (product_image_width, product_image_height), Image.ANTIALIAS)
    # Paste the product image on the template image
    # on the given coordinates
    background.paste(product, (product_image_x_coordinate,
                     product_image_y_coordinate))

    # Create the product details box with pillow
    product_details_box = Image.new(
        "RGB", (product_detail_box_width, product_detail_box_height), color=pink)
    product_details_box_draw = ImageDraw.Draw(product_details_box)

    # Reformat the obtained details
    image_title = title.replace("_", " ").title()
    image_code = "Code: " + code

    # Get the width and height of the written feilds
    image_title_width, image_title_height = product_details_box_draw.textsize(
        image_title, font=font_title)
    image_code_width, image_code_height = product_details_box_draw.textsize(
        image_code, font=font_code)

    # Get x and y coordinates of the title text starting postion
    image_title_x_coordinate = (
        product_detail_box_width - image_title_width) / 2
    image_title_y_cordinate = (
        product_detail_box_height - (image_title_height+60)) / 2

    # Get the x and y coordinates of the code text starting postion
    image_code_x_coordinate = (product_detail_box_width - image_code_width) / 2
    image_code_y_coordinate = (
        product_detail_box_height - (image_code_height - 60)) / 2

    # Write the contect of the image title to the details box (drawn)
    product_details_box_draw.text(
        (image_title_x_coordinate, image_title_y_cordinate), image_title, font=font_title, fill=black)
    # Write the content of the image code to the details box (drawn)
    product_details_box_draw.text(
        (image_code_x_coordinate, image_code_y_coordinate), image_code, font=font_code, fill=black)

    # Paste the backround image to the template image where the product
    # image is pasted
    background.paste(product_details_box,
                     (product_detail_box_x_cordinate, product_detail_box_y_cordinate))

    # Enhance the image and save it
    ImageEnhance.Color(background).enhance(1.5).convert(
        "RGB").save(os.getcwd() + "/img.jpg")

    # Update the uploaded.txt file with the uploaded image
    uploaded_txt = open(
        f"{os.getcwd()}/uploaded.txt", "a")
    uploaded_txt.write(f"{image_file}\n")
    uploaded_txt.close()

    return title, code
