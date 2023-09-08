from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import ProductForm
from .models import Product 

# Create your views here.


def index(request):
    products = Product.objects.all()
    print(products)  # Agrega este mensaje de depuración
    return render(
        request,
        'index.html',
        context={'products': products}
    )

def detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    return render(
        request, 
        'detail.html',
        context={ 'product': product})
    
def form(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/products')
    else:
        form = ProductForm()

    return render(
        request,
        'Product_from.html',
        {'form': form}
    )