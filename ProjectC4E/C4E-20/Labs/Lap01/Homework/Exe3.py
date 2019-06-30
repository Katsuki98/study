import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot

from pymongo import MongoClient
mongo_uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'

# count
client = MongoClient(mongo_uri)
db = client.get_default_database()

cts = db['customers']
all_cts = cts.find()

all_refs = {}
all_refs['Events'] = 0
all_refs['Advertisements'] = 0
all_refs['Word of mouth'] = 0

for i in all_cts:
    if i['ref'] == 'events':
        all_refs['Events'] += 1
    elif i['ref'] == 'ads':
        all_refs['Advertisements'] += 1
    elif i['ref'] == 'wom':
        all_refs['Word of mouth'] += 1

labels = []
values = []

for key, value in all_refs.items():
    print("The number of customers in group", key, ": ", value)
    labels.append(key)
    values.append(value)

# chart
colors = ['red','blue','yellow']
explode = [0,0,0.2]

pyplot.pie(
    values,
    labels=labels,
    colors=colors,
    explode=explode
)
pyplot.axis('equal')
pyplot.show()
