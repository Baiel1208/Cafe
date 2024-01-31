from django.contrib import admin
from . import models

class AboutInline(admin.TabularInline):
    model = models.About
    extra = 1

class StatiInline(admin.TabularInline):
    model = models.Stati
    extra = 1

class SettingsFilterAdmin(admin.ModelAdmin):
    list_filter = ('context',)
    list_display = ('title', 'context')
    search_fields = ('title', 'context')
    inlines = [AboutInline, StatiInline]


class InterestingInline(admin.TabularInline):
    model = models.Interesting
    extra = 1

class ProductFilterAdmin(admin.ModelAdmin):
    list_filter=['title']
    list_display = ('title', 'context', 'price', 'cart')  
    search_fields = ('title', 'context', 'price', 'cart')  
    inlines = [InterestingInline]

admin.site.register(models.Settings, SettingsFilterAdmin)
admin.site.register(models.Product, ProductFilterAdmin)



########################################################

admin.site.register(models.AboutMain)
admin.site.register(models.Blog)
