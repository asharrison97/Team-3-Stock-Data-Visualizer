stock_symbol = ""
chart_type = 0

# display title
print()
print("Stock Data Visualizer")
print("---------------------")
print()

# enter stock symbol
#while(stock_symbol == None):
    #prompt for input
symbol_input = input("Enter Stock Symbol: ")
    #validate symbol
        #if symbol found in database:
            #stock_symbol = symbol_input
        # if not found
            #display "Please enter a valid stock symbol"
            #continue



# enter chart type
print("\nChart Types")
print("-----------")
print("1. Bar \n2. Line")
while(chart_type == 0):
        #prompt for chart type
    chart_input = input("\nEnter the chart type you want (1,2): ")
        #validate input
    if (chart_input == "1"):
        chart_type = 1
        print("bar graph")
    elif (chart_input == "2"):
        chart_type = 2
        print("line graph")
    else:
        print("Please select a valid option.")