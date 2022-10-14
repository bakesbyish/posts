"""Choose an Image apply the template and upload to Facebook and Instagram."""
import os
import settings
from utils import randomly, convert, imgur
from facebook import template as fb_template, fb
from instagram import template as ig_template, ig
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
    quit()

try:
    file_parts = os.path.basename(str(chosen_image)).split(os.extsep, 2)

    if (len(file_parts) != 3):
        print("The image is not properly formatted")
        quit()

    ext = file_parts[2]
    if ext != "jpg":
        if ext == "png":
            convert.convert_png_to_jpg(
                settings.path_of_images_to_upload,
                f"{file_parts[0]}.{file_parts[1]}"
            )
        elif ext == "jpeg":
            convert.convert_jpeg_to_jpg(
                settings.path_of_images_to_upload,
                f"{file_parts[0]}.{file_parts[1]}"
            )
        elif ext == "webp":
            convert.convert_webp_to_jpg(
                settings.path_of_images_to_upload,
                f"{file_parts[0]}{file_parts[1]}"
            )
        else:
            print("Image format is not supported")
            quit()

        chosen_image = f"{file_parts[0]}.{file_parts[1]}.jpg"

except ValueError:
    whatsapp.renaming_error(chosen_image)
    print(f"The Image {chosen_image} have been renamed incorrectly")
    quit()

# Facebook
# Apply the Facebook template
title, code = fb_template.apply_template(chosen_image)
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
whatsapp.send_uploaded_image_detials(imgur_link, title, code, "Facebook")

# Instagram
# Apply the instagram template
title, code = ig_template.apply_template(chosen_image)
ig.upload_ig(settings.ig_username, settings.ig_password)
# Upload the image to imgur
imgur_link = imgur.upload_image("./img.jpg", title)
# Send alert
whatsapp.send_uploaded_image_detials(imgur_link, title, code, "Instagram")

# Remove the uploaded image
try:
    os.remove("./img.jpg")
except FileNotFoundError:
    pass
