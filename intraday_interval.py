def get_intraday_interval():
    print("\nSelect the time interval of the chart you want to generate")
    print("-----------")
    print("1. 1min \n2. 5min \n3. 15min\n 4. 30min\n 5. 60min\n")
    # loops until the user enters a valid choice, with an error catch incase a random unexpected value is entered
    while True:
        try:
            user_choice = int(input("\nEnter time series option (1, 2, 3, 4):"))
            if user_choice == 1:
                time_series = "1min"
                return time_series
            elif user_choice == 2:
                time_series = "5min"
                return time_series
            elif user_choice == 3:
                time_series = "15min"
                return time_series
            elif user_choice == 4:
                time_series = "30min"
                return time_series
            elif user_choice == 5:
                time_series = "60min"
                return time_series
            else:
                print("A valid option must be selected!")
        except ValueError as exc:
            print("Fatal Error: Invalid input!")
            return