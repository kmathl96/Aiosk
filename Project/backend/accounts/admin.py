from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','phoneNum', 'point')

class CouponAdmin(admin.ModelAdmin):
    list_display = ('id','code', 'user')

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Coupon, CouponAdmin)