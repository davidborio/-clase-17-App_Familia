from django.shortcuts import render
from django.http import HttpResponse
from familiares.models import Familiar
import datetime


def saludo(request,nombre, apellido, edad):
    context ={
        "nombre":nombre ,
        "apellidos" :apellido,
        "edad" : edad    }

    return render(request,"familiares/index.html",context)

def familia(request):
    context ={
        "nombres":["David", "Mica", "Anto", "Edgardo", "Teresa"] ,
        "apellidos" : ["Borio","Paulos"],        
    }
    return render(request,"familiares/index.html",context)

def mostrar_familia(request):
    familia=Familiar.objects.all()
    return render(request,"familiares/index.html",{"familia":familia})

def mostrar_familia_tabla(request):
    familiar1=Familiar(nombre="Antonella",edad=28,fecha_nac=datetime.date(1994,5,3),parentezco="Hermana")
    familiar1.save()
    familiar2=Familiar(nombre="Micaela",edad=32,fecha_nac=datetime.date(1991,6,22),parentezco="Hermana")
    familiar2.save()
    familiar3=Familiar(nombre="Teresa",edad=61,fecha_nac=datetime.date(1962,4,28),parentezco="Mamá")
    familiar3.save()
    familiar4=Familiar(nombre="Elvio Edgardo",edad=71,fecha_nac=datetime.date(1952,1,13),parentezco="Papá")
    familiar4.save()

    context={"familiar1":familiar1,"familiar2":familiar2,"familiar3":familiar3,"familiar4":familiar4}
    return render(request,"familiares/index.html",context)


# Create your views here.
