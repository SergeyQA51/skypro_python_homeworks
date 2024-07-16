from address import Address
from mailing import Mailing

to_address = Address("123456", "Murmansk", "Five corners Street", "11", "12")
from_address = Address("654321", "Saint Petersburg", "Sennaya Street", "4", "54")

mail = Mailing(to_address, from_address, 123500, "4567fdvd5335")

print(f"Отправление {mail.track} из {from_address.index}, {from_address.city}, {from_address.street}, {from_address.house} - {from_address.apartment} в {to_address.index}, {to_address.city}, {to_address.street}, {to_address.house} - {to_address.apartment}. Стоимость {mail.cost} рублей.")