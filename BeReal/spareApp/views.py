from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect

from django.urls import reverse

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import *

from .forms import *
from .filters import *
def index(request):
    return render(request,'spare/index.html')

def category(request):
    category=Category.objects.filter()
    context ={'category':category}
    return render(request,'spare/category.html',context)

def categoryFilter(request,categ):
   if (Category.objects.filter(category=categ)):
      Category_name=Category.objects.filter(category=categ).first()
      products= Product.objects.filter(category )
      context = {'products':products,'Category_name':Category_name}
      return render(request,'spare/products.html',context)
   else:
      messages.warning={request,'No such category'}
      return redirect('spare/category.html')



def home(request):
    Products = Product.objects.all().order_by('-id')
    Product_filters = ProductFilter(request.GET,queryset = Products)
    #query set
    Products = Product_filters.qs
    return render(request,'spare/home.html',{'products':Products,'product_filters':Product_filters})


@login_required
def receipt(request):
    sales = Sale.objects.all().order_by('-id')
    return render(request,'spare/receipt.html',{'sales':sales})

   
@login_required
def product_detail(request,product_id):
   product =Product.objects.get(id = product_id)
   return render(request,'spare/product_detail.html',{'product':product})

def receipt_detail(request,receipt_id):
   receipt = Sale.objects.get(id = receipt_id)
   return render(request,'spare/receipt_detail.html',{'receipt':receipt})
   

def all_sales(request):
   sales = Sale.objects.all()   
   total = sum([items.amount_received for items in sales])
   change = sum([items.get_change() for items in sales])
   net = total - change
   return render(request,'spare/all_sales.html',{'sales':sales,'total':total,'change':change,'net':net})

   
@login_required
def issue_item(request,pk):
   issued_item = Product.objects.get(id = pk)
   sales_form = SaleForm(request.POST)

   if request.method == 'POST' :
      if sales_form. is_valid():
         new_sale = sales_form.save(commit=False)
         new_sale.part_purchased = issued_item
         new_sale.unit_price = issued_item.unit_price
         new_sale.save()
         
         # keeping track of the stock remaining after sale
         issued_quantity = int(request.POST['quantity'])
         issued_item.total_quantity -= issued_quantity
         issued_item.save()

         print(issued_item.part_name)
         print(request.POST['quantity'])
         print(issued_item.total_quantity)

         return redirect('receipt')
   return render(request,'spare/issue_item.html',{'sales_form': sales_form })



def add_to_stock(request,pk):
    issued_item = Product.objects.get(id = pk)
    form = AddForm(request.POST)
   
    if request.method == 'POST':
      if form.is_valid():
         added_quantity = int(request.POST['received_quantity'])
         issued_item.total_quantity += added_quantity
         issued_item.part_number = '1'
         issued_item.save()
         #To add to the remaining stock quantity is reduced
         print (added_quantity)
         print(issued_item.total_quantity)
         return redirect('home')
    return render(request,'spare/add_to_stock.html',{'form':form})


def delete_product(request,product_id):
   delete_product = Product.objects.get(id=product_id)
   delete_product.delete()
   return HttpResponseRedirect(reverse('home'))
   

# Create your views here.
