from pprint import pprint


data = [
   ['hour','name','year','age'],
   [12,'pravin',1997,23],
   [12,'navin',1995,25],
   [12,'prashant',1989,30]
]

out = {'results':[dict(zip(data[0], row)) for row in data[1:]]}

pprint(out)