from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.

# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here

# class CarModelInline(admin.TabularInline):
#     model = CarModel


# class CarModelAdmin(admin.ModelAdmin):
#     model = CarModel

# class CarMakeAdmin(admin.ModelAdmin):
#     model = CarMake
#     inlines = [
#         CarModelInline
#     ]


admin.site.register(CarMake)
admin.site.register(CarModel)
