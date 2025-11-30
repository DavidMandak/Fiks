import requests


def get(path: str) -> dict:
    global environment, token
    url = environment+path
    params = {"botToken": token}

    response = requests.get(url=url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code)
        return None


def post(path: str, body: dict) -> dict:
    global environment, token
    url = environment+path
    params = {"botToken": token}

    response = requests.post(url=url, params=params, json=body)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code)
        return None


def delete(path: str, body: dict) -> dict:
    global environment, token
    url = environment+path
    params = {"botToken": token}

    response = requests.delete(url=url, params=params, json=body)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code)
        return None


exchange = [line.split() for line in open("12.ročník/Exchanges.txt").read().splitlines()]

environment, token = exchange[0]
name = "DejfMandy"
side = None
price = None
amount = None

body = {
    "botName": name,
    "side": "Sell",
    "priceCents": 1000,
    "quantity": 1
}

order_id = get("Orders/orders/mine")["sellOrders"][0]["id"]
delete(f"Orders/{order_id}", body)
