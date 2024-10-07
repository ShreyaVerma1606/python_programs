def calculate_age(birth_year, birth_month, birth_day):
    # Get the current date
    current_year = 2024
    current_month = 10
    current_day = 6

    # Calculate the age in years
    age_years = current_year - birth_year

    # Calculate the age in months
    age_months = current_month - birth_month
    if age_months < 0:
        age_years -= 1
        age_months += 12

    # Calculate the age in days
    age_days = current_day - birth_day
    if age_days < 0:
        # Adjust days and months
        if age_months == 0:
            age_years -= 1
            age_months = 11
        else:
            age_months -= 1
        # Assume 30 days in the previous month for simplicity
        age_days += 30  

    return age_years, age_months, age_days

# User input for birth date
birth_year = int(input("Enter your birth year (YYYY): "))
birth_month = int(input("Enter your birth month (1-12): "))
birth_day = int(input("Enter your birth day (1-31): "))

age_years, age_months, age_days = calculate_age(birth_year, birth_month, birth_day)
print(f"You are {age_years} years, {age_months} months, and {age_days} days old.")