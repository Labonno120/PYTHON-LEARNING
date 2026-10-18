import requests
import sys
import json
if len(sys.argv) != 2:
    sys.exit("Please provide a single argument for the API request.")
response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term="+ sys.argv[1])
print(json.dumps(response.json(), indent = 2))