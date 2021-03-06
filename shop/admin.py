from django.contrib import admin
# Register your models here.
from django.utils.safestring import mark_safe

from shop.models import City, Banner, ShopSetting, Product, Category, Company, ProductLabel, ProductGallery, \
    UserProduct, Score


class UserProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'created_at', 'updated_at')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'failure', 'company_name', 'discount_code', 'click', 'chatrbazi')
    list_filter = ('type',)
    search_fields = ('name', 'category__name', 'company__name', 'label__name')

    def company_name(self, obj):
        return " ,".join([c.name for c in obj.company.all()])

    company_name.short_description = "کمپانی"

    def headshot_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=150,
            height=150,
        )
        )

    readonly_fields = ('headshot_image',)


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


class ScoreAdmin(admin.ModelAdmin):
    list_display = ('company', 'star',)


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
admin.site.register(Score, ScoreAdmin)
