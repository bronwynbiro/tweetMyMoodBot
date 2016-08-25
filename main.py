import sys
sys.path.append('/usr/local/lib/python2.7/site-packages/')
import httplib, urllib, base64, json
import creds
import tweepy
import markovify
import twitter

if len(sys.argv) < 1:
    print("You need to include a link to a photo")
else:
    photofile = sys.argv[1]

def generateTweet(mood):
    filename = ("{}.txt").format(mood)
    with open(filename) as f:
        text = f.read()

    stripped = stripNonASCII(text)
    text = ''.join(stripped)
    text_model = markovify.Text(text)
    sentence = text_model.make_short_sentence(120)
    return sentence.encode('utf-8')

def stripNonASCII(string):
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)


def main():
    #body = {"URL": "http://www.scientificamerican.com/sciam/cache/file/35391452-5457-431A-A75B859471FAB0B3.jpg" }
    body = {"URL": photofile }

    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': 'bc5d8b32ff754da895daa0043add9f8c',
    }

    try:
        conn = httplib.HTTPSConnection('api.projectoxford.ai')
        conn.request("POST", "/emotion/v1.0/recognize", json.dumps(body) , headers)
        response = conn.getresponse()
        data = response.read()
        print("DATA:", data)
        jsonResponse = json.loads(data)
        print("json.loads complete")
        scores = jsonResponse[0]['scores']
        print("SCORES", scores)

        emotions = {}
        emotions['anger'] = jsonResponse[0]['scores']['anger']
        emotions['sadness'] = jsonResponse[0]['scores']['sadness']
        emotions['neutral'] = jsonResponse[0]['scores']['contempt']
        emotions['disgust'] = jsonResponse[0]['scores']['disgust']
        emotions['surprise'] = jsonResponse[0]['scores']['surprise']
        emotions['fear'] = jsonResponse[0]['scores']['fear']
        emotions['happiness'] = jsonResponse[0]['scores']['happiness']
        inverse = [(value, key) for key, value in emotions.items()]
        highestEmotionVal = max(inverse)[0]
        highestEmotion = max(inverse)[1]
        print("highestEmotion", highestEmotion)
        print("highestEmotionVal", highestEmotionVal)
        conn.close()
    except Exception as e:
        print("Error")


    twitter.updateDescription("Current mood: {}".format(highestEmotion))
    text = generateTweet(highestEmotion)
    twitter.postTweet(text)

if __name__ == "__main__":
    main()
