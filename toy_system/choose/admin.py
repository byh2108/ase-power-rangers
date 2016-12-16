from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Menu)
admin.site.register(CustRecord)
admin.site.register(OrderRecord)
admin.site.register(MenuImage)
admin.site.register(MenuVideo)
admin.site.register(Review)

# eare
