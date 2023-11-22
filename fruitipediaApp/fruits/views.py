from django.shortcuts import render, redirect

# Create your views here.
from fruitipediaApp.fruits.models import Fruit
from fruitipediaApp.fruits.forms import CategoryCreateForm


def index(request):
    return render(request, 'common/index.html')

def dashboard(request):
    fruits=Fruit.objects.all()
    context={
        'fruits': fruits
    }
    return render(request, 'common/dashboard.html', context)

def create_fruit(request):
    return render(request, 'fruits/create-fruit.html')

def details_fruit(request):
    return render(request, 'fruits/details-fruit.html')

def edit_fruit(request):
    return render(request, 'fruits/edit-fruit.html')

def delete_fruit(request):
    return render(request, 'fruits/delete-fruit.html')

def create_category(request):
    if request.method=='GET':
        form=CategoryCreateForm()
    else:
        form=CategoryCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context={
        'form': form
    }
    return render(request, 'categories/create-category.html', context)