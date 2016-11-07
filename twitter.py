from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Stream



access_token="714283612795842560-0BTetsGCwahWv5DHpg9xOUggknnDWr6"
access_token_secret="Gr6xYBYakIKtaJ01dSQ4Ye4YDlfwgbMQSHB7PmDr2T56M"
consumer_key="z7Tq8GEorjWtRmBzMjnkquLDB"
consumer_secret="cO0odfVYeTeQZ2aJhTrzcBmi29ApkQ1wR1YeQ31JKiG5IhXWAP"

auth=OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

class Listener(StreamListener):
	def on_data(self,data):
		
		print (data)
		f=open("/home/brucewayne/Desktop/twitter.txt","a")
		f.write(data)
		f.write('\n')
		f.close()
		return True
		

if __name__=="__main__":
	l=Listener()
	stream=Stream(auth,l)
	stream.filter(track=['Manchester United'])

