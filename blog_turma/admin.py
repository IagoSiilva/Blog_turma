from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('author','title','text')
    list_per_page=5
    list_editable=('title','text')
    search_fields=('title',)
