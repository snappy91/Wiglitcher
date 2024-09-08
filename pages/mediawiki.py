"""Utility class for Wikimedia API calls"""

import datetime
import requests, json


base_url_random = 'https://commons.wikimedia.org/w/api.php?action=query&list=random&rnnamespace=6&format=json'
base_url_image = 'https://commons.wikimedia.org/w/api.php?action=query&prop=imageinfo&format=json'
def get_random_images(count=1):
    url = base_url_random + '&rnlimit=%d' % count
    response = requests.get(url)
    jsondata = json.loads(response.text)
    imagelist = '|'.join(img['title'] for img in jsondata['query']['random'])

    url2 = base_url_image + '&titles=' + imagelist + '&iilimit=50&iiprop=timestamp|user|url|size|thumbnail'
    response2 = requests.get(url2)
    imagedata = json.loads(response2.text)

    idqp = imagedata['query']['pages']
    imagedata = [ idqp[img]['imageinfo'] for img in idqp.keys() ][0]
    #print(imagedata)
    return [{
        'thumbnail_url': img['url'],
        'image_width': img['width'],
        'image_height': img['height'],
        'description_text': img['descriptionurl'].replace('https://commons.wikimedia.org/wiki/File:', '').replace('_', ' '),
        'artist_name': img['user'],
        'attribution_url': img['descriptionshorturl'],
        'license_name': '?',
        'license_url': '?',
    } for img in imagedata ]

