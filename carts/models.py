from django.db import models

# Create your models here.
from accounts.models import User
from shop.models import Product


# class CartSession(models.Model):
#     ip = models.CharField(max_length=150, verbose_name=u"Ip")
#     key = models.CharField(max_length=500, verbose_name=u"Key Session")
#     header = models.TextField(verbose_name="Header Request")
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


class Cart(models.Model):
    STATUS = (
        (1, u"در حال انجام"),
        (3, u"موفق"),
        (4, u"لغو شده توسط کاربر"),
        (5, u"مشکل در درگاه پرداخت"),
    )
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name="cart_user",
                             verbose_name=u"کاربر")
    price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, verbose_name=u"مبلغ")
    total_price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True,
                                      verbose_name=u"مبلغ نهایی")
    status = models.PositiveSmallIntegerField(choices=STATUS, default=1, verbose_name=u"وضعیت")
    # session = models.ForeignKey(CartSession, on_delete=models.CASCADE, related_name="cart_session",
    #                             verbose_name=u"جلسه")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = u"سبد خرید"
        verbose_name_plural = u"سبد خرید"


class CartItem(models.Model):
    product = models.ForeignKey(Product, models.CASCADE, related_name="cartItem_product", verbose_name=u"محصول")
    price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, verbose_name=u"مبلغ")
    total_price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True,
                                      verbose_name=u"مبلغ نهایی")
    cart = models.ForeignKey(Cart, models.CASCADE, related_name="cartItem_cart", verbose_name=u"سبد خرید")
    count = models.IntegerField(default=1, verbose_name=u"تعداد")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = u"آیتم های سبد خرید"
        verbose_name_plural = u"آیتم های سبد خرید"

    def __str__(self):
        return str(self.product)

    def delete(self, using=None, keep_parents=False, *args, **kwargs):
        # print('action', self.__class__.__str__())
        print('object', str(self))

        oldData = self
        print('cart', str(self.cart))
        super(CartItem, self).delete(*args, **kwargs)
        cart = Cart.objects.filter(id=oldData.cart.id)
        if cart.count() > 0:
            item = CartItem.objects.filter(cart__id=cart.first().id)
            if item.count() == 0:
                print('count item', str(item.count()))
                cart.first().delete()
            else:
                cart = cart.first()
                cart.price = cart.price - oldData.total_price
                cart.total_price = cart.total_price - oldData.total_price
                if cart.price < 0 or cart.total_price < 0:
                    cart.delete()
                    print('bug')
                else:
                    cart.save()

    def update_price(self, cartId):
        print('action update price evented ')
        cartItem = CartItem.objects.filter(cart__id=cartId)
        print(str(cartItem))
        tt_price = 0
        if cartItem.count() > 0:
            for citem in cartItem:
                if citem.count == 0:
                    citem.delete()
                    continue
                if not citem.price:
                    price = citem.product.price
                else:
                    price = citem.price
                print('price', str(citem.price))
                print('count',str(citem.count))
                tt_price_item = int(price) * int(citem.count)
                citem.price = price
                citem.total_price = tt_price_item
                citem.save()
                tt_price += citem.total_price
        else:
            Cart.objects.filter(id=cartId).delete()
        if tt_price >= 0:
            Cart.objects.filter(id=cartId).update(
                price=tt_price, total_price=tt_price)
        else:
            Cart.objects.filter(id=cartId).delete()


    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None, *args, **kwargs):
        super(CartItem, self).save(*args, **kwargs)
    
