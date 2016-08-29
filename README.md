## Tweet My Mood
Tweet My Mood takes an image of a face as input and uses a Markov chain generator to tweet based off the emotion of the face. </br>
First, mine the data. We use Tweepy to stream live Twitter data with certain hashtags and then save them to a text file. </br>
Then, we use Microsoft Emotion API to determine the emotion of the picture. We tweet based on the highest shown emotion. </br>
We use Markovify to generate a (somewhat) realistic sentence using our source text files. Each word is selected based on how often it follows the previous word in the source. </br>
Lastly, we use Tweepy to post the tweet and update the current mood at https://twitter.com/tweetMyMoodBot. </br>

## Dependencies
Microsoft Emotion API <br />
Tweepy <br />
Markovify </br>


## How to run
First, register your app and get your Twitter API keys from https://dev.twitter.com. Add these into a file named creds.py. This program WILL NOT WORK unless you add your API keys. </br>

You can choose to mine your own data for the emotion files by running getdata.py, or you can use the data from the file named "data".
First, install the required packages. </br>
```
pip install virtualenv
git clone https://github.com/bronwynbiro/tweetMyMoodBot.git
cd tweetMyMoodBot
source venv/bin/activate
pip install markovify
pip install tweepy

```

Then run:

```python
python main.py 'https://www.yourLinkToAPhoto.com'
```

 <br />

## Future improvements
The tweet data was taken from a live Twitter stream based on hashtags of the desired emotion. I'd like to do build a classifier by using an annotated corpus. Classifcation could be done using a Maximum Entropy
Classifier.
