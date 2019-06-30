from mongoengine import *

# design database
# define collection
class Service(Document):  
    # Service() kế thừa class Document
    image = StringField()
    name = StringField()
    gender = IntField()
    yob = IntField()
    height = IntField()
    phone = StringField()
    address = StringField() 
    description = ListField()
    measurements = ListField()