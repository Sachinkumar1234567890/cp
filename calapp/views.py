from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
import math
from django.contrib.auth.models import User
from django.core.paginator import Paginator


# Create your views here.
def getfood(request):
    data=foodModel.objects.all()
    paginator=Paginator(data,3)
    page=request.GET.get("pg")
    data=paginator.get_page(page)
    return render(request,'index.html',{'data':data})


def register(request):
    registered= False
    if request.method == 'POST':
        form=register_form(request.POST,request.FILES)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            form.save()
            registered=True
            redirect('/')
    else:
        form=register_form()
    return render(request,'register.html',{'form':form,'registered':registered})

def newfood(request):
    if request.method == "POST":
        form=newfoodform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = newfoodform()
    return render(request,'newfood.html',{'form':form})

def addcalori(request):
    data=foodModel.objects.all()
    data1=dailycalory.objects.all()
    if request.method == "POST":
        food=request.POST.get("food")
        qty=int(request.POST.get("qty"))
        for i in data:
            if i.name==food:
                fname=i.name
                ftype=i.type
                fqty=i.quantity*qty
                fprotein=i.protein*qty
                fcarbs=i.carbs*qty
                ffat=i.fat*qty
                fnutrients=i.nutrients*qty
                fvitamins=i.vitamins 
                insert_values=dailycalory(dname=fname,dtype=ftype,dquantity=fqty,dprotein=fprotein,dcarbs=fcarbs,dfat=ffat,dnutrients=fnutrients,dvitamins=fvitamins)
                print(type(insert_values))
                insert_values.save()
        data1=dailycalory.objects.all()
    resqty=0
    resprotein=0
    rescarbs=0
    resfat=0
    resnutrients=0
    for j in data1:
        resqty+=j.dquantity
        resprotein+=j.dprotein
        rescarbs+=j.dcarbs
        resfat+=j.dfat
        resnutrients+=j.dnutrients
    return render(request,'addcalori.html',{'data1':data1,'data':data,'resqty':resqty,'resprotein':round(resprotein,1),'rescarbs':rescarbs,'resfat':resfat,'resnutrients':resnutrients})

def deletecal(request,pk):
    data1=dailycalory.objects.get(id=pk)
    data1.delete()
    return redirect('addcalori')

def editcal(request,pk):
    if request.method == "POST":
        res=dailycalory.objects.get(id=pk)
        data=foodModel.objects.get(name=res.dname)
        form=editfoodform(request.POST,instance=res)
        if form.is_valid():
            # ???????
            dname=res.dname
            dtype=res.dtype
            dquantity=res.dquantity
            dprotein=data.protein*res.dquantity
            dcarbs=data.carbs*res.dquantity
            dfat=data.fat*res.dquantity
            dnutrients=data.nutrients*res.dquantity
            dvitamins=data.vitamins
            insert_values=dailycalory(dname=dname,dtype=dtype,dquantity=dquantity,dprotein=dprotein,dcarbs=dcarbs,dfat=dfat,dnutrients=dnutrients,dvitamins=dvitamins)
            
            insert_values.save()
            res.delete()
            # ??????????
            return redirect('addcalori')
    res=dailycalory.objects.get(id=pk)
    form=editfoodform(instance=res)
    return render(request,'editcal.html',{'res':res,"form":form})

def detailfood(request,pk):
    data=foodModel.objects.get(id=pk)
    is_fav = False
    if data.fav.filter(id=request.user.id).exists():
        is_fav=True
    fav_food= is_fav
    return render(request,'detailfood.html',{'data':data,'fav_food':fav_food})

def fav_page(request,pk):
    var=get_object_or_404(foodModel,id=request.POST.get('food'))
    if var.fav.filter(id=request.user.id).exists():
        var.fav.remove(request.user)
    else:
        var.fav.add(request.user)
    return redirect('detail',pk=pk)

def favorite_page(request):
    data=foodModel.objects.filter(fav=request.user)
    return render(request,'favorite.html',{'data':data})





    




