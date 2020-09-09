def city_names(city, country):
    """Return neatly formated City, Country"""
    place = f"{city}, {country}"
    return place.title()

current_local = city_names('minsk', 'belarus')
print(current_local)

next_location = city_names('kyiv', 'ukraine')
print(f"\n{next_location}")

final_destination = city_names('gaborone', 'bostwana')
print(f"\n{final_destination.upper()}")
