from pymongo import MongoClient

mongo_uri = 'mongodb://admin:kazaru98shinnisuto@ds113402.mlab.com:13402/c4e20_lab'

# 1. Connect to database
client = MongoClient(mongo_uri)

# 2. Get database
db = client.get_default_database()

# 3. Create a collection
games = db['games']

# # 4. Create a document
# new_game = {
#     'title': 'PES',
#     'description': 'Pro Evolution Soccer',
# }

# # 5. Insert doc into collection 
# games.insert_one(new_game)

# 6. Read all documents
all_game = games.find()
first_game = all_game[0]
print(first_game['title'])