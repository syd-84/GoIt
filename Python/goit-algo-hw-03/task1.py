from datetime import datetime

def get_days_from_today(date):
  today=datetime.today().date()
  target_day=datetime.strptime(date, "%Y-%m-%d").date()
  res=(target_day-today).days
  return res

print(get_days_from_today("2027-10-09"))