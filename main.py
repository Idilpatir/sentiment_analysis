from data_reader.youtube_reader import Youtube_Reader 
from dotenv import load_dotenv, dotenv_values
load_dotenv()

reader= Youtube_Reader(dotenv_values(".env")["API_KEY"])
result = reader.Read(video_id="I76wvt0aEE4", count = 3)
print(result)