import sys
import requests
import json
if len(sys.argv) != 2:
    sys.exit("Please provide a single argument for the API request.")
response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term="+ sys.argv[1])
for result in response.json()["results"]:
    print(result["trackName"], result["previewUrl"])