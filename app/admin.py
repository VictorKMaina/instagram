from django.contrib import admin
from .models import Profile, Image, Comment

class ImageAdmin(admin.ModelAdmin):
    exclude = ('likes',)

# Register your models here.
admin.site.register(Profile)
admin.site.register(Image, ImageAdmin)
admin.site.register(Comment)