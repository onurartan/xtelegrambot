import json

def escape_markdown_v2(text):
    escape_chars = r"_[]()~>#+-=|{}.!"
    return ''.join(f"\\{char}" if char in escape_chars else char for char in text)

def get_country_by_code(code: str) -> dict:
    """
    Retrieve country information by its code from a JSON file.

    This function opens a JSON file containing a list of countries,
    each represented as a dictionary with fields for 'id', 'code',
    and 'value'. It searches through this list to find the country
    with the specified code and returns the corresponding country
    dictionary.

    Parameters:
    code (str): The ISO 3166-1 alpha-2 country code to search for.

    Returns:
    dict: A dictionary containing the 'id', 'code', and 'value' of the
          country, or None if no country with the specified code is found.
    """

    try:
        with open("app\countries.json", "r") as f:
            countries: list = json.load(f)["countries"]
        country = next(
            (country for country in countries if country["code"] == code), None
        )
        print(country)

        return country
    except FileExistsError:
        print("../countries.json file not found")
        return None
    except json.JSONDecodeError:
        print("Error decoding JSON.")
        return None


def get_countries() -> list:
    try:
        with open("app\countries.json", "r") as f:
            countries: list = json.load(f)["countries"]

        return countries
    except FileExistsError:
        print("../countries.json file not found")
        return None
    except json.JSONDecodeError:
        print("Error decoding JSON.")
        return None
