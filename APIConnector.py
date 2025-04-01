import requests;

# this function will accept a function type and stock symbol in order to create a valid API request
def get_api_connection(type, symbol, interval):
    functionType = type
    stockSymbol = symbol
    stockInterval = interval
    print(functionType)
    # check if the user requested an intraday type, which requires the use of the interval parameter
    if(functionType == "TIME_SERIES_INTRADAY"):
        url = ("https://www.alphavantage.co/query?function=%s&symbol=%s&interval=%s&apikey=RZ44H0Q12VLLXK96" % (functionType, stockSymbol, stockInterval))
    else:
        url = ("https://www.alphavantage.co/query?function=%s&symbol=%s&apikey=RZ44H0Q12VLLXK96" % (functionType, stockSymbol))
    # we are using the url constructed to execute a request
    r = requests.get(url)
    data = r.json()
    # we are making sure that the status code is 200, which indicates a successful query
    if(r.status_code is 200):
        return data
    else:
        print("A fatal error has occurred!")
        return

