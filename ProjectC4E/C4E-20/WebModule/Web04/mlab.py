import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds133601.mlab.com:33601/cms-c4e-20

host = 'ds133601.mlab.com'
port = 33601
db_name = 'cms-c4e-20'
user_name = 'admin'
password = 'kazaru98shinnisuto'

def connect():
    mongoengine.connect(
        db_name, 
        host=host, 
        port=port, 
        username=user_name, 
        password=password
    )