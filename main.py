import matplotlib.pyplot as plt
import seaborn as sns; sns.set() #Importing Libraries for Data Processing and Displaying
want = str(input("Pick stock Initials "))
start_date = '1960-4-1'  #Retrieving data from user
end_date = '2023-4-23'



import yfinance as yf  #Importing Stock Database / Scraping Libraries
import seaborn as sns; sns.set()
import requests

start_date = '2023-4-17'
end_date = '2023-4-21'

M = yf.download(tickers = want, #Setting search
                  start = start_date,
                  end = end_date)

M.head()
M.reset_index(inplace=True) #Organized and Retrieving data
M.head()
time_series = list(M['Open'])
print(M)

my_api_key = "api_key" #API KEY/CSE_ID for Google Search API
my_cse_id = "cse_id"
negp=0 #Point Calculation for prediction based off keyword
posp=0
headlines = ["","","","","","","","","","",""] #Initalizing Headline
ic = 0
closep = yf.download(tickers=want, start=start_date, end=start_date) #Giving Closing Stock Data from yfinance library
query = want
page = 1



start = (page - 1) * 100 + 75
url = f"https://www.googleapis.com/customsearch/v1?key={my_api_key}&cx={my_cse_id}&q={query}&start={start}"
data = requests.get(url).json() #Observing and Representing Data collected from Google API from ApiKey
search_items = data.get("items")
print(search_items)
try:
    for i, search_item in enumerate(search_items, start=1): #getting attributes of articles
        try:
            long_description = search_item["pagemap"]["metatags"][0]["og:description"]
        except KeyError:
            long_description = "N/A"
        # get the page title
        title = search_item.get("title")
        i=i+1
        snippet = search_item.get("snippet")
        print(title)

        #Searching for keywords
        if "crash" in title or "frustrate"in title or "blew"in title or "struggle"in title or "worse"in title or "problem"in title or "barely"in title or "drop"in title or "falling" in title or "fail"in title or "bad" in title or "lose" in title or "red" in title or "loss"in title or "miss"in title or "dip"in title or "soar"in title or "jump"in title or "jumped" in title or "concern" in title or "dip" in title:
            negp = negp+ 1

        if "thrive" in title or "beats" in title or "significant" in title or "rise" in title or "increase" in title or "creating" in title or "revolution"in title or "deal"in title or "relief"in title or "opportunity"in title or "great"in title or "progress"in title:
            posp = posp + 1

        if "thrive" in long_description or "beats" in long_description or "significant" in long_description or "rise" in long_description or "increase" in long_description or "creating" in long_description or "revolution" in long_description or "deal" in long_description or "relief" in long_description or "opportunity" in long_description or "great" in long_description or "progress" in long_description:
            posp = posp + 1

        if "crash" in long_description or "frustrate" in long_description or "blew" in long_description or "struggle" in long_description or "worse" in long_description or "problem" in long_description or "barely" in long_description or "drop" in long_description or "falling" in long_description or "fail" in long_description or "bad" in long_description or "lose" in long_description or "red" in long_description or "loss" in long_description or "miss" in long_description or "dip" in long_description or "soar" in long_description or "jump" in long_description or "jumped" in long_description or "concern" in long_description or "dip" in long_description:
            negp = negp + 1

        if "thrive" in snippet or "beats" in snippet or "significant" in snippet or "rise" in snippet or "increase" in snippet or "creating" in snippet or "revolution" in snippet or "deal" in snippet or "relief" in snippet or "opportunity" in snippet or "great" in snippet or "progress" in snippet:
            posp = posp + 1

        if "crash" in snippet or "frustrate" in snippet or "blew" in snippet or "struggle" in snippet or "worse" in snippet or "problem" in snippet or "barely" in snippet or "drop" in snippet or "falling" in snippet or "fail" in snippet or "bad" in snippet or "lose" in snippet or "red" in snippet or "loss" in snippet or "miss" in snippet or "dip" in snippet or "soar" in snippet or "jump" in snippet or "jumped" in snippet or "concern" in snippet or "dip" in snippet:
            negp = negp + 1

        headlines[i-1] = title
        html_snippet = search_item.get("htmlSnippet")
        link = search_item.get("link")
        print("="*10, f"Result #{i+start-1}", "="*10)
        print("Title:", title) #Reporting Data
        print("Description:", snippet)
        print("Long description:", long_description)
        print("URL:", link, "\n")

except KeyError:
    pass
net=0
if(posp>negp): #Prediction:
    net = (float(posp-negp)/2) #Calculation of Stock Market price increse
    print("Stock is going to increase by: ",net,"dollars")
else:
    net= (float(negp-posp)/2)
    print("Stock is going to decrease by about: ",net,"dollars")


plt.figure(figsize=(14,5)) # Setting up data graph and showing stock history
sns.set_style("ticks")
sns.lineplot(data=M,x="Date",y='Close',color='firebrick')
sns.despine()
plt.title("The Stock Price of "+want,size='x-large',color='blue')
plt.show()
