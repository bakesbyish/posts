"""Delete operations that relay on Facebook."""
import requests


def upload_fb(image_link, token, page_id):
    """Upload the given image link to the given Facebook credentials."""
    msg = "Please call or WhatsApp on 0717121856. \nIsland wide delivery available \nCash on Delivery or Bank Deposits accepted."
    image_url = 'https://graph.facebook.com/{}/photos'.format(page_id)
    payload = {
        'message': msg,
        'url': image_link,
        'access_token': token
    }
    requests.post(image_url, data=payload)
    print("Finished uploading to facebook")
