import requests


class Youtube_Reader:
    def __init__(self, API_KEY) -> None:
        self.apikey = API_KEY

    def Read(self, video_id, count=20):
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