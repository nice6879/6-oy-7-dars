from django.shortcuts import render, redirect, get_object_or_404
from .models import Cotegory, Product, About
from .forms import ProductForm

def home(request):
    product = Product.objects.all()
    cotegory = Cotegory.objects.all()
    return render(request, 'home.html', context={'product':product, 'cats':cotegory})
    

def cotegory(request, id):
    cot = get_object_or_404(Cotegory, id=id)
    product = cot.products.all()
    cotegory = Cotegory.objects.all()
    return render(request, 'home.html', context={'product':product, 'cats':cotegory})


def detail(request, id):
    product = get_object_or_404(Product, id=id)
    cotegory = Cotegory.objects.all()

    return render(request, 'detail.html', context={'product':product, 'cats':cotegory})


def about(request):
    about = About()
    cotegory = Cotegory.objects.all()


    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('about')
    return render(request, 'about.html', context={'about':about, 'cats':cotegory})



def product_create(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'crud.html', context={'form':form})


def product_update(request, id):
    updat = get_object_or_404(Product, id=id)

    form = ProductForm(instance=updat)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=updat)  
        if form.is_valid():
            form.save()
            return redirect('detail', id=updat.id)

    return render(request, 'crud.html', context={'form':form})


def product_delete(request, id):
    delet = get_object_or_404(Product, id=id)
    delet.delete()
    return redirect('home')
