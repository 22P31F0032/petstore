from django.shortcuts import render
from . models import petorders
# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def angelfish(request):
    return render(request, 'angelfish.html')
def angora(request):
    return render(request, 'angora.html')
def bobtail(request):
    return render(request, 'bobtail.html')
def booknow(request):
    return render(request, 'booknow.html')
def cocktail(request):
    return render(request, 'cocktail.html')
def contact(request):
    return render(request, 'contact.html')
def german(request):
    return render(request, 'german.html')
def golden(request):
    return render(request, 'golden.html')
def goldfish(request):
    return render(request, 'goldfish.html')
def greyparrot(request):
    return render(request, 'greyparrot.html')
def himalayan(request):
    return render(request, 'himalayan.html')
def husky(request):
    return render(request, 'husky.html')
def index(request):
    return render(request, 'index.html')
def login(request):
    return render(request, 'login.html')
def polish(request):
    return render(request, 'polish.html')
def registration(request):
    return render(request, 'registration.html')

def orders(request):
    if request.method=="POST":
       Breed_name=request.POST['Breed_name']
       color=request.POST['color']
       cus_name = request.POST['cus_name']
       email=request.POST['email']
       phone=request.POST['phone']
       inst= petorders(Breed_name,color,cus_name,email,phone)
       inst.save()
    return render(request, 'orders.html')
def show_orders(request):
    data=petorders.objects.all()
    return render(request, 'show_orders.html', {'data':data})