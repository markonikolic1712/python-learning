def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name("AnGEla", "YU"))


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        else:
            return True
    return False


print(f"is_leap_year(1700): {is_leap_year(1700)}") # False
print(f"is_leap_year(1989): {is_leap_year(1989)}") # False
print(f"is_leap_year(1900): {is_leap_year(1900)}") # False
print("------------------------------")
print(f"is_leap_year(2000): {is_leap_year(2000)}") # True
print(f"is_leap_year(2020): {is_leap_year(2020)}") # True
print(f"is_leap_year(2024): {is_leap_year(2024)}") # True
print(f"is_leap_year(2028): {is_leap_year(2028)}") # True
