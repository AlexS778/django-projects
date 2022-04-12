from django.contrib import admin

from .models import ISO, Category, Region, Site, State

admin.site.register(ISO)
admin.site.register(Category)
admin.site.register(Region)
admin.site.register(Site)
admin.site.register(State)
