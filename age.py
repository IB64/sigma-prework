from datetime import date

dates=[]
choice = input("Please input a date in this format dd-mm-yyyy:\n")
for item in choice.split("-"):
    dates.append(int(item))
past_date = date(dates[2], dates[1], dates[0])

print((date.today() - past_date).days//365)