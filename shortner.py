import requests
import json
import sys

def shortner(url):
    api = "https://redr.me/api/link/"
    post = {
        "target_url": url
    }
    r = requests.post(api,data=post).text
    output = json.loads(r)
    code = output["code"]
    return "https://redr.me/"+code

if __name__ == "__main__":
    if len(sys.argv) != 2 :
        print("Usage: python shortner.py https://example.com")
        exit()
    else:
        pass
    target = sys.argv[1]
    if "http" not in target:
        target = "http://"+target
    else:
        pass
    shorted_url = shortner(target)
    print(shorted_url)