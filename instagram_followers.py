import requests
from bs4 import BeatifulSoup

username = "hsdturkey"
url = 'https://www.instagram.com/' + username
r = requests.get(url)
soup=BeatifulSoup(r.content)
followers=soup.find()

start = '"edge_follow":{"count":'
end = '},"follows_viewer"'
following= r[r.find(start)+len(start):r.rfind(end)]

print(followers, following)
