import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier 
phone_number1 = phonenumbers.parse("+919865783846")
print(phone_number1)
print(geocoder.description_for_number(phone_number1,'en'))
print(carrier.name_for_number(phone_number1,'en')) 
phone_number2 = phonenumbers.parse("+917294536271")
print(geocoder.description_for_number(phone_number2,'en'))

