from address import Address
from mailing import Mailing

from_address = Address( "123456", "Саратов", "Рахова", "10", "154")
to_address = Address( "987654", "Самара", "Зеленая", "12", "7")

mailing = Mailing( to_address=to_address, from_address=from_address, cost=350.50, track="AB123456789RU")

print(
    f"Отправление {mailing.track} из {mailing.from_address.index}, "
    f"{mailing.from_address.city}, {mailing.from_address.street}, "
    f"{mailing.from_address.house} - {mailing.from_address.apartment} в "
    f"{mailing.to_address.index}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.house} - "
    f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей."
    )


