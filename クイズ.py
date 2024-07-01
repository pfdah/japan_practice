# ひらがな　と　かたかな　れんしゅうする　のために　パイテョン　の　プログラム
import json
from random import random

# Section: Load Data
file = open('./char_map.json')
data = json.load(file)

# Section: Data Handling:
hiraganas = data['hiragana']
katakanas = data['katakana']


# Section: User Prompt Handling
quiz_flag = ''
user_ask = input("Enter what you want to practice: Hiragana(H) or Katakan(K):\n")
while not user_ask.upper() == 'H' or user_ask.upper() == 'K':
    print("Invalid input.")
    user_ask = input("Enter what you want to practice: Hiragana(H) or Katakan(K) (use one letter):\n")

if user_ask.upper() == 'H':
    quiz_flag = 'Hiragana'
    print("===========================")
    print('You will practise Hiragana now. You will enter Romaji equivalent of the sounds. Enter "q" in the case you want to quit practice')
    print("===========================")
    while not usr_ans == 'q':
        hiragana, romaji = random.choice(list(hiraganas.items()))
        usr_ans = input(f'Enter Romaji for {hiragana}\n')
        if usr_ans.lower() == 'q':
            print('Thank you!')
            break
        elif usr_ans.lower() == romaji:
            print('Correct!')
        else:
            print(f'Incorrect! The correct pronunciation is "{romaji}"')

elif user_ask.upper() == 'K':
    quiz_flag = 'Katakana'
    print("===========================")
    print('You will practise Katakana now. You will enter Romaji equivalent of the sounds. Enter "q" in the case you want to quit practice')
    print("===========================")
    while not usr_ans == 'q':
        katakana, romaji = random.choice(list(katakanas.items()))
        usr_ans = input(f'Enter Romaji for {katakana}\n')
        if usr_ans.lower() == 'q':
            print('Thank you!')
            break
        elif usr_ans.lower() == romaji:
            print('Correct!')
        else:
            print(f'Incorrect! The correct pronunciation is "{romaji}"')