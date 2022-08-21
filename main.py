from GoogleNews import GoogleNews
from datetime import datetime, timedelta
from pytz import timezone
import pandas as pd

#GET A PERIOD OF TIME
est = timezone('EST')
today = datetime.now(est)
yesterday = today - timedelta(days=1)

print("Today's date:", today)
print("Yesterday's  date:", yesterday)

#SET THE DATE RANGE
googlenews=GoogleNews(start='08/09/2022',end=today.strftime("%m/%d/%Y"))
#SET THE LANGUAGE
googlenews.set_lang('en')
#SET THE TOPIC
googlenews.search('Science')
#Get links
googlenews.get_links()
a = googlenews.get_links()
#get total
googlenews.total_count()
#GET THE NEWS
result=googlenews.result()
#CONVERT THE RESULT TO A PANDAS DATAFRAME
df=pd.DataFrame(result)

# print(df)
# print(len(a))
print()
# googlenews = GoogleNews(start='02/01/2020',end='02/28/2020')

# print(result)