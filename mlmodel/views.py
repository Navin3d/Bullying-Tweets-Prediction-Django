from rest_framework.decorators import api_view
from tensorflow import keras
import re
import string
from nltk.corpus import stopwords
from keras.preprocessing import text
from nltk import word_tokenize
from rest_framework.response import Response
from pathlib import Path
from keras.utils import pad_sequences


max_words = 10000
tokenizer = text.Tokenizer(num_words = max_words)

stoplist = stopwords.words('english')


def remove_punct(text_data):
    text_nopunct = ''
    text_nopunct = re.sub('['+string.punctuation+']', '', str(text_data))
    return text_nopunct


def lower_token(tokens):
    return [word.lower() for word in tokens]


def removeStopWords(tokens):
    return [w for w in tokens if w not in stoplist]


def removenumeric(tokens):
    return [w for w in tokens if not w.isdigit()]


lstm_model = keras.models.load_model(Path("D:\\Programming\\Python\\Django\\offensive_tweets\\static\\ml_models\\lstm_model_final.h5"))


def Predict(predict_text):
    predict_text=remove_punct(predict_text)
    predict_text=word_tokenize(predict_text)
    predict_text=lower_token(predict_text)
    predict_text=removeStopWords(predict_text)
    predict_text=removenumeric(predict_text)
    predict_text=tokenizer.texts_to_sequences(predict_text)
    predict_text=pad_sequences(predict_text)
    return predict_text


@api_view(["POST"])
def predict_tweet(request):
    data = request.data
    input_tweet = data["tweet"]
    print(input_tweet)
    processed_tweet = Predict([input_tweet])
    predictions = lstm_model.predict(processed_tweet)
    predictions = predictions[0]
    result = "Not Cyber Bullying..."
    if predictions > 0.5:
        result = "Is Cyber Bullying..."
    response = {
        "status": "OK",
        "prediction": result
    }

    return Response(status=200, data=response)
