mobile_data = {
    'status': True,
    'data': [
          {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
          {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
          {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
          {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
          {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
          {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
            ],
    'exchnage_rate': 107.25
            }

brand = (mobile_data['data'][0]['name'])
origin = (mobile_data['data'][0]['made'])
amount = int(mobile_data['data'][0]['price'][:-3])
usd = (mobile_data['data'][0]['price'][4:])
bdt = int(mobile_data['exchnage_rate'])
usd1 = amount * bdt

print(f'{brand} is made from {origin}.The price is {amount} {usd} which is almost equal to {usd1} BDT')