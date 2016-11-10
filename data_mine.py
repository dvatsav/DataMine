import json
import pandas as pd
import matplotlib.pyplot as plt
import re
import tweepy



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

tweets["text"]=map(lambda tweet:tweet['text'],tweets_data)
tweets["lang"]=map(lambda tweet:tweet['lang'],tweets_data)

try:
	tweets_by_lang=tweets['lang'].value_counts()
except:
	pass
fig,ax=plt.subplots()
ax.tick_params(axis='x',labelsize=15)
ax.tick_params(axis='y',labelsize=10)
ax.set_xlabel('Countries',fontsize=15)
ax.set_ylabel('Number of Tweets',fontsize=15)
ax.set_title('Top 5 countries',fontsize=15,fontweight='bold')
tweets_by_lang[:5].plot(ax=ax,kind='bar',color='blue')
plt.show()


