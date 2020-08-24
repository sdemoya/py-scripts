def cities(city, country="the United States"):
    print(f"{city.title()} is in {country.title()}.")

cities('Washington, D.C.')

cities('Rome', 'Italy')

cities(country='Iceland', city='Reykjavik')
