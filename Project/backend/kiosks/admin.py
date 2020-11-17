from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')

class MenuAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'price', 'description', 'category')

class VirtualUserAdmin(admin.ModelAdmin):
    list_display = ('id','age')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','virtual_user', 'date', 'price')

class DetailAdmin(admin.ModelAdmin):
    list_display = ('id','menu', 'amount', 'order')

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(VirtualUser, VirtualUserAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Detail, DetailAdmin)
admin.site.register(History)
admin.site.register(VirtualHistory)