import requests


class CatFactService:
    CAT_API_URL = "https://catfact.ninja/fact"

    @staticmethod
    def get_cat_fact():
        try:
            response = requests.get(CatFactService.CAT_API_URL)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            cat_fact_data = response.json()
            return cat_fact_data.get("fact")
        except requests.RequestException as e:
            print(f"Error fetching cat fact: {e}")
            return None
