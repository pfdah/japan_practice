# ひらがな　と　かたかな　れんしゅうする　のために　パイテョン　の　プログラム
import json

# Section: load data
file = open('./char_map.json')
data = json.load(file)

# Data handling:
hiraganas = data['hiragana']
katakanas = data['kanji']

user_ask 