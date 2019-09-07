import datetime
import time 

import GetOldTweets3 as got
from bs4 import BeautifulSoup

from random import uniform
from tqdm import tqdm_notebook
import pandas as pd 

def crawling():
    days_range=[]

    start =datetime.datetime.strptime("2019-08-07","%Y-%m-%d")
    end =datetime.datetime.strptime("2019-08-19","%Y-%m-%d")
    date_generated=[start+datetime.timedelta(days=x)
                    for x in range(0,(end-start).days)]

    for date in date_generated:
        days_range.append(date.strftime("%Y-%m-%d"))

    print("===트윗 수집 기간은 {}에서 {}까지 입니다===".format(days_range[0],days_range[-1]))
    print("총 {}일간의 데이터 ".format(len(days_range)))

    start_date=(days_range[0])
    end_date=(datetime.datetime.strptime(days_range[-1],"%Y-%m-%d")
                +datetime.timedelta(days=1)).strftime("%Y-%m-%d")


    tweetCriteria=got.manager.TweetCriteria().setQuerySearch("(from:nctsmtown_dream)")\
                                            .setSince(start_date)\
                                            .setUntil(end_date)\
                                            .setMaxTweets(-1)


    #collect
    start_time=time.time()

    tweet=got.manager.TweetManager.getTweets(tweetCriteria)

    print ("collectin data end.. {0:0.2f} Minutes".format((time.time()-start_time)/60))
    print("===Total num or tweet is {}===".format(len(tweet)))

    tweet_list=[]

    for index in tweet:
        
        # 메타데이터 목록 
        username = index.username
        link = index.permalink 
        content = index.text
        tweet_date = index.date.strftime("%Y-%m-%d")
        tweet_time = index.date.strftime("%H:%M:%S")
        hashtag=index.hashtags
        mention=index.mentions
        # retweets = index.retweets
        # favorites = index.favorites
        # 결과 합치기
        info_list = [tweet_date ,tweet_time,username,content,link,hashtag]
        tweet_list.append(info_list)

        
        # 휴식 
        time.sleep(uniform(1,2))

    # #파일 저장
    # twitter_df=pd.DataFrame(tweet_list,
    #                         columns = ["date", "time", "user_name", "text", "link", "retweet_counts", "favorite_counts"])
    # # csv 파일 만들기
    # twitter_df.to_csv("sample_twitter_data_{}_to_{}.csv".format(days_range[0], days_range[-1]), index=False)
    # print("=== {} tweets are successfully saved ===".format(len(tweet_list)))

    # df_tweet = pd.read_csv('sample_twitter_data_{}_to_{}.csv'.format(days_range[0], days_range[-1]))
    # df_tweet.head(10) # 위에서 10개만
    
    return tweet_list
