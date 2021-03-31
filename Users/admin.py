from django.contrib import admin
from Users import models as model

# Register your models here.
myModels = [model.Profile, model.Contact]
admin.site.register(myModels)