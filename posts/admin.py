from django.contrib import admin
from .models import Post, Comment
# Register your models here.


class CommentAdminInline(admin.TabularInline):
    model = Comment
    fields = ['author', 'text',]
    extra = 0




@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title']
    inlines = [CommentAdminInline,]

