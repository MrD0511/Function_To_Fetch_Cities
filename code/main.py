import requests

api_url = "https://countriesnow.space/api/v0.1/countries/cities"


def get_cities_and_store_as_csv(country: str):
    """It is a function that uses countriesnow API to fetch all the cities of India.
    After Fetching the cities it writes the cities in the cities.csv file.
    """
    body = {
        "country": country
    }

    try:
        cities_data = requests.post(api_url, json=body)
        cities = cities_data.json()['data']

        with open("cities.csv", "w", encoding="utf-8") as f:
            f.write("id,city\n")
            for index, city in enumerate(cities):
                f.write(f"{index},{city}\n")

        print("Successful, All the cities of India stored in the cities.csv.")
    except:
        print("Error: Error fetching data.")

    
get_cities_and_store_as_csv("india")