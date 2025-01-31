from data_reader import Youtube_Reader 
from dotenv import load_dotenv, dotenv_values
from sentiment_analysis import Sentiment_Analyzer
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import asyncio
load_dotenv()

# if __name__ == "__main__":
#     API_KEY = dotenv_values(".env")["API_KEY"]
#     reader = Youtube_Reader(API_KEY)
#     analyzer = Sentiment_Analyzer()

#     video_id = input("Enter video url: ")

#     comments = reader.Read(video_id)

#     for comment in comments:
#         score = analyzer.Analyze(comment)
#         print(f"Comment: {comment}")
#         print(f"Score: {score}")

API_KEY = dotenv_values(".env")["API_KEY"]
reader = Youtube_Reader(API_KEY)
# result=reader.Data_Read("https://www.youtube.com/watch?v=16jA-6hiSUo&list=RD16jA-6hiSUo&start_radio=1")
# print(result)

app = FastAPI()

app.mount("/resources", StaticFiles(directory="resources"), name="static")

@app.get("/")   
async def Website():
    return FileResponse("main.html")

@app.get("/api")
async def Get_Data(video_url : str, count : int = 20):
    return {
        "data" : reader.Data_Read(video_url),
        "comments" : reader.Comments_Read(video_url, count)
    }
    



