def get_stock_symbol():
    stock_symbol = ""

    # display title
    print()
    print("Stock Data Visualizer")
    print("---------------------")
    print()

    # enter stock symbol
    while(stock_symbol == ""):
        #prompt for input
        symbol_input = input("Enter Stock Symbol: ")
        return symbol_input

