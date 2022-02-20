import decisions

option = int(input('Enter your option: '))
total = int(input('Enter your total: '))

decisions.get_options_ratio(option, total)

result = decisions.get_options_ratio(option, total)

print(result)

decisions.get_faculty_rating(result)