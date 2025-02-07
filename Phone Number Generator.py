#create a function to generate a phone number, with country code, area code, first four digits
#and last four digits

country = input("Enter your country code: ")
area = input("Enter your area code: ")
first = input("Enter your phone number's first four digits: ")
last = input("Enter your phone number's last four digits: ")

def number(country, area, first, last):
    print(f"+{country} ({area}) {first}-{last}")
    
number(country=country, area=area, first=first, last=last)
