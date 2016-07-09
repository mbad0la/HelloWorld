from django.contrib import admin
from app.models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Login)
admin.site.register(Votes)
admin.site.register(Poll)
admin.site.register(Project)