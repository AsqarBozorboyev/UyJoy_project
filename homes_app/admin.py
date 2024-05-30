from django.contrib import admin

from .models import Homes, Category, Contact, Comment

@admin.register(Homes)
class HomesAdmin(admin.ModelAdmin):
    list_display = ('title', 'manzil', 'category', 'narxi')
    list_filter = ['category', 'narxi']
    search_fields = ['title', 'manzil', 'category', 'narxi']
    ordering = ['status', 'publish_time']
    date_hierarchy = 'publish_time'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'body', 'created_time', 'active']
    list_filter = ['active', 'created_time']
    search_fields = ['user', 'body']
    actions = ['disable_comments', 'activate_comments']

    def disable_comments(self, request, queryset):
        queryset.update(active=False)

    def activate_comment(self, request, queryset):
        queryset.update(active=True)

# admin.site.register(Comment, CommentAdmin)