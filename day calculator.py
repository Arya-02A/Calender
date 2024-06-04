
date = int(input('Enter Date : '))
month = int(input('Enter Month Number : '))
year = int(input('Enter Last Two Digits Of The Year : '))
century = int(input('Enter First 2 Digits Of The Century : '))

leapcode = year//4

if month==1:
    monthcode = 1
elif month==2:
    monthcode = 4
elif month==3:
    monthcode = 4
elif month==4:
    monthcode = 0
elif month==5:
    monthcode = 2
elif month==6:
    monthcode = 5
elif month==7:
    monthcode = 0
elif month==8:
    monthcode = 3
elif month==9:
    monthcode = 6
elif month==10:
    monthcode = 1
elif month==11:
    monthcode = 4
elif month==12:
    monthcode = 6

if century % 4 == 0:
    centurycode = 6
elif century % 4 == 1:
    centurycode = 4
elif century % 4 == 2:
    centurycode = 2
elif century % 4 == 3:
    centurycode = 0

day = (date + year + leapcode + monthcode + (centurycode - 1)) % 7

if day == 1:
    print('The Day Is Monday')
elif day == 2:
    print('The Day Is Tuesday')
elif day == 3:
    print('The Day Is Wednesday')
elif day == 4:
    print('The Day Is Thursday')
elif day == 5:
    print('The Day Is friday')
elif day == 6:
    print('The Day Is Saturday')
elif day == 0:
    print('The Day Is Sunday')