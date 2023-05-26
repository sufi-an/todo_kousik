from django.contrib import admin

from core.models import  User,Task

# Register your models here.

class UserAdmin(admin.ModelAdmin):

    list_display=('last_name','first_name','email')
    search_fields =('last_name','first_name','email')
    list_per_page=25
    

admin.site.register(User, UserAdmin)
admin.site.register(Task)

admin.site.site_title = 'conf_proj'
admin.site.site_header = 'conf_proj'
