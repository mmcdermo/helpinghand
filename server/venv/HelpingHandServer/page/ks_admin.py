

from django.contrib import admin
from models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ('title','menu','targetType','target')

admin.site.register(Item,ItemAdmin)


from django.contrib import admin
from models import Page
admin.site.register(Page)
