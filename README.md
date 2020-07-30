# YahooFinanceAPI-AccessSample
 Sample scripts to access various aspects of the Yahoo Finance 

The rapidapi Yahoo Finance API uses a REST interface. These can be accessed through a many different ways. From what I see, all of these are simply http GET requests.

From my previous experience, I would use the Google Chrome Postman extension or a curl command (see below) to test these.

```
curl -X GET -H "Content-Type: application/json" -H "x-rapidapi-host: apidojo-yahoo-finance-v1.p.rapidapi.com" -H "x-rapidapi-key: ead654d653mshb2f6685579090aap13ceeajsn2582512b8e79" https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-summary?region=CA&lang=en
```

All scripts used here use my personal RapidAPI access key liked to the free access tier allowing a quote of 500 queries/month.

The main python script examples are all in the python-examples folder and named after the endpoint. All python scripts are using ```import http.client``` to interface with the APi and all scripts are outputting in a JSON prettyPrint format for better legibility when run as below, with python3 on Ubuntu.
```python3 market-get-summary.py  | less``` 


All endpoints and parameters are shown below. Options params are italicized. 
| Endpoint | Description | Arg1 | Arg2 | Arg3 | Arg4 | Arg5 | Arg6 | Arg7 |
|---|---|---|---|---|---|---|---|---|
|```market/get-summary```| Get live summary information at the request time | region | lang | | | | | |
|```market/get-movers```| The live day gainers / losers / actives in specific region | region | lang | *start* | *count* | | | |
|```market/get-quotes```| The quotes by symbols | region | lang | symbols | | | | |
|```market/get-charts```| Get data to draw chart for a specific symbol and its comparisons | region | lang | symbol | interval | range | *comparisons* | |
|```market/auto-complete```| Get auto complete suggestion for stocks | region | lang | query | | | | |
|```market/get-spark```| Used with …/market/get-trending-tickers endpoint together to draw brief chart. | symbols | *interval* | *range* | | | |
|```market/get-earnings```| Get recent earnings in the market | region | startDate | endDate | *size* | | | |
|```market/get-trending-tickers```| Get latest trending tickers in the market | region | | | | | | |
|```market/get-popular-watchlists```| Get popular watchlists in the market | | | | | | | |
|---|---|---|---|---|---|---|---|---|
|```stock/get-news```| Get latest news related to a symbol, the result may be empty if there is no news in that region | region | category | | | | | |
|```stock/v2/get-holders```| Get holders tab information | symbol | | | | | | |
|```stock/v2/get-financials```| Get financials tab information | symbol | | | | | | |
|```stock/v2/get-options```| Get options tab information | symbol | date | *straddle* | | | | |
|```stock/v2/get-analysis```| Get analysis tab information | symbol | | | | | | |
|```stock/v2/get-insights```| Get brief reports relating to a symbol | symbol | | | | | | |
|```stock/v2/get-historical-data```| Get historical data tab information | period1 | period2 | symbol | *frequency* | *filter* | | |
|```stock/v2/get-statistics```| Get statistics tab information | *region | symbol* | | | | | |
|```stock/v2/get-chart```| Get data to draw full screen chart | interval | region | symbol | lang | range | *period1* | *period2* | |
|```stock/v2/get-timeseries```| Get financial data quarterly for more detail | symbol | period1 | period2 | *region* | *lang* | | |
|```stock/v2/get-summary```| Get summary tab information | region | symbol | | | | | |
|```stock/v2/get-balance-sheet```| Get data in Balance Sheet tab | *symbol* | | | | | | |
|```stock/v2/get-profile```| Get profile tab information | *symbol* | | | | | | |
|---|---|---|---|---|---|---|---|---|
|```news/get-details```| Read the specific news in details | uuid | | | | | | |
|```news/list```| List latest general news or video feeds or news relating to a symbol, the result may be empty if there is no news in that region | region | category | *start_uuid* | | | | |
|---|---|---|---|---|---|---|---|---|
|```conversations/list```| List conversations relating to a symbol | region | symbol | messageBoardId | *userActivity* | *sortBy | *off* | |


References:
https://rapidapi.com/apidojo/api/yahoo-finance1\
man curl