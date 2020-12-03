from django.contrib import admin
from .models import WikiPost, WikiCategory


class WikiAdmin(admin.ModelAdmin):
    list_display = ["__str__", "author", "date", "category"]
    list_filter = ["category", "date"]
    search_fields = ["title", "content", "category", "date"]
    readonly_fields = ('slug',)

    class Meta: 
        model = WikiPost


class WikiCategoryAdmin(admin.ModelAdmin):
    list_display = ["__str__", "slug", "author", "date"]

    class Meta:
        model = WikiCategory


admin.site.register(WikiPost, WikiAdmin)
admin.site.register(WikiCategory, WikiCategoryAdmin)
