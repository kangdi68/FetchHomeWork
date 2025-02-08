import argparse
import requests
import re

def get_information_by_using_place_name(city, state):
    print("check with placement name= ", city, state)
    location_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},US&appid=f897a99d971b5eef57be6fafa0d83239"
    data = api_call(location_url)
    return data


def get_information_by_using_zip_code(zip_code):
    print("check with zip code=", zip_code)
    zip_url = f"http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},US&appid=f897a99d971b5eef57be6fafa0d83239"
    data = api_call(zip_url)
    return data

def api_call(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error:{response.status_code}")
        return None

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--locations', nargs='+', default=False, help='“Madison, WI” “12345”')
    args = parser.parse_args()
    input_data = args.locations
    search_place = re.compile("([A-Za-z\\s]+),\\s*([A-Z]{2})")
    search_zip = re.compile("(^\\d{5}$)")
    for i in range(0, len(input_data)):
        place = search_place.search(input_data[i])
        zip_code = search_zip.search(input_data[i])
        if place is not None and len(place.groups()) == 2:
            data=get_information_by_using_place_name(place.group(1).strip(), place.group(2).strip())
            latitude = data[0]['lat']
            longitude = data[0]['lon']
            place_name = f'{data[0]['name']}, {data[0]['state']} {data[0]['country']}'
            local_name = data[0]['local_names']['ko']
            print(place_name, ":")
            print("latitude={}, longitude={}, local_name={}".format(latitude, longitude, local_name))
        elif zip_code is not None and len(zip_code.groups()) == 1:
            data=get_information_by_using_zip_code(zip_code.group(1))
            latitude = data['lat']
            longitude = data['lon']
            place_name = f'{data['name']}, {data['country']} {data['zip']}'
            print(place_name, ":")
            print("latitude={}, longitude={}".format(latitude, longitude))
        else:
            print(f"Failed: {input_data[i]} is not valid input")
            break
