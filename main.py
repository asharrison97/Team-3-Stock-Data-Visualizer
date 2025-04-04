# importing functions from other files
from APIConnector import get_api_connection
from start_date import get_start_date
from end_date import get_end_date
from chart_type import get_chart_type
from enter_symbol import get_stock_symbol
from time_series import get_time_series
from intraday_interval import get_intraday_interval
#from generate_graph import create_chart

def main():
    stock_symbol = get_stock_symbol()
    chart_type = get_chart_type()
    time_series = get_time_series()
    if(time_series == "TIME_SERIES_INTRADAY"):
        interval = get_intraday_interval()
    else:
        interval = None
    start_date = get_start_date()
    end_date = get_end_date(start_date)
    data = get_api_connection(time_series, stock_symbol, interval)
    #create_chart(data, start_date, end_date, chart_type, stock_symbol, interval)
main()