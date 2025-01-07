from data_reader.youtube_reader import Youtube_Reader 
from dotenv import load_dotenv, dotenv_values
from sentiment_analysis.sentimet_analysis import Sentiment_Analyzer
load_dotenv()

Analyzer = Sentiment_Analyzer()
print(Analyzer.Analyze("shit.a !!!!"))
print(Analyzer.Analyze("very bad!!"))
print(Analyzer.Analyze("avarage"))
print(Analyzer.Analyze("good"))
print(Analyzer.Analyze("very good!?!?"))
