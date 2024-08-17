from django.utils.html import format_html
from django.contrib import admin
from .models import *


@admin.register(Nft)
class NftAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "img_nft",
        "name",
        "created_by__user__username",
        "prise",
        "is_sold",
    )
    list_display_links = (
        "id",
        "img_nft",
        "name",
        "created_by__user__username",
        "prise",
        # "is_sold",
    )
    list_filter = (
        "collection",
        "is_sold",
        "tegs",
    )

    search_fields = ("name", "created_by__user__username")

    readonly_fields = ("create_date",)
    list_editable = ("is_sold",)

    def img_nft(self, obj):

        return format_html(
            f'<img src="{obj.img.url}" width="50" height="50" style="object-fit: cover;"/>'
        )

    img_nft.short_description = "Nft"


@admin.register(Tegs)
class TegsAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "img_user",
        "user__username",
        "created",
        "nfts_sold",
        "balans",
    )
    list_display_links = (
        "id",
        "img_user",
        "user__username",
        "created",
        "nfts_sold",
        "balans",
    )

    readonly_fields = (
        "created",
        "nfts_sold",
        "balans",
    )

    def img_user(self, obj):

        return format_html(
            f'<img src="{obj.photo.url}" width="50" height="50" style="object-fit: cover;"/>'
        )

    img_user.short_description = "Фото"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "img_category", "name")
    list_display_links = ("id", "name")

    def img_category(self, obj):

        return format_html(
            f'<img src="{obj.photo.url}" width="50" height="50" style="object-fit: cover;"/>'
        )

    img_category.short_description = "Изображения"
