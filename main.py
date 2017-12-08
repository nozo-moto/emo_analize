import twitter
import emotional
import json

def make_text(result: dict):
    tweet = "analitics result is \n\
            likedislike:{}\n\
            joysad:{}\
            angerfear:{}".format(
                result["likedislike"],
                result["joysad"],
                result["angerfear"],
            )
    

if __name__ == "__main__":
    with open('key.json', 'r') as f:
        key = json.load(f)['emo_key']
    meta = emotional.Metadata(key)
    twitter = twitter.Twitter()

    tweet = twitter.getTimeLine()
        
    [
        meta.analize(t)
        for t in tweet
    ]
    text = make_text(meta.result)
    twitter.tweetUpdate(text)