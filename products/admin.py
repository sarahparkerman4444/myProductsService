from django.contrib import admin
from .models import Product, Property


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'installation_date', 'manufacture_date', 'category', 'create_date', 'edit_date')
    display = 'Product'
    list_filter = ('create_date',)
    readonly_fields = ('uuid', 'replaced_product', )
    search_fields = ('name',)


class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_date', 'edit_date')
    display = 'Property'
    list_filter = ('create_date',)
    search_fields = ('name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Property, PropertyAdmin)
