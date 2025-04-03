def get_chart_type():
    chart_type = 0
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