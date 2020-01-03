# Problem :
# We add a Leap Day on February 29, almost every four years. The leap day is an extra, or intercalary day and we add it to the shortest month of the year, February.
# In the Gregorian calendar three criteria must be taken into account #to identify leap years:

# case1: The year can be evenly divided by 4, is a leap year, unless:
# case2: The year can be evenly divided by 100, it is NOT a leap year, unless:
# case3: The year is also evenly divisible by 400. Then it is a leap year.


def is_leap(year):
    leap = False

    # Write your logic here
    if year % 4 == 0:  # case1
        leap = True
        if year % 100 == 0:  # case2
            leap = False
        if year % 400 == 0:  # case3
            leap = True
    return leap


year = int(input())
print(is_leap(year))
