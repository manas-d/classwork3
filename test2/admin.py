from django.contrib import admin

# Register your models here.
from django.contrib import admin

from test2.models import Post, Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
