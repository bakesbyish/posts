import json
import requests


phone_number_id = "101218452786459"
access_token = "EAALN6CCMvegBAAh4Qm9JZA5Bz9UVE7jKHmIPev2yWotfOos6Yo60GHTpqL8tWjV9bBPdQ7pbgAJ3iw0NOQhPfZC3JuIzNFVxxrwDbNSjd0dNNzDT1tOA5CPoVQ3jBG1na3bQ92Mw5lMMuMOYyMA7olsQvRgSBsNw1nZCfBVgmU7CILZAw09uGxhYZBH1bUVncOive2CnpswZDZD"
recipient_phone_number = "94760471427"

url = f"https://graph.facebook.com/v13.0/{phone_number_id}/messages"
headers = {
    "Authorization": f"Bearer {access_token}",
    'Content-Type': 'application/json'
}

build_number = '2022.1'
build_author = 'Ben Keen'

msg_body_params = [
    {
        "type": "text",
        "text": build_number
    },
]

data = {
    'messaging_product': 'whatsapp',
    'to': recipient_phone_number,
    'type': 'template',
    'template': {
        'name': 'images',
        'language': {
            'code': 'en_US'
        },
        'components': [
            {
                'type': 'body',
                'parameters': msg_body_params
            }
        ]
    }
}

response = requests.post(url, headers=headers, data=json.dumps(data))
response.ok
