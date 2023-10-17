# Which year do you want to check?
# year = int(input())


# 🚨 Don't change the code above 👆

# Write your code below this line 👇
def is_leap_year(year_to_check):
    if year_to_check % 4 != 0:
        return "Not leap year"
    if year_to_check % 100 == 0 and year_to_check % 400 != 0:
        return "Not leap year"
    return "Leap year"


print(is_leap_year(1989))
