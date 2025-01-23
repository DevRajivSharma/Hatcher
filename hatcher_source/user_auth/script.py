from datetime import datetime
date = "2003-01-12"
print(date)
try:
    date = datetime.strptime(date, '%Y-%m-%d').date()
except ValueError:
    # Handle the case where the date format is incorrect
    print(ValueError)
print(date)