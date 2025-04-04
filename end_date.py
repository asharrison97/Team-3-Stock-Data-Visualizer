from get_valid_date import get_valid_date

# This function will return the end date input by the user
def get_end_date(start_date):
    while True:
        end_date = get_valid_date("Enter the end date (YYYY-MM-DD): ")

        if end_date >= start_date:
            return end_date
        else:
            print("End date cannot be before the start date. Please try again.")