from django.contrib import admin
from blog.models import Blog

class BlogAdministrator(admin.ModelAdmin):
	prepopulated_fields = {'slug' : ('title',)}
	list_display = ('title','time')
admin.site.register(Blog,BlogAdministrator)
