from django.contrib import admin
from .models import Category, Request, RequestImage, PoliceOffice

admin.site.register(PoliceOffice)
admin.site.register(Category)
admin.site.register(Request)
admin.site.register(RequestImage)
