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
#This function gets date range and makes sure end date doesn't come before start date
def get_date_range():
    while True:
        start_date = get_valid_date("Enter the beginning date (YYYY-MM-DD): ")
        end_date = get_valid_date("Enter the end date (YYYY-MM-DD): ")

        if end_date >= start_date:
            return start_date, end_date
        else:
            print("End date cannot be before the start date. Please try again.")

if __name__ == "__main__":
    start_date, end_date = get_date_range()
    print(f"Selected date range: {start_date} to {end_date}")
