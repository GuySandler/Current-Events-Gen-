##########################################################
#this is the code explained and without the testing parts#
##########################################################

from pygooglenews import GoogleNews #imports the api
from datetime import datetime, timedelta #datetime (unused for now)
from pytz import timezone #timezones (unused for now)
import random #random for giving you a random article

#Get Time of today
PST = timezone('EST')
today = datetime.now(PST)

#search
gn = GoogleNews() #shorter name
news = gn.topic_headlines("science") #searches for articles with the topic of science

entries = news["entries"]

#counter and list veriables
count = 0
Results = []

#makes the final part
for entry in news["entries"]:
        if count > 50:
                # one less then the last
                break
        count = count + 1

        # print(str(count) + ". " + "title: " + entry["title"] + "link: " + entry["link"])
        Results.append(str(count) + ". " + "title: " + entry["title"] + "link: " + entry["link"])
        

#randomize
num = random.randint(0, len(Results))

#give you the Result
print(Results[num])
