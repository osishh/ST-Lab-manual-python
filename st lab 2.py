def next_date(year, month, day):
    # Validate year
    if not (1 <= year <= 9999):
        raise ValueError("Invalid year")
    
    # Validate month
    if not (1 <= month <= 12):
        raise ValueError("Invalid month")
    
    # Validate day
    if not (1 <= day <= 31):
        raise ValueError("Invalid day")
    
    # Days in each month
    days_in_month = [31, 29 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Check if day is valid for the given month
    if day > days_in_month[month - 1]:
        raise ValueError("Invalid day for the given month")
    
    # Compute next date
    if day < days_in_month[month - 1]:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

# Test cases
print("Valid dates:")
print(next_date(2022, 6, 15)) # (2022, 6, 16)
print(next_date(2022, 6, 30)) # (2022, 7, 1)
print(next_date(2022, 12, 31)) # (2023, 1, 1)
print(next_date(2020, 2, 28)) # (2020, 2, 29)
print(next_date(2019, 2, 28)) # (2019, 3, 1)

print("\nInvalid dates:")
try:
    print(next_date(0, 6, 15)) # Error
except ValueError as e:
    print(e)

try:
    print(next_date(2022, 13, 15)) # Error
except ValueError as e:
    print(e)

try:
    print(next_date(2022, 6, 32)) # Error
except ValueError as e:
    print(e)
