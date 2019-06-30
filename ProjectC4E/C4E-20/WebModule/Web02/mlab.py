import mongoengine

# mongodb://admin:kazaru98shinnisuto@ds125912.mlab.com:25912/muadongkhonglanh-c4e20

host = "ds125912.mlab.com"
port = 25912
db_name = "muadongkhonglanh-c4e20"
user_name = "admin"
password = "kazaru98shinnisuto"


def connect():
    mongoengine.connect(
        db_name, 
        host=host, 
        port=port, 
        username=user_name, 
        password=password
    )

