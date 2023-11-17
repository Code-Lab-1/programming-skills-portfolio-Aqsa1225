def describe_city(city, country='South Korea'):
    """Describe a city."""
    msg = city.title() + " is in " + country.title() + "."
    print(msg)

describe_city('seoul')
describe_city('reykjavik', 'iceland')
describe_city('busan')