'''
Experimental algorithm to invest based on sentiment analysis
'''

import subprocess, json, nltk
from utils import destructure
from datetime import datetime
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
from nltk.tokenize import word_tokenize

def compute_sentiment_scores(d):
    sia = SIA()
    scores = []
    for entry in d:
        title_pol_score = sia.polarity_scores(entry['title'])
        summary_pol_score = sia.polarity_scores(entry['summary'])

        # get compound title score, compound summary score, time of news item,
        # and number of clicks for news item
        scores.append({'title_score': title_pol_score['compound'],
            'summary_score': summary_pol_score['compound'], 'time':
            entry['updated_at'], 'num_clicks': entry['num_clicks']})

    return scores

def sentiment_analysis(**kwargs): 
    defaults = {
        'n_shares': 0,
        'index': 0,
        'sentiments': []
        'times': []
    }

    defaults.update(kwargs)

    n_shares, index, sentiments, times = destructure(defaults, ('n_shares', 'index', 'sentiments', 'times'))

    scores = compute_sentiment_scores(sentiments)

    # weight attributed to title and summary of news item
    title_score_weight = 0.7
    summary_score_weight = 0.3

    # weighted score is a value between [-1, 1]
    # threshold values indicate when to buy or sell
    buy_threshold = 0.7
    sell_threshold = -0.7

    if index+1<len(times):
        start_date = datetime.strptime(times[index], '%Y-%m-%dT%H:%M:%SZ')
        end_date = datetime.strptime(times[index+1], '%Y-%m-%dT%H:%M:%SZ')
        cum_score = 0
        total_clicks = 0
        for sentiment in sentiments:
            sentiment_date = datetime.strptime(sentiment['time'], '%Y-%m-%dT%H:%M:%S.%fZ') 
            # check if news item lies in relevant date range and accumulate
            # score, number of clicks
            if sentiment_date<end_date and sentiment_date>start_date:
                cum_score += (sentiment['title_score']*title_score_weight +
                        sentiment['summary_score']*summary_score_weight)*sentiment['num_clicks']
                total_clicks += sentiment['num_clicks']

            # compute weighted score and buy/sell accordingly
            if total_clicks>0
                weighted_score = cum_score/total_clicks
                if weighted_score>buy_threshold:
                    return n_shares+1
                elif weighted_score<sell_threshold:
                    return n_shares-1
                else:
                    return n_shares
            else:
                return n_shares
    return n_shares
