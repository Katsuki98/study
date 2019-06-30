from models.customer import Customer
import mlab
from faker import Faker
from random import randint,choice

mlab.connect()

fake = Faker()

for i in range(50):
    print('Saving customer', i + 1, '......')
    yob = randint(90,99)
    ctm_name = fake.name()
    new_customer = Customer(
        name=ctm_name,
        gender=randint(0,1),
        email=ctm_name.replace(' ', '') + str(yob) + "@gmail.com",
        phone=fake.phone_number(),
        job=fake.job(),
        company=fake.company(),
        contacted=choice([True, False])
    )

    new_customer.save()