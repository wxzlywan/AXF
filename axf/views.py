from django.shortcuts import render

# Create your views here.
from axf.models import Wheel, Nav, Mustbuy, Shop, Mainshow, Foodtypes, Goods


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
    mainshow = Mainshow.objects.all()

    data = {
        'wheels':wheels,
        'navs':navs,
        'mustbuys':mustbuys,
        'shophead': shophead,
        'shoptabs':shoptabs,
        'shopclasses':shopclasses,
        'shopcommends':shopcommends,
        'mainshow': mainshow,
    }

    return render(request,'home/home.html',data)


def market(request,categoryid,childid,sortid):    # 闪购超市
    # 分类数据
    foodtypes = Foodtypes.objects.all()

    # 子类商品数据
    typeIndex = int(request.COOKIES.get('typeIndex',0))

    categoryid = foodtypes[typeIndex].typeid

    childtypename  =foodtypes.get(typeid=categoryid).childtypenames

    childList = []
    dir1 = {}
    for item in childtypename.split('#'):
        arr1 = item.split(':')
        dir1 = {
            'childname':arr1[0],
            'childid':arr1[1]
        }
        childList.append(dir1)
        # print(childList)
        # print(type(childList))


    if childid == '0':
        goods = Goods.objects.filter(categoryid=categoryid)
    else:
        goods = Goods.objects.filter(categoryid=categoryid,childcid=childid)

    if sortid == '1':
        goods = goods.order_by('-productnum')
    elif sortid == '2':
        goods = goods.order_by('price')
    elif sortid == '3':
        goods = goods.order_by('-price')


    data={
        'foodtypes':foodtypes,
        'goods':goods,
        'categoryid': categoryid,
        'childid': childid,
        'childList':childList

    }
    return render(request,'market/market.html',context=data)


def cart(request):      # 购物车
    return render(request,'cart/cart.html')


def mine(request):      # 我的
    return render(request,'mine/mine.html')