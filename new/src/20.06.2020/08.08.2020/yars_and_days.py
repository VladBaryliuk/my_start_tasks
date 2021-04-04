import datetime
today = datetime.datetime.today()
birthday = datetime.datetime(int(input("enter birthday year")), int(input("enter birthday month")),
                                                                   int(input("enter birthday day")))
days = today - birthday
print(days.days)