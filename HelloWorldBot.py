from flask import Flask, request
import requests
import json
import traceback
import random
import pafy
app = Flask(__name__)

token = "EAAaCZAcRNubwBAC2ZCjqxWsEPTLCi0BvhqSwUy59SC8vZAyLEuTLMjyKhxZC1RoZAnGwfX0HHzwkxpk9Oh0eaK3KcLF1SYPPpaoPBRvYnUCqh5IU0OsJ14lixdr8HiqqKtneJD970Wp7VuuZCMtYs7xULKBIZBjyINxZCEZCOgYtpXwZDZD"

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
  if request.method == 'POST':
    try:
      data = json.loads(request.data)
      text = data['entry'][0]['messaging'][0]['message']['text'] # Incoming Message Text
      sender = data['entry'][0]['messaging'][0]['sender']['id'] # Sender ID
      # Undergoing Job Here
      # Hay Hay Ho
      link = pafy.new(data['text'])
      mystream = link.getbest()
      mystream.rawbitrate
      mystream.bitrate
      mystream.url
      # This is the End!
      # This is the real end.
      payload = {'recipient': {'id': sender}, 'message': {'text': mystream.url}} # We're going to send this back
      r = requests.post('https://graph.facebook.com/v2.6/me/messages/?access_token=' + token, json=payload) # Lets send it
    except Exception as e:
      print (traceback.format_exc()) # something went wrong
  elif request.method == 'GET': # For the initial verification
    if request.args.get('hub.verify_token') == 'HelloWorldFromKaMiSaMa':
      return request.args.get('hub.challenge')
    return "Wrong Verify Token"
  return "Thank You" #Not Really Necessary

if __name__ == '__main__':
  app.run(debug=True)
