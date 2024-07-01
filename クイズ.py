# ひらがな　と　かたかな　れんしゅうする　のために　パイテョン　の　プログラム
import json
from random import choice

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
    usr_ans = ''
    usr_score = 0
    usr_attempts = 0
    while not usr_ans == 'q':
        hiragana, romaji = choice(list(hiraganas.items()))
        usr_ans = input(f'Enter Romaji for {hiragana}\n')
        if usr_ans.lower() == 'q':
            print(f'Thank you! You scored {usr_score}/{usr_attempts} in the Hiragana quiz.')
            break
        elif usr_ans.lower() == romaji:
            usr_attempts += 1
            usr_score += 1
            print('Correct!')
        else:
            usr_attempts += 1
            print(f'Incorrect! The correct pronunciation is "{romaji}"')

elif user_ask.upper() == 'K':
    quiz_flag = 'Katakana'
    print("===========================")
    print('You will practise Katakana now. You will enter Romaji equivalent of the sounds. Enter "q" in the case you want to quit practice')
    print("===========================")
    usr_ans = ''
    usr_score = 0
    usr_attempts = 0
    while not usr_ans == 'q':
        katakana, romaji = choice(list(katakanas.items()))
        usr_ans = input(f'Enter Romaji for {katakana}\n')
        if usr_ans.lower() == 'q':
            print(f'Thank you! You scored {usr_score}/{usr_attempts} in the Hiragana quiz.')
            break
        elif usr_ans.lower() == romaji:
            print('Correct!')
        else:
            print(f'Incorrect! The correct pronunciation is "{romaji}"')