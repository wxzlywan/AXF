from django.shortcuts import render

# Create your views here.
from axf.models import Wheel, Nav, Mustbuy, Shop


def home(request):      # 首页
    # 获取顶部轮播图数据
    wheels = Wheel.objects.all()

    # 获取导航栏数据
    navs = Nav.objects.all()

    # 获取每日必购数据
    mustbuys = Mustbuy.objects.all()

    # 获取商品数据
    shophead = Shop.objects.get(pk=1)
    shoptabs = Shop.objects.filter(pk__gt=1, pk__lt=4)
    shopclasses = Shop.objects.filter(pk__gt=3,pk__lt=8)
    shopcommends = Shop.objects.filter(pk__gt=7)


    # 获取主体内容数据
    data = {
        'wheels':wheels,
        'navs':navs,
        'mustbuys':mustbuys,
        'shophead': shophead,
        'shoptabs':shoptabs,
        'shopclasses':shopclasses,
        'shopcommends':shopcommends,
    }

    return render(request,'home/home.html',data)


def market(request):    # 闪购超市
    return render(request,'market/market.html')


def cart(request):      # 购物车
    return render(request,'cart/cart.html')


def mine(request):      # 我的
    return render(request,'mine/mine.html')