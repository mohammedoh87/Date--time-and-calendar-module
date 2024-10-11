def hotel_cost(nights):
    return 140 * nights
def plane_cost(city):
    if city == "tampa":
        return 220
    elif city == "Los Angeles":
        return 475
def car_cost(days):
    if days >= 7:
        return 40 *days -50
    elif days >= 3:
        return 40 * days - 20
    else:
        return 40 * days
def trip_cost(city, days, spending_money):
    return hotel_cost(days) + plane_cost(city) + car_cost(days) + spending_money

print(trip_cost("tampa", 5, 600))
