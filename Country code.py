country_codes = {
    'India': '0091',
    'Australia': '0025',
    'Nepal': '00977'
}

def get_country_code(country):
    return country_codes.get(country, "Country not found")
countries_to_check = ['India', 'Australia', 'Nepal', 'USA']

for country in countries_to_check:
    code = get_country_code(country)
    print(f"The country code for {country} is: {code}")
