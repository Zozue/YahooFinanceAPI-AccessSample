import json
import pprint
import http.client

conn = http.client.HTTPSConnection("apidojo-yahoo-finance-v1.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
    'x-rapidapi-key': "ead654d653mshb2f6685579090aap13ceeajsn2582512b8e79"
    }

conn.request("GET", "/market/get-spark?interval=1m&range=1d&symbols=AMZN%252CAAPL%252CWDC%252CREYN%252CAZN%252CYM%253DF", headers=headers)

res = conn.getresponse()
data = res.read()

pprint.pprint(json.loads(data.decode("utf-8")))