from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
import numpy as np

class Sentiment(object):

    sentiment = ["neg","neu","pos"]

    def __init__(self):
        self._compound_score = []

    def analyze(self, paragraph):
        neg_score = []
        neu_score = []
        pos_score = []
        sentences = tokenize.sent_tokenize(paragraph)
        sid = SentimentIntensityAnalyzer()

        for sentence in sentences:
            # print(sentence)
            ss = sid.polarity_scores(sentence)
            sentence_polarity_score = [ss['compound'], ss['neg'], ss['neu'], ss['pos']]
            # print('[compound, neg, neu, pos]')
            # print(sentence_polarity_score)
            neg_score.append(ss['neg'])
            neu_score.append(ss['neu'])
            pos_score.append(ss['pos'])
            self._compound_score.append(ss['compound'])

    def get_compound(self):
        # return sum(self._compound_score)/float(len(self._compound_score))
        return sum(self._compound_score)

    def get_sentiment(self):
        if self.get_compound() >= 0.5:
            return 1
        elif self.get_compound() <= -0.5:
            return -1
        else:
            return 0

    def compile_polarity_scores(self, score_list):
        return

if __name__ == '__main__':
    paragraph = "What if I have multiple sentences? This really sucks! Actually, yeah, this "\
                "is awful. Does it change if i add more? I hate this. This is a awesome paragraph!"

    a = Sentiment()
    a.analyze(paragraph)
    print(a.get_sentiment())
