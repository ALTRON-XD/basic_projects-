# This program converts a given number of days into years, months, and days.

n = int(input("Enter number of days: ")) # Input number of days

years = n // 365 # floor division to get full years
months = (n % 365) // 30 # remaining days after extracting full years, divided by 30 to get full months
days = (n % 365) % 30 # remaining days after extracting full months

print(f"{n} days is approximately {years} years, {months} months, and {days} days.") #output the result
