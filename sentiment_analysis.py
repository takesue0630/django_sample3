from deep_translator import GoogleTranslator
from textblob import TextBlob

text = '今日はいい天気だった。日差しが暖かかった。'
# text = '今日は雨が降っていた。洗濯物を取り込み忘れたせいで、再び濡れてしまい洗濯が二度手間となった。'

trans_text = GoogleTranslator(source='auto', target='en').translate(text)

print(trans_text)

blob = TextBlob(trans_text)

sentiment = blob.sentiment.polarity

print(sentiment)

if sentiment > 0:
    print("ポジティブな感情です。")
elif sentiment < 0:
    print("ネガティブな感情です。")
else:
    print("ニュートラルな感情です。")