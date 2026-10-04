import requests
import pprint

URL = "http://127.0.0.1:5000/inventory"


def get_inventory():
    print("Fetching data ...")
    try:
        res = requests.get(URL)

        if res.status_code == 200:
            data = res.json()
            print("Inventory Items::")
            pprint.pprint(data, indent=2)
        else:
            data = res.json()
            if "message" in data:
                print(
                    f"Failed to fetch data:\nStatus code: {res.status_code}\n{data['message']}"
                )
            else:
                print(f"Failed to fetch data:\nStatus code: {res.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"A network error occurred: {e}")


def add_item(args):
    print("Posting data...")
    item = {}
    item["name"] = args.name

    if args.quantity:
        item["quantity"] = args.quantity
    if args.brands:
        item["brands"] = args.brands

    try:
        res = requests.post(URL, json=item)
        if res.status_code == 201:
            data = res.json()
            print("New product added successfully::")
            pprint.pprint(data, indent=2)
        else:
            data = res.json()
            if "message" in data:
                print(
                    f"Failed to Post data:\nStatus code: {res.status_code}\n{data['message']}"
                )
            else:
                print(f"Failed to post data:\nStatus code: {res.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"A network error occured: {e}")


def get_item(args):
    print(f"Serching for item id: {args.id} ...")

    try:
        res = requests.get(URL + f"/{args.id}")
        if res.status_code == 200:
            data = res.json()
            print(f"Item ({data['name']})::")
            pprint.pprint(data, indent=2)
        else:
            data = res.json()
            if "message" in data:
                print(
                    f"Failed to retrieve data:\nStatus code: {res.status_code}\n{data['message']}"
                )
            else:
                print(f"Failed to retrieve data:\nStatus code: {res.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"A network error occured: {e}")
