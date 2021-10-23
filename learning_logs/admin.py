from django.contrib import admin
from .models import Topic
admin.site.register(Topic)
from .models import Topic, Entry
admin.site.register(Entry)

# Register your models here.
