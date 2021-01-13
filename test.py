from datetime import date

init_date = date(2020, 1, 5)
today = date.today()

alexa_age = today - init_date
lat = alexa_age.days // 365
print(lat)
