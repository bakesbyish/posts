"""Delete operations that relay on Facebook."""
import requests


def upload_fb(image_link, token, page_id):
    """Upload the given image link to the given Facebook credentials."""
    msg = "WhatsApp: links.bakesbyish.com/whatsapp\nInstagram: links.bakesbyish.com/ig\nWeb: bakesbyish.com\nLocation: links.bakesbyish.com/map\nIsland wide cash on delivery available"
    image_url = 'https://graph.facebook.com/{}/photos'.format(page_id)
    payload = {
        'message': msg,
        'url': image_link,
        'access_token': token
    }
    requests.post(image_url, data=payload)
    print("Finished uploading to facebook")
