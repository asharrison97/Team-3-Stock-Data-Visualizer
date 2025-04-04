from datetime import datetime
#This function asks user for valid date 
def get_valid_date(prompt):
    while True:
        date_str = input(prompt)
        try:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d")
            return date_obj.strftime("%Y-%m-%d")  # Return as a string
        except ValueError:
            print("Invalid format. Please enter the date in YYYY-MM-DD format.")

#if __name__ == "__main__":
#    start_date, end_date = get_date_range()
#    print(f"Selected date range: {start_date} to {end_date}")
