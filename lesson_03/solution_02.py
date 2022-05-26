dev = 2130

bonus=120

percent = 0.1

first_year=dev+dev*percent+bonus

second_year=first_year+first_year*percent+bonus
third_year=second_year+second_year*percent+bonus

fourth_year=third_year+third_year*percent+bonus

fifth_year=fourth_year+fourth_year*percent+bonus

print(fifth_year)
