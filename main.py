import phonenumbers
from text import number

from phonenumbers import geocoder

ch_nmber = phonenumbers.parse(number)
print(geocoder.description_for_number(ch_nmber, "en"))

from phonenumbers import carrier
service_nmber = phonenumbers.parse(number)
print(carrier.name_for_number(service_nmber, "en"))