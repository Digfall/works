import requests
import json


def get_homeworld(homeworld_url):
    response = requests.get(homeworld_url)
    homeworld_data = response.json()
    return homeworld_data


def main():
    url = "https://swapi.dev/api/starships/10/"
    response = requests.get(url)
    data = response.json()

    pilots_info = []
    for pilot_url in data['pilots']:
        pilot_response = requests.get(pilot_url)
        pilot_data = pilot_response.json()
        homeworld_info = get_homeworld(pilot_data['homeworld'])
        pilot_info = {
            "name": pilot_data["name"],
            "height": pilot_data["height"],
            "mass": pilot_data["mass"],
            "homeworld": homeworld_info["name"],
            "homeworld_url": pilot_data["homeworld"]
        }
        pilots_info.append(pilot_info)

    ship_info = {
        "name": data["name"],
        "max_atmosphering_speed": data["max_atmosphering_speed"],
        "ship_class": data["starship_class"],
        "pilots": pilots_info
    }

    print(json.dumps(ship_info, indent=2))

    with open("millennium_falcon_info.json", "w") as file:
        json.dump(ship_info, file, indent=2)


if __name__ == "__main__":
    main()