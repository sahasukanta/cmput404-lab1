import requests

# print version
print(requests.__version__)

# get google homepage
print(requests.get("http://www.google.com").text)
