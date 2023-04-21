import nltk

from nltk.tokenize import word_tokenize, sent_tokenize
import heapq

nltk.download('stopwords')
from nltk.corpus import stopwords
def nltk_summarizer(raw_text):
    stopWords = set(stopwords.words("english"))
    word_frequency={}
    for word in nltk.word_tokenize(raw_text):
        if word not in stopWords:
            if word not in word_frequency.keys():
                word_frequency[word]=1
            else:
                word_frequency[word]+=1
    maximum_frequency=max(word_frequency.values())
    for word in word_frequency.keys():
        word_frequency[word]=(word_frequency[word]/maximum_frequency)

    sentence_list=nltk.sent_tokenize(raw_text)
    sentence_score={}
    for sent in sentence_list:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_frequency.keys():
                if len(sent.split(' '))<30:
                    sentence_score[sent]=word_frequency[word]
                else:
                    sentence_score[sent]=word_frequency[word]

    summary_sentence=heapq.nlargest(7,sentence_score,key=sentence_score.get)
    summary=' '.join(summary_sentence)
    return summary