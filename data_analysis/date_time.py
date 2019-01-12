from datetime import datetime
#the second argument tell Python to interpret first 4 digit before dash is year, next is month and third is date
first_date = datetime.strptime('2014-7-1', '%Y-%m-%d')
print(first_date)
