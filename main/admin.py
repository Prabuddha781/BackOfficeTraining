from django.contrib import admin

# Register your models here.
from .models import DebitEntry, SecondPage, Overview

admin.site.register(SecondPage)
admin.site.register(DebitEntry)
admin.site.register(Overview)