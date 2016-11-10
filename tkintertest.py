import json
import pandas as pd
import matplotlib.pyplot as plt
import re
import Tkinter	
import tkMessageBox
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Stream, Cursor, API,api
import pygame,sys
from pygame.locals import *
import simplejson
from ScrolledText import *

access_token="714283612795842560-0BTetsGCwahWv5DHpg9xOUggknnDWr6"
access_token_secret="Gr6xYBYakIKtaJ01dSQ4Ye4YDlfwgbMQSHB7PmDr2T56M"
consumer_key="z7Tq8GEorjWtRmBzMjnkquLDB"
consumer_secret="cO0odfVYeTeQZ2aJhTrzcBmi29ApkQ1wR1YeQ31JKiG5IhXWAP"

auth=OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=API(auth)

top=Tkinter.Tk()
menubar = Tkinter.Menu(top)
filemenu = Tkinter.Menu(menubar, tearoff=0)

filemenu.add_command(label="Exit", command=top.quit)
menubar.add_cascade(label="File", menu=filemenu)

def test1():
	for status in Cursor(api.home_timeline).items(10):   #read homepage
   		tkMessageBox.showinfo("Tweets from my homepage", status.text)

def test2():
	tkMessageBox.showinfo( "Extracting tweets", "Tweets")
	tkMessageBox.showinfo( "Extracting tweets", "Keyboard interrupt in terminal to stop process")
	class Listener(StreamListener):
		def on_data(self,data):
			print (data)
			f=open("/home/brucewayne/Desktop/twitter.txt","a")
			f.write(data)
			f.write('\n')
			f.close()
			return True

	l=Listener()
	stream=Stream(auth,l)
	stream.filter(track=['Manchester United'])

def test3():
	tweets_data_path="/home/brucewayne/Desktop/twitter.txt"
	tweets_data=[]
	tweets_file=open(tweets_data_path,"r")

	for line in tweets_file:
		try:
			tweets_data.append(json.loads(line))
		except:
			pass

	print len(tweets_data)

	tweets=pd.DataFrame()
	tweets["lang"]=map(lambda tweet:tweet['lang'],tweets_data)

	try:
		tweets_by_lang=tweets['lang'].value_counts()
	except:
		pass

	fig,ax=plt.subplots()
	ax.tick_params(axis='x',labelsize=15)
	ax.tick_params(axis='y',labelsize=10)
	ax.set_xlabel('Languages',fontsize=15)
	ax.set_ylabel('Number of Tweets',fontsize=15)
	ax.set_title('Top 5 Languages',fontsize=15,fontweight='bold')
	tweets_by_lang[:5].plot(ax=ax,kind='bar',color='blue')
	plt.show()

def test4():
	tweets_data=[]
	f=open("/home/brucewayne/Desktop/twitter.txt","r")
	for line in f:
		try:
			tweets_data.append(json.loads(line))
		except:
			pass

	tweets=pd.DataFrame()
	tweets["text"]=map(lambda tweet:tweet['text'],tweets_data)
	tweets["lang"]=map(lambda tweet:tweet['lang'],tweets_data)

	def onclick():
   		pass

	root1 = Tkinter.Tk()
	root2 = Tkinter.Tk()
	text1 = ScrolledText(root1,wrap=Tkinter.WORD)
	text2 = ScrolledText(root2,wrap=Tkinter.WORD)
	text1.insert(Tkinter.INSERT, tweets["text"])
	text2.insert(Tkinter.INSERT, tweets["lang"])
	text1.pack()
	text2.pack()
	root1.mainloop()
	root2.mainloop()
	
B = Tkinter.Button(top, text ="Display homepage tweets", command = test1, height=10, width=20, background="black",fg="white")
C = Tkinter.Button(top, text ="Mine Tweets",command = test2,height=10,width=20,background="white",fg="black",activebackground="black",activeforeground="white")
D = Tkinter.Button(top, text ="Lang. Graph analysis",command=test3,height=10,width=20,background="black",fg="white",)
E = Tkinter.Button(top, text ="Display text and lang", command=test4, height=10,width=20,background="white",fg="black",activebackground="black",activeforeground="white")

B.pack()
C.pack()
D.pack()
E.pack()
top.config(menu=menubar)

top.mainloop() 	