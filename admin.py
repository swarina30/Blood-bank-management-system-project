from django.contrib import admin
from .models import *


admin.site.site_header = 'Admin Dashboard'
admin.site.register(donorform)
admin.site.register(requesterlist)
