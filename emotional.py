import urllib.request
import urllib.parse
import json
import math

EMOTIN_URL = "http://ap.mextractr.net/emotion_measure"
with open('key.json', 'r') as f:
    APIKEY = json.load(f)['emo_key']

class Metadata():
    def __init__(self, apikey: str):
        self.Params = {
            "out" : "json",
            "apikey" : apikey,
            "text": ""
        }
        self.result = {
            "likedislike" : 0,
            "joysad" : 0,
            "angerfear" : 0,
            "num" : 0
        }

    def analize(self, text: str):
        self.set_text(text)
        self.request()
    
    def set_text(self, text: str):
        self.Params["text"] = text

    def request(self):
        request_url = self.encode_url()
        with urllib.request.urlopen(request_url) as res:
            res_body = res.read().decode("utf-8")
            res_dict = json.loads(res_body)
            self.analize_res(res_dict)

    def analize_res(self, res: dict):
        self.result["likedislike"] += res["likedislike"]
        self.result["joysad"] += res["joysad"]
        self.result["angerfear"] += res["angerfear"]
        self.result["num"] += 1
    
    def adjust_result(self, point: int):
        return math.pow(point)

    def encode_url(self) ->str:
        encodedParams = urllib.parse.urlencode(
            self.Params
        )
        url = "{}?{}".format(EMOTIN_URL, encodedParams)
        return url

    def result(self) -> dict:
        return {
            "likedislike": math.sqrt(self.result["likedislike"]),
            "joysad": math.sqrt(self.result["joysad"]),
            "angerfear": self.result["angerfear"],
            "num": self.result["num"]
        }

if __name__ == '__main__':
    meta = Metadata(APIKEY)
    meta.analize("俺は昨年末に会社を首になって、それからはずっと倉庫でバイトをしている。いわゆるおっさんフリーターってやつだ。33才。当然、お先真っ暗。でも特に嘆いたり悲しんだりはしない。もうそんな段階はとっくにこえてしまった。まあ人生こんなもんだろ、しかたねーやって感じ。学歴もコネも才能もない。石の裏に棲息する虫みたいに、ひっそり生きて死ぬ。それでいい。たまに小さな幸福を拾えたら御の字。拾えないならそれもまたよし。")
    meta.analize("夏にＳさんという男が新たにバイトとして入ってきた。俺よりひとまわり年上の45才。とにかく無口なおっさんだった。俺もかなり無口な方だが、Ｓさんにはかなわない。")
    meta.analize("俺とＳさんは同じエリアを担当することになった。そこは最もコミュニケーションを必要とされない業務内容で、俺やSさんのような人間にはうってつけの場所だった。")
    meta.analize("いつのまにか俺はＳさんと仲良くなっていた。無口な者同士で妙にうまがあい、仕事の後にふたりで飲みにいくようになった。酒の席でもあまり会話はしなかった。お互いに黙って、自分達のペースで手酌で飲む。それが心地よかった。")
    meta.analize("先週、ふたりで飲んでいたら終電を逃してしまった。Ｓさんのアパートがタクシーでワンメーターの距離だったので、泊めてもらうことにした。Ｓさんは独身でひとり暮しだった。部屋についてからさらに飲み直した。ふたりとも休日前だったので、心置きなく飲むことができた。Ｓさんはかなり酔っていて、見違えるぐらい饒舌になっていた。")
    meta.analize("Ｓさんが俺に缶を渡す。きんきんに冷えている。500mlのロング缶。どこからどうみてもストロングゼロだった。実物を見るのは初めてだった。俺にとってストロングゼロは文学の中にしか存在しない酒だった。Ｓさんが語りだす。")
    print(meta.result)

