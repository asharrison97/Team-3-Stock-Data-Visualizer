# importing functions from other files
from APIConnector import get_api_connection
from Date_Selection import get_date_range
from chart_type import get_chart_type
from enter_symbol import get_stock_symbol
from time_series import get_time_series

def main():
    stock_symbol = get_stock_symbol()
    chart_type = get_chart_type()
    time_series = get_time_series()
    if(time_series == "TIME_SERIES_INTRADAY"):
        interval = int(input("\nEnter an appropriate time interval for the INTRADAY function."))
    else:
        interval = None
    date_range = get_date_range()
    get_api_connection(time_series, stock_symbol, interval)
main()