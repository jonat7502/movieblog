from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.shortcuts import render

from .models import Product

# Create your views here.
def store(request):
    return render(request, "base.html")

def get_now(request):
    now = datetime.datetime.now()
    return render(request, "base.html", {"current_date": now})



def product(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})
