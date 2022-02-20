from numbers import Rational


option = int(input('Enter your option: '))
total = int(input('Enter your total: '))

def get_options_ratio(option, total):
    return option / total

ratio = get_options_ratio(option, total)

def get_faculty_rating(ratio):
    if ratio < 1 and ratio >= .9:
        print ('Excellent')
    else:
        if ratio > .8:
            print ('Very Good')
        else:
            if ratio > .7:
                print ('Good')
            else:
                if ratio > .6:
                    print ('Needs Improvement')
                else:
                    if ratio < .59 and num > 0:
                        print ('Unacceptable')

finalOutput = get_faculty_rating(ratio)