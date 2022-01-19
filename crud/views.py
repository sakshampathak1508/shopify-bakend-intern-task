# from unicodedata import name
from django.shortcuts import render
import csv
from django.http import HttpResponseRedirect,HttpResponse
from .models import Product
# Create your views here.
def index(request):
    return render(request,'crud/index.html')

def view_prod(request):
    obj = Product.objects.all()
    params = {'prod':obj}
    return render(request,'crud/list.html',params)

def add_prod(request):
    if request.method == "POST":    
        prod_name = request.POST['prod_name']
        image = request.FILES['img']
        price = request.POST['price']
        brand = request.POST['brand']
        sc = request.POST['sc']
        category = request.POST['category']
        about = request.POST['about']
        obj = Product(name=prod_name,image=image,price=price,brand=brand,stock_count=sc,category=category,about=about)
        obj.save()
        return HttpResponseRedirect("/list")
    return render(request,'crud/add.html')

def edit_prod(request,id):
    obj = Product.objects.filter(id=id).first()
    if request.method == "POST":    
        prod_name = request.POST['prod_name']
        image = request.FILES['img']
        price = request.POST['price']
        brand = request.POST['brand']
        sc = request.POST['sc']
        category = request.POST['category']
        about = request.POST['about']
        obj.name = prod_name
        obj.image = image
        obj.price = price
        obj.brand = brand
        obj.stock_count = sc
        obj.category = category
        obj.about = about
        obj.save()
        return HttpResponseRedirect("/list")
    params = {'prod':obj}
    return render(request,'crud/edit.html',params)

def delete_prod(request,id):
    obj = Product.objects.filter(id=id).first()
    obj.delete()
    return HttpResponseRedirect("/list")

def export(request):
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['name','image','price','brand','stock count','category','about'])
    for obj in Product.objects.all().values_list('name','image','price','brand','stock_count','category','about'):
        writer.writerow(obj)

    response['Content-Disposition'] = 'attachment;filename="Products.csv"'
    return response