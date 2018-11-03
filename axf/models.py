from django.db import models


# Create your models here.
# 基类
class Base(models.Model):
    img = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    trackid = models.CharField(max_length=10)

    class Meta:
        abstract = True

# 首页轮播图
class Wheel(Base):
    class Meta:
        db_table = 'axf_wheel'

# 首页导航栏
class Nav(Base):
    class Meta:
        db_table = 'axf_nav'

# 首页每日必购
class Mustbuy(Base):
    class Meta:
        db_table = 'axf_mustbuy'

# 首页商品
class Shop(Base):
    class Meta:
        db_table = 'axf_shop'


# 首页主体内容
class Mainshow(models.Model):
    class Meta:
        db_table = 'axf_mainshow'

    trackid = models.CharField(max_length=8)
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    categoryid = models.CharField(max_length=8)
    brandname = models.CharField(max_length=100)
    img1 = models.CharField(max_length=100)
    childcid1 = models.CharField(max_length=8)
    productid1 = models.CharField(max_length=8)
    longname1 = models.CharField(max_length=100)
    price1 = models.FloatField()
    marketprice1 = models.FloatField()
    img2 = models.CharField(max_length=100)
    childcid2 = models.CharField(max_length=8)
    productid2 = models.CharField(max_length=8)
    longname2 = models.CharField(max_length=100)
    price2 = models.FloatField()
    marketprice2 = models.FloatField()
    img3 = models.CharField(max_length=100)
    childcid3 = models.CharField(max_length=8)
    productid3 = models.CharField(max_length=8)
    longname3 = models.CharField(max_length=100)
    price3 = models.FloatField()
    marketprice3 = models.FloatField()

# 闪购超市分类
class Foodtypes(models.Model):
    typeid = models.CharField(max_length=8)
    typename = models.CharField(max_length=100)
    childtypenames =  models.CharField(max_length=256)
    typesort = models.IntegerField()

    class Meta:
        db_table='axf_foodtypes'


# 闪购超市商品内容
class Goods(models.Model):
    productid = models.CharField(max_length=20)
    productimg= models.CharField(max_length=100)
    productname= models.CharField(max_length=100)
    productlongname= models.CharField(max_length=100)
    isxf= models.BooleanField(default=False)
    pmdesc= models.BooleanField(default=False)
    specifics= models.CharField(max_length=100)
    price= models.DecimalField(max_digits=10,decimal_places=2)
    marketprice= models.DecimalField(max_digits=10,decimal_places=2)
    categoryid= models.IntegerField()
    childcid= models.IntegerField()
    childcidname= models.CharField(max_length=100)
    dealerid= models.CharField(max_length=20)
    storenums= models.IntegerField()
    productnum= models.IntegerField()
