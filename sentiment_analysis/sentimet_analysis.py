from nltk.sentiment.vader import SentimentIntensityAnalyzer
import re

class Sentiment_Analyzer:
    def __init__(self) -> None:
        self.Analyzer = SentimentIntensityAnalyzer()

    def _Clean(self,text: str) -> str:
        return " ".join(re.sub(r'[^\w?!]', ' ', text).split())   ####

    def Analyze(self, text: str) -> int:
        clean_text = self._Clean(text)
        score = self.Analyzer.polarity_scores(clean_text)
        comp = score["compound"]
        return (comp+1)*5