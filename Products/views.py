from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Categorie,Product,Order
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ProductAddForm
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
item = []
wishlist = []
# Create your views here.

class HomeListView(ListView):
    model = Product
    template_name = 'Products/home.html'
    queryset = Product.objects.all()[:6]
    context_object_name = 'Products'

class CategoryListView(ListView):
    model = Categorie
    template_name = 'Products/category.html'
    context_object_name = 'categories'

    def Meta(self):
        my_car = self.request.session['user_id']

def CategoryByProductsView(request, id):
    products = Product.objects.filter(CategoryId=id)
    # paginator = Paginator(products, 6) # Show 25 contacts per page.
    # page_number = request.GET.get('page')
    # products = paginator.get_page(page_number)
    context = {'products':products}
    return render(request, 'Products/products.html', context)

class ProductListView(ListView):
    model = Product
    template_name = 'Products/products.html'
    context_object_name = 'products'
    paginate_by = 6

class ProductDetailView(DetailView):
    def get(self, request, *args, **kwargs):
        book = get_object_or_404(Product, pk=kwargs['pk'])
        request.session['ProductId'] = book.id
        request.session['Image'] = book.Image.url
        context = {'book': book}
        return render(request, 'Products/product_detail.html', context)

    def post(self, request, *args, **kwargs):
        form = ProductAddForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('Name')
            price = form.cleaned_data.get('Price')
            color = form.cleaned_data.get('Color')
            size = form.cleaned_data.get('Size')
            quantity = form.cleaned_data.get('Quantity')
            image = request.session['Image']
            productId = request.session['ProductId']
            userId = request.session['user_id']
            data={
                'Name' : name,
                'ProductId' : productId,
                'UserId' : userId,
                'Price' : price,
                'Color' : color,
                'Size' : size,
                'Quantity' : quantity,
                'Image' : image
            }
        if 'cart' in request.POST:
            if str(data["Quantity"]) != str(0):
                item.append(data)
                return redirect('cart')
            else:
                messages.warning(request, 'Quantity must be greater than 0!')
                return HttpResponseRedirect('/products/'+str(data["ProductId"])+'/product-detail')
        elif 'Wishlist' in request.POST:
            if len(wishlist) > 0 :
                for x in str(len(wishlist)):
                    # print(wishlist[int(x)-1]["ProductId"])
                    if data["ProductId"] is wishlist[int(x)-1]["ProductId"]:
                        return redirect('my-wishlist')
                    else:
                        wishlist.append(data)
            else:
                wishlist.append(data)
            return redirect('my-wishlist')
        return render(request, 'Products/product_detail.html', {'some_flag': True})
        

class OrderListView(LoginRequiredMixin,ListView):
    model = Order
    template_name = 'Products/orders.html'
    context_object_name = 'Orders'

    def get_queryset(self):
        user_id = self.request.session['user_id']
        orderdata = Order.objects.filter(UserId = user_id)
        return orderdata

def cart(request):
    if request.method == 'GET':
        context = {'items': item}
        return render(request, 'Products/cart.html', context)

    if request.method == 'POST':
        product = Product
        user = []
        for i in range(len(item)):
            item[i]['Image'] = item[i]['Image'].replace('/media/images','/images')
            
            # Insert in the database
            Order.objects.create(Name = item[i]['Name'], 
                                 ProductId= Product.objects.filter(pk = item[i]['ProductId']).first(),
                                 UserId =  User.objects.filter(pk = item[i]['UserId']).first(),
                                 Color = item[i]['Color'],
                                 Size = item[i]['Size'],
                                 Quntity = item[i]['Quantity'],
                                 Price = item[i]['Price'],
                                 GrandTotal = (int(item[i]['Price']) * int(item[i]['Quantity'])),
                                 Image = item[i]['Image'])
        item.clear()
        return redirect('my-orders')
    return render(request, 'Products/cart.html',{'items':item})

def Wishlist(request):
    context = {'wishlist': wishlist}
    return render(request, 'Products/wishlist.html', context)

def DeleteItem(request,id):
    for i in range(len(item)):
        if id is i+1: 
            del item[i]
    return redirect('cart')

def DeleteWishlist(request,id):
    for i in range(len(wishlist)):
        if id is i+1: 
            del wishlist[i]
    return redirect('my-wishlist')