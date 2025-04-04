#Function to create a pygal bar or line chart, based on the user's input.
import pygal
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
    
        bar_chart.render_in_browser()

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
    
        line_chart.render_in_browser()
