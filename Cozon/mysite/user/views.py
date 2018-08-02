from django.shortcuts import render,redirect,HttpResponse
from .models import User,ShopCart
from django.contrib.auth import login,authenticate,logout
from.models import Category,Picture,Product,ShopCartProduct,Address,Commentt
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
import ast,json

def index(request):
    categories=Category.objects.all().filter(parent_id=None).values()
    for lv1 in categories:
        lv1['children']=Category.objects.all().filter(parent_id=lv1['id']).values()
        for lv2 in lv1['children']:
            lv2['children'] = Category.objects.all().filter(parent_id=lv2['id']).values()
    banner=Picture.objects.all().filter(type=1)
    return render(request,'user/home.html',{
        'categories':categories,
        'ban':banner
    })



def sign_up(request):
    if request.method=='GET':
        return render(request,'user/register.html')
    else:
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        user = User.objects.create_user(username=username,email=email,password=password)
        if user is not None:
            return redirect('sign_in')
        else:
            return HttpResponse('失败')

def sign_in(request):
    if request.method=='GET':
        return render(request,'user/login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
                login(request, user)
                return HttpResponse('登录成功')
        else:
            return HttpResponse('用户不存在，请注册！')
def logoout(request):
    logout(request)
    return redirect('index')

def search(request):
    category_id=request.GET.get('category_id',0)
    keywords=request.GET.get('keywords','')
    if category_id:
        products = Product.objects.all().filter(category_id=category_id)
    elif keywords:
        products = Product.objects.all().filter(title__contains=keywords)
    else:
        products=None
    paginator=Paginator(products,2)
    page= request.GET.get('page',1)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    return render(request,'user/search.html',{
        'products':data,
        'category_id':category_id,
        'keywords':keywords,
        'has_prev':data.has_previous(),
        'has_next':data.has_next(),

    })

def detail(request):

    product_id = request.GET.get('product_id','')
    product = Product.objects.get(pk=product_id)
    return render(request,'user/introduction.html',{
        'product':product,

    })

def comment(request):
    color = request.POST['color']
    chicun = request.POST['chicun']
    content = request.POST['message']
    daa = Commentt.objects.create(color=color, chicun=chicun, content=content)
    return render(request, 'user/introduction.html', {
        'daa': daa
    })


def add_to_cart(request):
    product_id = request.POST.get('product_id')
    number = request.POST.get('num')
    cart = ShopCart.objects.get_or_create(user=request.user,defaults={'user_id': request.user.id})
    # 购物车对象cart
    res = cart[0].shopcartproduct_set.update_or_create(product_id=product_id, defaults={
        'product_id': product_id,

    })
    # 中间表对象res
    if res[1] :
        res[0].number = int(number)
    else:
        res[0].number += int(number)
    res[0].save()

    if res is not None:
        return HttpResponse('添加成功！')
    else:
        return HttpResponse("添加失败！")

def deleo(request):
    cid=request.GET.get('cid')
    ShopCartProduct.objects.get(pk=cid).delete()
    return redirect('show_cart')


def show_cart(request):
    try:
        cart = ShopCart.objects.get(user=request.user)
    except Exception:
        cart=None
    data = cart.shopcartproduct_set.all()
    con = cart.shopcartproduct_set.all().count()

    return render(request,'user/shopcart.html',{'cart':data,'con':con})


def pay(request):
        add = Address.objects.all().filter(user=request.user)
        sid = request.GET.get(('sid'))
        total = request.GET.get('total')
        sid1 = ast.literal_eval(sid)
        m1 = []
        for i in range(0, len(sid1)):
            sid1[i]['id'] = ast.literal_eval(sid1[i]['id'])
            m1.append(sid1[i]['id'])
        cart = ShopCart.objects.get(user=request.user)
        data = cart.shopcartproduct_set.filter(product_id__in=m1)
        con = cart.shopcartproduct_set.all().count()
        return render(request, 'user/pay.html', {'data': data, 'total': total,'con':con,'add':add})

def succe(request):
    cart = ShopCart.objects.get(user=request.user)
    sid = request.GET.get('sid')
    sid1 = ast.literal_eval(sid)
    con = cart.shopcartproduct_set.all().count()
    return render(request, 'user/success.html', {
        'sid1':sid1,
        'con':con
    })
# Create your views here.
def con(request):
    return render(request,'user/comment.html')

def selled(request):
    return render(request,'user/selled.html')