import json

indian_cities_data = '''
{
  "cities": [
    {
      "name": "Mumbai",
      "population": 12478447,
      "state": "Maharashtra",
      "coordinates": {
        "latitude": 19.0760,
        "longitude": 72.8777
      }
    },
    {
      "name": "Delhi",
      "population": 11007835,
      "state": "Delhi",
      "coordinates": {
        "latitude": 28.7041,
        "longitude": 77.1025
      }
    },
    {
      "name": "Bangalore",
      "population": 8443675,
      "state": "Karnataka",
      "coordinates": {
        "latitude": 12.9716,
        "longitude": 77.5946
      },
      "budget": "100 Crore"
    }
  ]
}
'''

parsed_indian_cities_data = json.loads(indian_cities_data)

for city in parsed_indian_cities_data["cities"]:
    print("City:", city["name"])
    print("Population:", city["population"])
    print("State:", city["state"])
    print("Latitude:", city["coordinates"]["latitude"])
    print("Longitude:", city["coordinates"]["longitude"])
    if "budget" in city:
        print("Budget:", city["budget"])
    print()
