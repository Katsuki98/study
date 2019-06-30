from models.service import Service
import mlab

mlab.connect()

# all_service = Service.objects()

# first_service = all_service[0]

# print(first_service['name'])

id_to_find = '5b78203867609f09b48fc091'

# hera = Service.objects(id=id_to_find)  ## => [Service obj]
# hera = Service.objects.get(id=id_to_find)  ## => Service obj
service = Service.objects.with_id(id_to_find)  ## => Service obj

# check if document exist
if service is not None:
    # print(service.name)
    # service.delete()
    # print('Deleted')
    print('Before: ')
    print(service.to_mongo())
    service.update(set__yob=2005)
    service.reload()
    print('After: ')
    print(service.to_mongo())
else:
    print('Not found')