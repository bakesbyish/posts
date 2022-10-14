"""Convert diffrent files into diffrent files."""
import PIL.Image as Image
from decouple import os


def convert_png_to_jpg(path, name):
    """Convert a png file to a jpg file."""
    if (str(path).endswith("/")):
        file_path = path
    else:
        file_path = f"{path}/"

    image = Image.open(f"{file_path}{name}.png").convert("RGB")
    image.save(f"{file_path}{name}.jpg")

    # Remove the old png file
    os.remove(f"{file_path}{name}.png")


def convert_jpeg_to_jpg(path, name):
    """Convert a jpeg file to a jpg file."""
    if (str(path).endswith("/")):
        file_path = path
    else:
        file_path = f"{path}/"

    image = Image.open(f"{file_path}{name}.jpeg")
    image.save(f"{file_path}{name}.jpg")

    # Remove the old png file
    os.remove(f"{file_path}{name}.jpeg")


def convert_webp_to_jpg(path, name):
    """Convert a webp file to a jpg file."""
    if (str(path).endswith("/")):
        file_path = path
    else:
        file_path = f"{path}/"

    image = Image.open(f"{file_path}{name}.webp").convert("RGB")
    image.save(f"{file_path}{name}.jpg")

    # Remove the old png file
    os.remove(f"{file_path}{name}.webp")
