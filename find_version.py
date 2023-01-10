import requests

# print version
print(requests.__version__)

# get google homepage
# print(requests.get("http://www.google.com").text)


print(requests.get("https://raw.githubusercontent.com/sahasukanta/cmput404-lab1/master/find_version.py").text)


