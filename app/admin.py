from django.contrib import admin
from .models import (
    Customer,
    Product,
    Cart,
    OrderPlaced,
)
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "name", "locality", "city", "zipcode", "state"]
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "selling_price", "discounted_price",  "description", "brand", "category", "product_image"]
@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "product", "quantity"]
@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "customer", "product", "quantity", "ordered_date", "status"]
admin.site.site_header = "Hackcoder Admin"
admin.site.index_title = "𝕎𝕖𝕝𝕔𝕠𝕞𝕖 𝕋𝕒𝕟𝕛𝕚𝕞𝕦𝕝 ℍ𝕚𝕤𝕙𝕒𝕞 (𝔽𝕒𝕣𝕕𝕚𝕟)"
admin.site.site_title = "𝔸𝕕𝕞𝕚𝕟 𝕋𝕒𝕟𝕛𝕚𝕞𝕦𝕝 ℍ𝕚𝕤𝕙𝕒𝕞"