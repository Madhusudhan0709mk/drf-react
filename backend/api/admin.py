from django.contrib import admin
from .models import *
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','thumbnail']

class UserAdmin(admin.ModelAdmin):
    search_fields  = ['username', 'email']
    list_display  = ['username', 'email']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title"]

class PostAdmin(admin.ModelAdmin):
    list_display = ["title","user","category","view"]

class CommentAdmin(admin.ModelAdmin):
    list_display = ["post","name","email","comment"]

class BookmarkAdmin(admin.ModelAdmin):
    list_display = ["user","post"]

class NotificationAdmin(admin.ModelAdmin):
    list_display = ["user","post","type","seen",]

admin.site.register(User,UserAdmin)
admin.site.register(Profile,ProfileAdmin)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(Bookmark, BookmarkAdmin)