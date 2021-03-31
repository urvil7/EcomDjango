from django.contrib import admin
from Products import models as model

# Register your models here.
myModels = [model.Categorie, model.Order, model.Product]
admin.site.register(myModels)