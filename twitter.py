from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Stream, Cursor, API,api
import pygame,sys
from pygame.locals import *
import simplejson

access_token="714283612795842560-0BTetsGCwahWv5DHpg9xOUggknnDWr6"
access_token_secret="Gr6xYBYakIKtaJ01dSQ4Ye4YDlfwgbMQSHB7PmDr2T56M"
consumer_key="z7Tq8GEorjWtRmBzMjnkquLDB"
consumer_secret="cO0odfVYeTeQZ2aJhTrzcBmi29ApkQ1wR1YeQ31JKiG5IhXWAP"

auth=OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=API(auth)


pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption('Twitter')	

background=pygame.Surface(screen.get_size())
background=background.convert()
background.fill((250,250,250))

L=[]
for status in Cursor(api.home_timeline).items(10):   #read homepage
	L.append(status.text)

font = pygame.font.Font(None,16)
for i in L:
	text=font.render(i,1,(10,10,10))
textpos=text.get_rect()
textpos.centerx=background.get_rect().centerx
background.blit(text, textpos)

screen.blit(background,(0,0))
pygame.display.flip()

while 1:
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()

	screen.blit(background,(0,0))
	pygame.display.flip()

def process_store(tweet):
	print(json.loads(tweet))





for status in Cursor(api.home_timeline).items(10):   #read homepage
	print (status.text)

for friend in Cursor(api.friends).items():
	process_store(friend)

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


