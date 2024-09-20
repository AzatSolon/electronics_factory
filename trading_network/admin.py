from django.contrib import admin

from trading_network.models import Factory, Contact, Network, Product


@admin.action(description="Обнулить задолженность перед поставщиком")
def clear_debt(modeladmin, request, queryset):
    queryset.update(debt_to_supplier=0.00)


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ["title", "email", "country", "city", "address", "phone_number"]


@admin.register(Contact)
class RetailAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "email",
        "country",
        "city",
        "address",
        "phone_number",
        "arrears",
        "product",
        "supplier",
    ]
    list_filter = ("city",)
    list_display_links = ["supplier"]


@admin.register(Network)
class IndividualAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "level", "supplier", "debt_to_supplier"]
    actions = [clear_debt]
    list_display_links = ["supplier"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "factory",
        "name",
        "model",
        "release_date",
        "created_at",
        "supplier",
    ]
    list_filter = (
        "release_date",
        "supplier",
    )
    list_display_links = ["supplier"]
