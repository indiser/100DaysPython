temps_in_celsius={
    "Monday":12,
    "Tuesday":14,
    "Wednesday":15,
    "Thursday":14,
    "Friday":21,
    "Saturday":22,
    "Sunday":24
}


temp_in_farhehite={day:((c*1.8)+32) for (day,c) in temps_in_celsius.items()}
print(temp_in_farhehite)