import requests

def get_data_from_api():
    api_url = "https://api.example.com/data" # Not Acual
    api_key = "my_public_api_key" # Not Actual

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

data = get_data_from_api()
if data:
    print(data)
