import json
import pandas as pd
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


from Tkinter import *

def onclick():
   pass

root = Tk()
text = Text(root)
text.insert(INSERT, tweets["text"])
text.insert(END, "END")
text.pack()
root.mainloop()