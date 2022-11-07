"""Load custom config from the .env file."""
from decouple import config

path_of_images_to_upload = config("PRODUCT_PATH", default="")
fb_token = config("FB_TOKEN", default="")
fb_page_id = config("PAGE_ID", default="")
dicord_token = config("DISCORD_TOKEN", default="")
imgur_token = config("IMGUR_TOKEN", default="")
ig_username = config("IG_USERNAME", default="")
ig_password = config("IG_PASSWORD", default="")
whatsapp_accsess_token = config("WHATSAPP_ACCSESS_TOKEN", default="")
whatsapp_phonenumber_id = config("WHATSAPP_PHONENUMBER_ID", default="")
whatsapp_recepient_phone_number = config(
    "WHATSAPP_RECEIPENT_PHONE_NUMBER", default="")
redis_password = config("REDIS_PASSWORD", default="")
