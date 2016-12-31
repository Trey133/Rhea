#!/usr/bin/python
elif verb == "btc":
        print('---')
        for currency, symbol in currencies:
            r = requests.get('http://data.mtgox.com/api/2/{}/money/ticker'.format(currency))
            data = r.json()['data']
            avg = float(data['avg']['value'])
            high = float(data['high']['value'])
            low = float(data['low']['value'])
            last = float(data['last']['value'])

            print(currency.encode('utf8'))
            print('Low: {}{::.2f}'.format(symbol,low).encode('utf8'))
            print('Average: {}{::.2f}'.format(symbol,low).encode('utf8'))
            print('High: {}{::.2f}'.format(symbol,low).encode('utf8'))
            print('Last: {}{::.2f}'
.format(symbol,low).encode('utf8'))
            print('---')

