
import datetime

name = input('Enter your name:')

hour = datetime.datetime.now().hour


def find_greeting(current_hour):
    match current_hour:
        case 21 | 22 | 23 | 1 | 2 | 3 | 4 | 5:
            greeting = "Good Night";
        case 6 | 7 | 8 | 9 | 10 | 11 | 12:
            greeting = "Good Morning";
        case 13 | 14 | 15:
            greeting = "Good Afternoon";
        case 16 | 17 | 18 | 19 | 20:
            greeting = "Good Evening";
    return greeting;



print(f'Hello {name}. ' + find_greeting(hour))
