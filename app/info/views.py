from django.shortcuts import get_object_or_404, redirect, render
from .models import Employees, Position
from .forms import CreateEmployess,EditEmployess
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required()
def list(request):
    
    employess = Employees.objects.all()
    return render(request, "info/list.html", {"bussiness":employess})

@login_required()
def create(request):

    if request.method == "POST":
        form = CreateEmployess(request.POST)

        if form.is_valid():
            form.save()
            return redirect("list")
    else:
        form = CreateEmployess()

    return render(request, "info/create.html",{
        "form":form})    

def edit(request, id):
    user = get_object_or_404(Employees, pk=id)
    if request.method == "POST":
        form = EditEmployess(request.POST, instance=user)
        form.save()
        return redirect("list")
    else:
        form = EditEmployess(instance=user)

    return render (request, "info/edit.html", {
        "form":form
        })

def logsuc(request):
    return render(request, "account/logout.html")


def search(request):
   
    if "q" in request.GET and request.GET["q"] != "":
        q = request.GET['q']
        calisanlar = Employees.objects.filter(name__contains=q).order_by("startdate")
    else:
        return redirect("list")

    return render(request,'info/search.html',{
        'calisanlar': calisanlar,
   })

@login_required()
def home(request):
    kullanıcı = Employees.objects.all()
    sayisi = len(kullanıcı)
    salarys = Employees.objects.values_list('salary',flat=True)

    salaryy = sum(salarys)
    salar = salaryy / sayisi
    salary = round(salar, 2)
    
    
        

    return render(request, "info/home.html",{"sayi":sayisi,"maas":salary})

