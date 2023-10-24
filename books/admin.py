from django.contrib import admin
from .models import Book, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'text', 'book', 'datetime_created', 'recommend', 'is_active']
    search_fields = ('user', 'text', 'book')


admin.site.register(Book)
# admin.site.register(Comment, CommentAdmin)
