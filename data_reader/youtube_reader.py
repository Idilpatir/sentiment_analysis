import requests
from urllib.parse import urlparse, parse_qs

class Youtube_Reader:
    def __init__(self, API_KEY) -> None:
        self.apikey = API_KEY


    def _Parse(self, video_url):
        url=urlparse(video_url)
        video_id = parse_qs(url.query)['v'][0]
        return video_id
    

    def Read(self, video_url, count=20):
        video_id = self._Parse(video_url)
        payload = {
            "key" : self.apikey,
            "maxResults" : count,
            "videoId" : video_id,
            "part" : "snippet"
        }
        r = requests.get('https://www.googleapis.com/youtube/v3/commentThreads', params=payload)
        json = r.json()
        result = list()
        for item in json["items"]:
            result.append(item["snippet"]["topLevelComment"]["snippet"]["textDisplay"])

        return result