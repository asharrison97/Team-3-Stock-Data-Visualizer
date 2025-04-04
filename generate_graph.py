#Function to create a pygal bar or line chart, based on the user's input.
import pygal;
def create_chart(data, start_date, end_date, chart_input, symbol_input, intraday_interval):
    open = []
    high = []
    low = []
    close = []

    for files in data:
        open.append(files["1. open"])
        high.append(files["2. high"])
        low.append(files["3. low"])
        close.append(files["4. close"])

    if chart_input == "1":
        #Bar chart components:
        bar_chart = pygal.Bar()
        chart_title = f"Stock Data for {symbol_input}: {start_date} to {end_date}"
        bar_chart.title = chart_title
        bar_chart.x_labels = intraday_interval
        bar_chart.add("Open", open)
        bar_chart.add("High", high)
        bar_chart.add("Low", low)
        bar_chart.add("Close", close)
    
        bar_chart.render_in_browser()

    elif chart_input == "2":
        pass
