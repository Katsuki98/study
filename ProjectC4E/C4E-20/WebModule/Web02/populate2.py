from models.service import Service
import mlab
from faker import Faker
from random import *

mlab.connect()

fake = Faker()

for i in range(20):
    print('Saving service', i + 1, '...')
    gender = randint(0,1)
    des_male = ['đẹp trai','thích thể thao','trầm tính','năng động','hào phóng','tiết kiệm','hoà đồng','giàu có']
    des_female = ['xinh xắn','nhu mì','cởi mở','vị tha','chung thuỷ','sôi động','chăm chỉ','tomboy']
    image_male = ['male.jpg','hand.jpg','slide4.jpg','slide5.jpg'] 
    image_female = ['female.jpg','hand.jpg','slide3.jpg']

    if gender:
        new_service = Service(
            image = '../static/image/' + choice(image_male),
            name = fake.name(),
            gender = gender,
            yob = randint(1990,2000),
            height = randint(150,190),
            phone = fake.phone_number(),
            address = fake.address(),
            description = fake.words(ext_word_list=des_male,3)
        )
    else:
        new_service = Service(
            image = '../static/image/' + choice(image_female),
            name = fake.name(),
            gender = gender,
            yob = randint(1990,2000),
            height = randint(150,170),
            phone = fake.phone_number(),
            address = fake.address(),
            description = fake.words(ext_word_list=des_female,3),
            measurements = [randint(70,90), randint(60,70), randint(70,90)]
        )

    new_service.save()
