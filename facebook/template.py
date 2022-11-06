"""Get the newly choosen image and apply the template."""

# OS
import os

# Pillow
import PIL.Image as Image
import PIL.ImageFont as ImageFont
import PIL.ImageDraw as ImageDraw
import PIL.ImageEnhance as ImageEnhance

# Define the font used
title_font = f"{os.getcwd()}/fonts/BerkshireSwash-Regular.ttf"
price_font = f"{os.getcwd()}/fonts/OleoScript-Regular.ttf"
sku_font = f"{os.getcwd()}/fonts/OleoScript-Regular.ttf"

# Define the template image file
template_img = f"{os.getcwd()}/facebook/template.png"

# Define the used colors
black = (0, 0, 0)
pink = (255, 183, 195)

# Set the working directory to the current dirrectory
os.environ["PATH"] += os.getcwd()


def apply_template(title, sku, price, path):
    """Apply the template to the choosen image file."""
    # Define the sizes of the fonts
    font_size_title = 90
    font_size_sku = 45
    font_size_price = 65

    # Define the needed fonts
    pil_title_font = ImageFont.truetype(title_font, font_size_title)
    pil_sku_font = ImageFont.truetype(sku_font, font_size_sku)
    pil_price_font = ImageFont.truetype(price_font, font_size_price)

    # Product image dimensions
    # and pasting coordinates on the template image
    # (63, 165)          Width:478
    #    ############################################
    #    #                                          #
    #    #                                          #
    #    #                                          #
    #    #                                          # Height: 449
    #    #                                          #
    #    #                                          #
    #    ############################################
    #

    # Define the product image dimensions
    product_image_width = 478
    product_image_height = 449

    # Define the product image coordinates to paste the image on the
    # template background image
    product_image_x_coordinate = 63
    product_image_y_coordinate = 165

    # Product title text paste coordinates
    # ((image_width/2)-(product_title_length/2), 18)
    #    ############################################
    #    #                                          #
    #    #                                          #
    #    #                                          #
    #    #                                          #
    #    #                                          #
    #    #                                          #
    #    ############################################
    #

    # Product sku text paste cordinates
    # (619, 283)
    #    ############################################
    #    #                                          #
    #    #                                          #
    #    #                                          #
    #    #                                          #
    #    #                                          #
    #    #                                          #
    #    ############################################
    #

    # Product price text paste cordinates
    # (619, 345)
    #    ############################################
    #    #                                          #
    #    #                                          #
    #    #                                          #
    #    #                                          #
    #    #                                          #
    #    #                                          #
    #    ############################################
    #

    # Open the template image
    template = Image.open(template_img).convert("RGB")

    # Get the width of the image
    template_width, _ = template.size

    # Resize and paste the product image on the
    # template
    product = Image.open(path).convert(
        "RGB").resize((product_image_width, product_image_height))
    template.paste(product, (product_image_x_coordinate,
                   product_image_y_coordinate))

    # Convert the template to a canvas by drawing it
    draw = ImageDraw.Draw(template)

    # Write the product title
    title_length = pil_title_font.getlength(title)
    title_x_cordinate = (template_width / 2) - (title_length / 2)
    title_y_cordinate = 18
    draw.text((title_x_cordinate, title_y_cordinate),
              title, black, font=pil_title_font)

    # Write the product SKU
    sku_x_cordinate = 619
    sku_y_cordinate = 283
    draw.text((sku_x_cordinate, sku_y_cordinate),
              f"SKU {sku}", black, font=pil_sku_font)

    # Write the product price
    price_x_cordinate = 619
    price_y_cordinate = 345
    draw.text((price_x_cordinate, price_y_cordinate),
              f"Rs. {price}/", black, font=pil_price_font)

    # Save the image
    ImageEnhance.Color(template).enhance(1.5).convert(
        "RGB").save(f"{os.getcwd()}/img.jpg")
