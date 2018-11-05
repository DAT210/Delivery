import requests

jobs = [{
    "order_id": 1,
    "delivery_method": "driving",
    "address": "Stokkabrautene+24a+stavanger",
    "aborted": False
},
{
    "order_id": 2,
    "delivery_method": "driving",
    "address": "Joahn+thorsens+gate+41+stavanger",
    "aborted": False
},{
    "order_id": 3,
    "delivery_method": "driving",
    "address": "Cleng+Peersons+vei+1+stavanger",
    "aborted": False
},
{
    "order_id": 4,
    "delivery_method": "driving",
    "address": "Olav+Kyrres+gate+7+stavanger",
    "aborted": False
},
{
    "order_id": 5,
    "delivery_method": "driving",
    "address": "Admiral+Hammerichs+vei+18b+stavanger",
    "aborted": False
},
{
    "order_id": 6,
    "delivery_method": "driving",
    "address": "Solåsveien+13+stavanger",
    "aborted": False
}]


def main():
    for o in jobs:
        r = requests.post("http://127.0.0.1:1337/delivery/neworder", data=o)
        print(r.content)


if __name__ == "__main__":
    main()