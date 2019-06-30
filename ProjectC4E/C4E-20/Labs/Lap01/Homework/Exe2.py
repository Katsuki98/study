from pymongo import MongoClient
mongo_uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'

client = MongoClient(mongo_uri)
db = client.get_default_database()


add_quote = {
    'title': 'Favorite Quote',
    'author': 'Katsuki',
    'content': 'Thà không nói để người ta tưởng mình ngu \
    Còn hơn nói ra để người ta không còn nghi ngờ gì nữa',
}
add_feedback = {
    'title': 'Feedback',
    'author': 'Katsuki',
    'content': 'friendly, funny, satisfied',
}
add_come = {
    'title': 'For future',
    'author': 'Katsuki',
    'content': 'Prepare yourself, drama is coming!',
}

db['posts'].insert_one(add_quote)
db['posts'].insert_one(add_feedback)
db['posts'].insert_one(add_come)