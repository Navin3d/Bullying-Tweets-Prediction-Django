from rest_framework.decorators import api_view
from rest_framework.response import Response
import tensorflow as tf


loaded_model = tf.keras.models.load_model("D:\\Programming\\Python\\Django\\offensive_tweets\\static\\ml_models\\Cyber_Disaster")


@api_view(["POST"])
def predict_tweet(request):
    data = request.data
    input_tweet = data["tweet"]
    print(input_tweet)
    predictions = loaded_model.predict([input_tweet])
    predictions = predictions[0][0]
    result = "Not Cyber Bullying..."
    if predictions > 0.5:
        result = "Is Cyber Bullying..."
    response = {
        "status": "OK",
        "prediction": result
    }
    return Response(status=200, data=response)
