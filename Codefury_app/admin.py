from django.contrib import admin
from .models import Announcment,Contact,Question
# Register your models here.
admin.site.register(Contact)
admin.site.register(Announcment)
admin.site.register(Question)
