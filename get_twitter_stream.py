import json
import requests
from requests_oauthlib import OAuth1
from datetime import datetime
import re

class MyTwitterStream:
    """
    use Twitter Streaming API
    """
    def __init__(self):
        '''
        initialize
        '''
        self.auth = OAuth1(
            API_KEY,
            API_SECRET,
            ACCESS_TOKEN,
            ACCESS_SECRET
        )
        self.stream = requests.get(
            "https://stream.twitter.com/1.1/statuses/sample.json",
            auth=self.auth,
            stream=True,
        )

    def get_tweets(self):
        '''
        Tweet（JSON形式）を取得して、必要な情報を抜き出す（TSV形式）
        '''
        for line in self.stream.iter_lines():
            try:
                status = json.loads(line.decode("utf-8"))
            except:
                continue

            if not 'created_at' in status:
                continue

            daytime = self.convert_datetime(status['created_at'])

            user_created_at = self.convert_datetime(status['user']['created_at'])
            retweet_count = status['retweet_count'] if 'retweet_count' in status else 0
            favorite_count = status['favorite_count'] if 'favorite_count' in status else 0

            text = re.sub(r'[\r\n\t]+', " ", status['text'])
            tsv = f"{status['id']}\t{daytime}\t{status['user']['screen_name']}\t{status['user']['id']}\t{user_created_at}\t{status['user']['statuses_count']}\t{status['user']['friends_count']}\t{status['user']['followers_count']}\t{retweet_count}\t{favorite_count}\t{text}"

            outname = self.convert_datetime_str(status['created_at'])
            yield (outname, tsv)

    def convert_datetime(self, created_at):
        '''
        Twitterの日時表現を年月日時分秒（'yyyy-mm-dd hh:MM:ss'）に変換する
        '''
        dt = datetime.strptime(created_at, '%a %b %d %H:%M:%S %z %Y')
        dt = dt.astimezone()
        dst = datetime.strftime(dt, '%Y-%m-%d %H:%M:%S')
        return dst

    def convert_datetime_str(self, created_at):
        '''
        Twitterの日時表現を年月日時（'yyyymmdd_hh'）に変換する
        '''
        dt = datetime.strptime(created_at, '%a %b %d %H:%M:%S %z %Y')
        dt = dt.astimezone()
        dst = datetime.strftime(dt, '%Y%m%d_%H')
        return dst

if __name__ == '__main__':
    mystream = MyTwitterStream()
    for (outname, tsv) in mystream.get_tweets():
        filename = outname+'.txt'
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(tsv+'\n')
