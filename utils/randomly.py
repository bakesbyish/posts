"""All the stuff that are done randomly."""

import random
import os


def choose_a_file(path_of_images_to_upload, path_of_uploaded_images_file):
    """Return a file to upload randomly."""
    files = []
    for file in os.listdir(path_of_images_to_upload):
        files.append(str(file).replace("-", "_").replace(" ",
                     "_").replace("$", "_").replace("%", "_").replace("@", "_"))

    file = sorted(files)

    already_uploaded = []
    with open(path_of_uploaded_images_file, "r") as uploaded_file:
        for image in uploaded_file:
            already_uploaded.append(image.strip())
    already_uploaded = sorted(already_uploaded)
    available_opts = set(files).difference(already_uploaded)

    # If there are no images to upload return None
    if len(list(available_opts)) == 0:
        return None

    # Return the name of the image to upload
    return random.choice(tuple(available_opts))
