# Problem 19

# You are given the following information, but you may prefer to do some research for yourself.
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

leap = []

for i in range(1901,2001):
    if i % 100 == 0:
        if i % 400 == 0:
            leap.append(i)
    elif i % 4 == 0:
        leap.append(i)

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap_months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
days.reverse()

def next_month(start, month, year):
    if year in leap:
        number_of_days = leap_months[month-1]
    else:
        number_of_days = months[month-1]
    index_day = days.index(start)
    extra_days = number_of_days % 7
    new_day = days[index_day - extra_days]
    return new_day

def next_year(start, year):
    if year in leap:
        number_of_days = 366
    else:
        number_of_days = 365
    index_day = days.index(start)
    extra_days = number_of_days % 7
    new_day = days[index_day - extra_days]
    return new_day

def sundays_in_year(first_day_of_year, year):
    first = first_day_of_year
    sundays = 0
    if first == "sunday":
        sundays += 1
    for i in range(1,12):
        first = next_month(first, i, year)
        if first == "sunday":
            sundays += 1
    return sundays

start_days = [["monday", 1900]]

for i in range(1900,2000):
    a = next_year(start_days[-1][0], i)
    start_days.append([a, (i+1)])

start_days = start_days[1:]

count = 0
for i in range(len(start_days)):
    count += sundays_in_year(start_days[i][0], start_days[i][1])
count
