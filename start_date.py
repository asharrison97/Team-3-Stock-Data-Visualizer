from get_valid_date import get_valid_date

# This function will return the start date input by the user
def get_start_date():
    while True:
        start_date = get_valid_date("Enter the beginning date (YYYY-MM-DD): ")
        return start_date