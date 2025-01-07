from data_reader.youtube_reader import Youtube_Reader 
from dotenv import load_dotenv, dotenv_values
from sentiment_analysis.sentimet_analysis import Sentiment_Analyzer
load_dotenv()

if __name__ == "__main__":
    API_KEY = dotenv_values(".env")["API_KEY"]
    reader = Youtube_Reader(API_KEY)
    analyzer = Sentiment_Analyzer()

    video_id = input("Enter video url: ")

    comments = reader.Read(video_id)

    for comment in comments:
        score = analyzer.Analyze(comment)
        print(f"Comment: {comment}")
        print(f"Score: {score}")


