from django.contrib import admin
from django.contrib.auth.models import Group, User

from .models import Product

admin.site.unregister(Group)
admin.site.unregister(User)
# admin.site.site_title = admin.site.site_header
admin.site.register(Product)
