def get_time_series():
    time_series = ""
    # enter a valid time series type
    print("\nSelect the Time Series of the chart you want to generate")
    print("-----------")
    print("1. Intraday \n2. Daily \n3. Weekly\n 4. Monthly")
    # loops until the user enters a valid choice, with an error catch incase a random unexpected value is entered
    while True:
        try:
            user_choice = int(input("\nEnter time series option (1, 2, 3, 4):"))
            if user_choice == 1:
                time_series = "TIME_SERIES_INTRADAY"
                return time_series
            elif user_choice == 2:
                time_series = "TIME_SERIES_DAILY"
                return time_series
            elif user_choice == 3:
                time_series = "TIME_SERIES_WEEKLY"
                return time_series
            elif user_choice == 4:
                time_series = "TIME_SERIES_MONTHLY"
                return time_series
            else:
                print("A valid option must be selected!")
        except ValueError as exc:
            print("Fatal Error: Invalid input!")
            return