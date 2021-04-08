import requests


def get_prices():
    name = "SeedifyFund"

    crypto_data = requests.get("https://api.pancakeswap.info/api/tokens").json()["data"]

    data = None
    for i in crypto_data:
        current = crypto_data[i]

        if current['name'] == name:
          data = {
              "coin": i,
              "priceusd": current["price"],
              "pricebnb": current["price_BNB"],
          }

    return data


if __name__ == "__main__":
    print(get_prices())