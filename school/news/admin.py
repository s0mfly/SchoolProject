from django.contrib import admin
from .models import Articles, Polzakt


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'anons', 'full_text', 'date')
    list_display_links = ('title', 'anons')
    search_fields = ('title', 'anons',)


admin.site.register(Articles, ArticlesAdmin)


class PolzaktAdmin(admin.ModelAdmin):
    list_display = ('idpolz', 'famil', 'name', 'telefon', 'electpoch', 'chr_class', 'datareg',
                    'pole1', 'pole2', 'pole3', 'pole4', 'pole5')
    list_display_links = ('pole1', 'pole2', 'pole3', 'pole4', 'pole5')
    search_fields = ('idpolz', 'famil', 'name', 'telefon', 'electpoch', 'chr_class', 'datareg',)


admin.site.register(Polzakt, PolzaktAdmin)


