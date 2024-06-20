import requests
import json

NEW_IP_RANGE_FILE = "resources/ipRanges.json"
OLD_IP_RANGE_FILE = "resources/oldIpRanges.json"

TOP_COMPONENT_FILE = "component/top.js"
BOTTOM_COMPONENT_FILE = "component/bottom.js"
BUNDDLE_JS_FILE = "../docs/bundle.js"

FETCH_URL = 'https://ip-ranges.amazonaws.com/ip-ranges.json'


def move_to_old_ip_range() -> None:
    try:
        with open(NEW_IP_RANGE_FILE, 'r') as file:
            data = file.read()
    except FileNotFoundError:
        data = 'File not found this time. Creating dummy old ip range file...'

    with open(OLD_IP_RANGE_FILE, 'w') as file:
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


def is_the_same_ip_range() -> bool:
    old_ip = read_ip_range(OLD_IP_RANGE_FILE)
    new_ip = read_ip_range(NEW_IP_RANGE_FILE)

    return old_ip == new_ip


def combine_bundle_js() -> None:
    try:
        with open(TOP_COMPONENT_FILE, 'r') as file:
            top_component = file.read()

        with open(NEW_IP_RANGE_FILE, 'r') as file:
            ip_ranges = json.load(file)['prefixes']

        with open(BOTTOM_COMPONENT_FILE, 'r') as file:
            bottom_component = file.read()

        with open(BUNDDLE_JS_FILE, 'w') as file:
            file.write(top_component)

            for index, ip in enumerate(ip_ranges):
                is_last = False

                if index == len(ip_ranges) - 1:
                    is_last = True

                formatted_ip = format_json_to_str(ip, is_last)
                file.write(formatted_ip)

            file.write(bottom_component)

    except IOError as e:
        print(f"IO error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def format_json_to_str(json_input: dict, is_last=False) -> str:
    s = ("    \"{\" \n +" +
         "\"      \\\"ip_prefix\\\": \\\"" + json_input['ip_prefix'] + "\\\", \" \n +" +
         "\"      \\\"region\\\": \\\"" + json_input['region'] + "\\\", \" \n +" +
         "\"      \\\"service\\\": \\\"" + json_input['service'] + "\\\", \" \n +" +
         "\"      \\\"network_border_group\\\": \\\"ap-northeast-2\\\" \" \n +" +
         "\"   }, \" \n +"
         )

    if is_last:
        s = ("    \"{\" \n +" +
             "\"      \\\"ip_prefix\\\": \\\"" + json_input['ip_prefix'] + "\\\", \" \n +" +
             "\"      \\\"region\\\": \\\"" + json_input['region'] + "\\\", \" \n +" +
             "\"      \\\"service\\\": \\\"" + json_input['service'] + "\\\", \" \n +" +
             "\"      \\\"network_border_group\\\": \\\"ap-northeast-2\\\" \" \n +" +
             "\"   } \" \n +"
             )
    return s


# init
move_to_old_ip_range()
fetch_new_ip_range()

# check ip is updated.
# if so, update bundle.js
if not is_the_same_ip_range():
    combine_bundle_js()
