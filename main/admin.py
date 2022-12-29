from django.contrib import admin
from .models import Person, Singer,Rank

admin.site.register(Person)
admin.site.register(Singer)
admin.site.register(Rank)


# Группы пользователей
#   * admin - superuser
#   * zam - ...
#   * kurator
#   * helper