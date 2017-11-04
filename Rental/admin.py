from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(LocationModel)
admin.site.register(CategoryModel)
admin.site.register(Rental)
admin.site.register(Hostel)
admin.site.register(ConventionCentre)
admin.site.register(Apartment)
admin.site.register(Garage)
admin.site.register(Office)
admin.site.register(Sublet)

