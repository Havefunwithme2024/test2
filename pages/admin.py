from django.contrib import admin
from .models import Categories, Subjects, Items, GalleryItems
from django.utils.html import format_html


admin.site.register(Categories)
admin.site.register(Subjects)


class GalleryItemInline(admin.TabularInline):
    model = GalleryItems
    extra = 1


@admin.register(Items)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'quantity_views', 'is_available', 'creation_datetime', 'updates_datetime', 'author', 'show_photo']
    list_display_links = ['pk', 'title']
    prepopulated_fields = {'slug': ['title']}
    inlines = [GalleryItemInline]
    list_per_page = 10
    list_filter = ['category__name', 'subject_item__name']
    search_fields = ['title', 'description', 'card_description']
    ordering = ['-creation_datetime']
    list_editable = ['is_available']
    filter_horizontal = ['subject_item']


    @admin.action(description='Фото товара')
    def show_photo(self, obj):
        try:
            image = obj.get_first_photo()
            return format_html(f'<img src="{image}" width="100">')
        except:
            return '-'