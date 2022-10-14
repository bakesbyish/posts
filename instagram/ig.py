"""Do things with Instagram."""
import shutil
from instabot import Bot
from instabot.bot.bot import os


def upload_ig(username, password):
    """Upload the image to Instagram."""
    # Try and remove the config folder contaning the ig credentials
    try:
        shutil.rmtree("config")
    except FileNotFoundError:
        pass

    # Initialize the bot
    bot = Bot()
    bot.login(username=username, password=password)

    bot.upload_photo(
        f"{os.getcwd()}/img.jpg",
        caption="WhatsApp or call to place your order now. \n Islandwide delivery is available. "
        "\n Cash On Delivery / Bank Deposits accepted. \n #cakedecorating #cakedesign "
        "#cake  #caketools #caketopper #plungercutter #cakeboards #cakeboxes \n DM "
        "@bakes_by_ish \n Reach us on WhatsApp at : https://wa.link/bakesbyish \n visit us "
        "on: www.bakesbyish.com",
    )

    try:
        os.remove(f"{os.getcwd()}/img.jpg" + ".REMOVE_ME")
    except FileNotFoundError:
        pass
