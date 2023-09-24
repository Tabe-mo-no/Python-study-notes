# test
def get_city_details(city, country, population = ''):
    if population:
        city_details = city + ', ' + population + ', ' + country
    else:
        city_details = city + ', ' + country
    return city_details.title()


