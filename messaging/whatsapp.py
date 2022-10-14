"""Send messages with WhatsApp."""
import json
import requests
from settings import whatsapp_accsess_token, whatsapp_phonenumber_id, whatsapp_recepient_phone_number

url = f"https://graph.facebook.com/v13.0/{whatsapp_phonenumber_id}/messages"
headers = {
    "Authorization": f"Bearer {whatsapp_accsess_token}",
    'Content-Type': 'application/json'
}


def all_images_uploaded():
    """Send to notify that all the images have been uploaded."""
    data = {
        'messaging_product': 'whatsapp',
        'to': whatsapp_recepient_phone_number,
        'type': 'template',
        'template': {
            'name': 'done_uploading',
            'language': {
                'code': 'en_US'
            },
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response.ok


def reminder_to_upload_more_photos():
    """Send a reminder to upload more photos."""
    data = {
        'messaging_product': 'whatsapp',
        'to': whatsapp_recepient_phone_number,
        'type': 'template',
        'template': {
            'name': 'reminder',
            'language': {
                'code': 'en_US'
            },
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response.ok


def send_uploaded_image_detials(image_link, product_title, product_code, platform):
    """Send a message describing the uploaded image."""
    data = {
        'messaging_product': 'whatsapp',
        'to': whatsapp_recepient_phone_number,
        'type': 'template',
        'template': {
            'name': 'uploaded_image',
            'language': {
                'code': 'en_US'
            },
            'components': [
                {
                    'type': 'header',
                    'parameters': [
                        {
                            'type': 'image',
                            'image': {
                                'link': image_link
                            }
                        },
                    ]
                },
                {
                    'type': 'body',
                    'parameters': [
                        {
                            'type': 'text',
                            'text': product_title
                        },
                        {
                            'type': 'text',
                            'text': product_code
                        },
                        {
                            'type': 'text',
                            'text': platform
                        },
                    ]
                }
            ]
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response.ok


def renaming_error(file_name):
    """Alert the user that a specific file renamming pattern was wrong."""
    data = {
        'messaging_product': 'whatsapp',
        'to': whatsapp_recepient_phone_number,
        'type': 'template',
        'template': {
            'name': 'renaming_error',
                'language': {
                    'code': 'en_US'
                },
            'components': [
                {
                    'type': 'body',
                    'parameters': [
                        {
                            'type': 'text',
                            'text': file_name
                        },
                    ]
                }
            ]
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response.ok
