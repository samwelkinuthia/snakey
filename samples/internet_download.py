import random, urllib.request

def downloader():
    name = random.randint(1, 20)
    image_name = str(name) + ".jpg"
    print("enter the image url")
    url = str(input())
    urllib.request.urlretrieve(url, image_name)
downloader()
