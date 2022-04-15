import requests

username = "hsdturkey"
url = 'https://www.instagram.com/' + username
r = requests.get(url).text

start = '"edge_followed_by":{"count":'
end = '},"followed_by_viewer"'
followers= r[r.find(start)+len(start):r.rfind(end)]

start = '"edge_follow":{"count":'
end = '},"follows_viewer"'
following= r[r.find(start)+len(start):r.rfind(end)]

print(followers, following)
