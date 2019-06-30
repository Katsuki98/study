import mlab
from mongoengine import *
from models.service import Service

mlab.connect()

id_to_find = "5b781d7b67609f1dc46f0195"
doc_id = Service.objects.get(id=id_to_find)
doc_id.delete()