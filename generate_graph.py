#Function to create a pygal bar or line chart, based on the user's input.
from flask import Flask, render_template, request, flash, url_for
import pygal

#create a Flask object
app = Flask(__name__)

def create_chart(data, start_date, end_date, chart_input, symbol_input, intraday_interval):
    open = []
    high = []
    low = []
    close = []

    for files in data:
        open.append(files["open"])
        high.append(files["high"])
        low.append(files["low"])
        close.append(files["close"])

    if chart_input == "1":
        #Bar chart components:
        bar_chart = pygal.Bar()
        chart_title = f"Stock Data for {symbol_input}: {start_date} to {end_date}"
        bar_chart.title = chart_title
        bar_chart.x_labels = map(intraday_interval, range(start_date, end_date))
        bar_chart.add("Open", open)
        bar_chart.add("High", high)
        bar_chart.add("Low", low)
        bar_chart.add("Close", close)
    
        bar_chart.render_to_file('static/chart.svg')

    elif chart_input == "2":
        #Line chart components:
        line_chart = pygal.Line()
        chart_title = f"Stock Data for {symbol_input}: {start_date} to {end_date}"
        line_chart.title = chart_title
        line_chart.x_labels = map(intraday_interval, range(start_date, end_date))
        line_chart.add("Open", open)
        line_chart.add("High", high)
        line_chart.add("Low", low)
        line_chart.add("Close", close)
    
        line_chart.render_to_file('static/chart.svg')

#route/view to display query results submitted from the user's input
@app.route("/results", methods=['POST'])
def results():
    from enter_symbol import get_stock_symbol
    from APIConnector import get_api_connection
    from time_series import get_time_series
    from intraday_interval import get_intraday_interval
    from start_date import get_start_date
    from end_date import get_end_date
    from chart_type import get_chart_type

    symbol = get_stock_symbol()
    api_connector = get_api_connection(get_time_series(), symbol, get_intraday_interval())

    #assign result variable a default value
    query_result = None

    #python dictionary for query parameters
    query = {}

    query["Symbol"] = symbol
    query_result = list(api_connector.find(query))
    chart = create_chart(query_result, get_start_date(), get_end_date(), get_chart_type(), get_stock_symbol(), get_intraday_interval())

    #send the results to the results.html template
    return render_template("results.html", query_result=query_result, chart=chart)
