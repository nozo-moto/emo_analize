from requests_oauthlib import OAuth1Session
import json

class Twitter:
    def __init__(self):
        with open('key.json', 'r') as f:
            key = json.load(f)['key']
        self.sess = OAuth1Session(key['CONSUMER_KEY'], key['CONSUMER_SECRET_KEY'], key['ACCESS_TOKEN'], key['ACCESS_TOKEN_SECRET'])

    def getTimeLine(self, include_entities = 1, exclude_replies = 1) -> list:
        url = 'https://api.twitter.com/1.1/statuses/home_timeline.json'
        params = {
            'count': 30,
            "include_entities": include_entities,
            "exclude_replies": exclude_replies
        }
        req = self.sess.get(url, params=params)
        timeline = json.loads(req.text)
        tweetdata = [text['text'] for text in timeline]
        return tweetdata

    def tweetUpdate(self, tweet: str):
        url = "https://api.twitter.com/1.1/statuses/update.json"
        params = {"status": tweet}
        req = self.sess.post(url, params=params)
        if req.status_code == 200:
            print("Tweet Succeed!\t" + tweet)
        else:
            print("ERROR : %d" % req.status_code)

if __name__ == "__main__":
    twitter = Twitter()
    tweet = twitter.getTimeLine()
    print(tweet)

