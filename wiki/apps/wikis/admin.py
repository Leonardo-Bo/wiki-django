from django.contrib import admin
from .models import WikiPost, WikiCategory


class WikiAdmin(admin.ModelAdmin):
    list_display = ["__str__", "author", "category", "created_date", "updated_date"]
    list_filter = ["category", "author", "created_date", "updated_date"]
    search_fields = ["title", "content", "category", "created_date", "updated_date"]
    readonly_fields = ('slug',)

    class Meta: 
        model = WikiPost


class WikiCategoryAdmin(admin.ModelAdmin):
    list_display = ["__str__", "slug", "author", "created_date", "updated_date"]

    class Meta:
        model = WikiCategory


admin.site.register(WikiPost, WikiAdmin)
admin.site.register(WikiCategory, WikiCategoryAdmin)
