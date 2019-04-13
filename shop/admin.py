from urllib.parse import quote

import requests
from django.contrib import admin
# Register your models here.
from django.utils.safestring import mark_safe

from shop.models import City, Banner, ShopSetting, Product, Category, Company, ProductLabel, ProductGallery, UserProduct


class UserProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'created_at', 'updated_at')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'failure', 'click', 'count', 'chatrbazi', 'is_free')
    list_filter = ('type',)
    search_fields = ('name', 'category__name', 'company__name', 'label__name')

    def headshot_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=150,
            height=150,
        )
        )

    readonly_fields = ('headshot_image',)

    def save_model(self, request, obj, form, change):
        super(ProductAdmin, self).save_model(request, obj, form, change)
        url = u'https://chatrbaazan.ir/chatrbazan_bot/broadcast.php?send_notification&slug={0}'.format(
            obj.slug)
        result = requests.get(quote(url, safe=':/.?&='))
        if result.status_code == 200 and result.content:
            print('send notification success: ', url)
        else:
            print('send notification failed: ', url)


class CompanyAdmin(admin.ModelAdmin):
    search_fields = ('name',)

    def headshot_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=150,
            height=150,
        )
        )

    readonly_fields = ('headshot_image',)


class GalleryAdmin(admin.ModelAdmin):
    def headshot_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=150,
            height=150,
        )
        )

    readonly_fields = ('headshot_image',)


class BannerAdmin(admin.ModelAdmin):
    def headshot_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=150,
            height=150,
        )
        )

    readonly_fields = ('headshot_image',)


admin.site.register(City)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(UserProduct, UserProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(ProductLabel)
# admin.site.register(Discount)
admin.site.register(ProductGallery, GalleryAdmin)
admin.site.register(ShopSetting)
