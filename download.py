from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from dotenv import load_dotenv
import traceback
import os, time, sys

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

key       = os.environ.get("FlickrAPI_KEY")
secret    = os.environ.get("FlickrAPI_SECRET")
wait_time = 1

keyword = sys.argv[1]
savedir = "./data/" + keyword

flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
    text = keyword,
    text_page=400,
    media='photos',
    sort='relevance',
    safe_search=1,
    extras='url_q, license'
)

photos = result['photos']

for i, photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    filepath = savedir + '/' + photo['id'] + '.jpg'
    if os.path.exists(filepath): 
        continue
    try:
        urlretrieve(url_q, filepath)
        time.sleep(wait_time)
    except Exception as e:
        print(traceback.format_exc())
        continue
