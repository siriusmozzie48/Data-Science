# Start your code here!
import os
import pandas as pd
from openai import OpenAI

# Instantiate an API client
# If you named your environment variable differently 
# then change "OPENAI_API_KEY" to reflect the variable name
client = OpenAI(api_key=os.environ["OPENAI"])

nasdaq100 = pd.read_csv("nasdaq100.csv")
price_change = pd.read_csv("nasdaq100_price_change.csv")

# Merge to add the "ytd" column
nasdaq100 = pd.merge(
    nasdaq100,
    price_change[["symbol", "ytd"]],  # Select only symbol and ytd
    on="symbol",
    how="left"
)
sectors=[]
# Optional: Handle missing YTD values (e.g., set to 0)
nasdaq100["ytd"] = nasdaq100["ytd"].fillna(0)
for company in nasdaq100["symbol"]:
    response = client.chat.completions.create(model="gpt-4o-mini", messages =[{"role":"system", "content":"you are a stock market analyst analysing the nasdaq100"}, {"role":"user", "content":" classify the following stock into a sector with the following values :  Technology, Consumer Cyclical, Industrials, Utilities, Healthcare, Communication, Energy, Consumer Defensive, Real Estate, or Financial. Give a one word answer response naming the sector for the stock,  The stock is " + company}], temperature =0.0, max_tokens=100)
    sector = response.choices[0].message.content
    print(sector)
    sectors.append(sector)
    
nasdaq100["sector"] = sectors

print(nasdaq100[["symbol", "sector"]].head()) 

stock_recommendations = client.chat.completions.create(model="gpt-4o-mini", messages = [{"role":"user", "content":f"""provide summary information about Nasdaq-100 stock performance YTD, recommending the three best sectors and three or more companies per sector, here is the data : {nasdaq100[["symbol", "ytd", "sector"]]}"""}] )

print(stock_recommendations)
