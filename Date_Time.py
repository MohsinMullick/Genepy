from datetime import datetime
# Get the current date and time
now = datetime.now()
# Format the date as YYYY-MM-DD (month and day zero-padded automatically)
date_str = now.strftime("%Y-%m-%d")
# Format the time as HH:MM:SS (hour zero-padded automatically)
time_str = now.strftime("%H:%M:%S")
# Print in the exact required format
print(f"Today is {date_str} and it is {time_str}.")