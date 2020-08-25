def city_names(city, country):
    """Return neatly formated City, Country"""
    place = f"{city}, {country}"
    return place.title()

current_local = city_names('minsk', 'belarus')
print(current_local)


