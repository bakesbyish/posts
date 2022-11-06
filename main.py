"""Choose an Image apply the template and upload to Facebook and Instagram."""
import os
import settings
from utils import randomly, convert, imgur
from facebook import template as fb_template, fb
# from instagram import template as ig_template, ig
from messaging import whatsapp

# Choose an image randomly
chosen_image = randomly.choose_a_file(
    settings.path_of_images_to_upload, "./uploaded.txt")
if chosen_image == "":

    if os.path.isfile(".uploaded"):
        whatsapp.reminder_to_upload_more_photos()
    else:
        open(".uploaded").close()

    print("All the images have been uploaded")
    whatsapp.all_images_uploaded()
    quit()

try:
    file_parts = os.path.basename(str(chosen_image)).split(os.extsep, 3)

    if (len(file_parts) != 4):
        print("The image is not properly formatted")
        whatsapp.error(str(chosen_image))
        quit()

    title, sku, price, ext = file_parts
    if len(title) > 23:
        print("Image title is too long")
        whatsapp.error(str(chosen_image))
        quit()
    elif not str(sku).isnumeric():
        print("SKU is not numeric")
        whatsapp.error(str(chosen_image))
        quit()
    elif not str(sku).isnumeric():
        print("Price is not numeric")
        whatsapp.error(str(chosen_image))
        quit()

    if ext != "jpg":
        if ext == "png":
            convert.convert_png_to_jpg(
                settings.path_of_images_to_upload,
                f"{title}.{sku}.{price}"
            )
        elif ext == "jpeg":
            convert.convert_jpeg_to_jpg(
                settings.path_of_images_to_upload,
                f"{title}.{sku}.{price}"
            )
        elif ext == "webp":
            convert.convert_webp_to_jpg(
                settings.path_of_images_to_upload,
                f"{title}{sku}.{price}"
            )
        else:
            print("Image format is not supported")
            whatsapp.error(str(chosen_image))
            quit()

        chosen_image = f"{title}.{sku}.{price}.jpg"
except ValueError:
    whatsapp.error(str(chosen_image))
    print(f"The Image {chosen_image} have been renamed incorrectly")
    quit()

title, sku, price, _ = os.path.basename(str(chosen_image)).split(os.extsep, 3)
title = title.replace("_", " ").replace(
    "-", " ").replace("$", " ").replace("#", " ").replace("%", " ")

# Facebook
# Apply the Facebook template
fb_template.apply_template(
    title, sku, price, f"{settings.path_of_images_to_upload}/{chosen_image}")
# Upload the Facebook template added image to imgur
imgur_link = imgur.upload_image("./img.jpg", title)

# Remove the uploaded image
try:
    os.remove("./img.jpg")
except FileNotFoundError:
    pass

# Upload the image to the Facebook page
fb.upload_fb(imgur_link, settings.fb_token, settings.fb_page_id)
# Send an Alert
whatsapp.send_uploaded_image_detials(imgur_link, title, sku, price)

# # Instagram
# # Apply the instagram template
# title, code = ig_template.apply_template(chosen_image)
# ig.upload_ig(settings.ig_username, settings.ig_password)
# # Upload the image to imgur
# imgur_link = imgur.upload_image("./img.jpg", title)
# # Send alert
# whatsapp.send_uploaded_image_detials(imgur_link, title, code, "Instagram")

# Update the uploaded.txt file
uploaded_txt = open(
    f"{os.getcwd()}/uploaded.txt", "a")
title = title.replace(" ", "_")
uploaded_txt.write(f"{title}.{sku}.{price}.jpg\n")
uploaded_txt.close()

# Remove the uploaded image
try:
    os.remove("./img.jpg")
except FileNotFoundError:
    pass
