import requests
import os
import bs4

url = 'http://imgur.com/topic/The_Great_Outdoors'
os.makedirs('imgur', exist_ok=True)


print('Downloading page %s...' % url)
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.txt)
postElem = soup.select('a img')if postElem == []:
    print('Could not find the posts images.')
else:
    for i in range(0, len(postElem)):
        postUrl = 'http:' + postElem[i].get('src')
        print('Downloading image %s...' % (postUrl))
        res = requests.get(postUrl)
        res.raise_for_status()
        imageFile = open(os.path.join('imgur', os.path.basename(postUrl)), 'wb')
        for chunk in res.iter_content(1000000):
            imageFile.write(chunk)
        imageFile.close()


print('Done.')