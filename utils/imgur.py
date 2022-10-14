"""Do functions with Imgur."""
import pyimgur


def upload_image(image, title):
    """Upload the given image to imgur."""
    im = pyimgur.Imgur("96e7cff33a99bd0")
    uploaded_image = im.upload_image(image, title=title)

    return uploaded_image.link
