import requests;

# this function will accept a function type, stock symbol, and a time interval in order to create a valid API request
def get_api_connection(time_series, symbol, interval):
    functionTimeSeries = time_series
    stockSymbol = symbol
    timeInterval = interval
    # check if the user requested an intraday type, which requires the use of the interval parameter
    if(functionTimeSeries == "TIME_SERIES_INTRADAY"):
        url = ("https://www.alphavantage.co/query?function=%s&symbol=%s&interval=%s&datatype=csv&apikey=RZ44H0Q12VLLXK96" % (functionTimeSeries, stockSymbol, timeInterval))
    else:
        url = ("https://www.alphavantage.co/query?function=%s&symbol=%s&datatype=csv&apikey=RZ44H0Q12VLLXK96" % (functionTimeSeries, stockSymbol))
    # we are using the url constructed to execute a request
    r = requests.get(url)
    data = r.csv()
    # we are making sure that the status code is 200, which indicates a successful query
    if(r.status_code is 200):
        return data
    else:
        print("A fatal error has occurred!")
        return

