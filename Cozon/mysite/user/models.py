from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    content = RichTextUploadingField(null=True, blank=True)

# # class UserInfo(models.Model):
# #     class Meta:
# #         verbose_name='用户信息'
# #         verbose_name_plural=verbose_name
# #     user=models.OneToOneField(User,on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.user.username

class uuser(models.Model):
    class Meta:
        verbose_name = '用户信息表'
        verbose_name_plural = verbose_name
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=100)
    def __str__(self):
        return self.user.username


class Category(models.Model):
    class Meta:
        verbose_name='商城列表'
        verbose_name_plural=verbose_name
    parent=models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True)
    icon=models.ImageField("图标",blank=True,null=True)
    title = models.CharField("名称",max_length=20)
    def __str__(self):
        return self.title

class Picture(models.Model):
    class Meta:
        verbose_name='图片'
        verbose_name_plural=verbose_name

    url=models.ImageField('URL')
    desciption=models.CharField('描述',max_length=100)
    link=models.URLField("链接")
    type=models.SmallIntegerField('类型',default=1,choices=[(1,'轮播图'),(2,'广告图')])
    def __str__(self):
        return self.desciption

class Product(models.Model):
    class Meta:
        verbose_name = '商品'
        verbose_name_plural = verbose_name
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title  = models.CharField('标题', max_length=30)
    sell_price=models.DecimalField("售价",max_digits=5,decimal_places=2)
    market_price = models.DecimalField("市场价", max_digits=5, decimal_places=2)
    picture=models.ImageField('主图',upload_to='product/%Y%m%d')
    detail=models.TextField("详情",max_length=3000)

    def __str__(self):
        return self.title
class ShopCart(
    models.Model):
    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = verbose_name
    user=models.OneToOneField(User,on_delete=models.CASCADE,verbose_name='用户')
    product=models.ManyToManyField(Product,through='ShopCartProduct',through_fields=('shopcart','product'))

class ShopCartProduct(models.Model):
    shopcart=models.ForeignKey(ShopCart,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    number= models.SmallIntegerField(default=0)

class Detial(models.Model):
    class Meta:
        verbose_name = '详情'
        verbose_name_plural = verbose_name
    product=models.OneToOneField(Product,on_delete=models.CASCADE,verbose_name='商品')
    product_type = models.CharField('产品类型', max_length=30)
    yuanliao_chandi = models.CharField("原料产地", max_length=15)
    product_chandi = models.CharField("产地", max_length=10)
    peiliao = models.CharField('配料', max_length=50)
    baozhiqi = models.CharField("保质期", max_length=18)
    savemethod=models.CharField("保存方法", max_length=20)
    eatmethod=models.CharField("实用方法", max_length=20)
    picture = models.ImageField('配图', upload_to='product/%Y%m%d')




class Address(models.Model):
    class Meta:
        verbose_name = '地址'
        verbose_name_plural = verbose_name
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=100)




class Commentt(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=20, default='佚名')
    content = models.CharField(verbose_name='内容', max_length=300)
    color = models.CharField(verbose_name='颜色', max_length=10)
    chicun = models.CharField(verbose_name='尺寸', max_length=10)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '商品评论'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.content[:10]

# Create your models here.
