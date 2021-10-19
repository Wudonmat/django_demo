from django.shortcuts import render

# Create your views here.
def cart(request):
    return render(request, "payment/cart.html")

def purchase(request):
    return render(request, "payment/purchase.html")

def complete(request):
    return render(request, "payment/complete.html")