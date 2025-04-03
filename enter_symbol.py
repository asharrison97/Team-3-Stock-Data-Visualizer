def get_stock_symbol():
    stock_symbol = ""

    # display title
    print()
    print("Stock Data Visualizer")
    print("---------------------")
    print()

    # enter stock symbol
    while(stock_symbol == None):
        #prompt for input
        symbol_input = input("Enter Stock Symbol: ")
        #validate symbol
            # try api request with provided symbol:
                #return validated sybmol
            # catch
                #display "Please enter a valid stock symbol"
                #continue

