from django.contrib import admin
from .models import Concerts, Places, Artists, Genres, Typesofplaces


# Register your models here.
admin.site.register(Concerts)
admin.site.register(Places)
admin.site.register(Artists)
admin.site.register(Genres)
admin.site.register(Typesofplaces)