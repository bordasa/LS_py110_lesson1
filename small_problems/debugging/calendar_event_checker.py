events = {
    "2023-08-13": ["Python debugging exercises"],
    "2023-08-14": ["Read 'Automate the Boring Stuff'"],
    "2023-08-15": ["Webinar: Python for Data Science"],
}

def is_date_available(date):
    if date in events:
        return False

    return True

print(is_date_available("2023-08-14"))  # should return False
print(is_date_available("2023-08-16"))  # should return True

'''
Explaining what the code was doing.
In the original code, the function was checking to see if the date is in
the calendar. If the date is in the calendar, it was returning True.
If the date was not already in the calendar, it was returning False.
For a function called "is_date_available(date):"this is the opposite logic
from what is needed. If we reverse the logic, either in the conditional or
in the return statements, then the function will work as expected.
'''