# know the size of a image from a url
from PIL import Image
from io import BytesIO
import requests

response = requests.get('https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png')
img = Image.open(BytesIO(response.content))
width, height = img.size

aspect_ratio = width / height

print('{{{0}:{1}}}'.format(width, height))

