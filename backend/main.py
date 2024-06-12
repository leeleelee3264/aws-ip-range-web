import requests
import json

NEW_IP_RANGE_FILE = 'ip-ranges.json'
OLD_IP_RANGE_FILE = 'old-ip-ranges.json'

FETCH_URL = 'https://ip-ranges.amazonaws.com/ip-ranges.json'


def move_to_old_ip_range(source_file, destination_file):
    try:
        with open(source_file, 'r') as file:
            data = file.read()
    except FileNotFoundError:
        data = 'File not found this time. Creating dummy old ip range file...'

    with open(destination_file, 'w') as file:
        file.write(data)


def fetch_new_ip_range() -> None:
    try:
        response = requests.get(FETCH_URL)
        data = response.json()
    except requests.exceptions.RequestException as e:
        data = 'Failed to fetch new ip range. Creating dummy new ip range file...'

    with open(NEW_IP_RANGE_FILE, 'w') as file:
        json.dump(data, file)


def read_ip_range(filename) -> str:
    with open(filename, 'r') as file:
        data = file.read()
    return data


def is_the_same_ip_range(old_file, new_file) -> bool:
    old_ip = read_ip_range(old_file)
    new_ip = read_ip_range(new_file)

    return old_ip == new_ip


# init
move_to_old_ip_range(NEW_IP_RANGE_FILE, OLD_IP_RANGE_FILE)
fetch_new_ip_range()

# compare to check if the ip ranges are updated.
t = is_the_same_ip_range(NEW_IP_RANGE_FILE, OLD_IP_RANGE_FILE)
print(t)
