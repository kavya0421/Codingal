import datetime

print("==============================")
print("DATE AND TIME OPERATIONS")
print("==============================")

now = datetime.datetime.now()

print("Current Date and Time:", now)
print("Current Date:", now.date())
print("Current Time:", now.time())
print("Day:", now.day)
print("Month:", now.month)
print("Year:", now.year)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)
print("Formatted Date:", now.strftime("%d-%m-%Y"))
print("Formatted Time:", now.strftime("%I:%M:%S %p"))
