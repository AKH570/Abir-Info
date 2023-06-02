from django.shortcuts import render
from django.http import HttpResponse
from . models import home,experience,Educations,References,myPortfolio,ExtraAct,Contact
from datetime import date
from django.contrib import messages

# Create your views here.


def myhome(request):
    info=home.objects.all()
    return render(request,'home/home.html',{'info':info})
def about(request):
    about=home.objects.all()
    info=home.objects.all()
    return render(request,'home/about.html',{'abt':about,'info':info})
def skill(request):
    info=home.objects.all()
    return render(request,'home/skill.html',{'info':info})
def myexp(request):
    info=home.objects.all()
    experiences=experience.objects.all()
    info=home.objects.all()
    return render(request,'home/experience.html',{'exp':experiences,'info':info})
def educations(request):
    info=home.objects.all()
    education=Educations.objects.all()
    return render(request,'home/educations.html',{'edu':education,'info':info})

#alsdjfaldskf
def contactme(request):
    info=home.objects.all()
    contact=home.objects.all()
    if request.method=='POST':
        nm=request.POST.get('name') #this get() attribute name is from html name attribute
        mail=request.POST.get('email')
        sub=request.POST.get('subject')
        mesg=request.POST.get('message')

        con=Contact(name=nm,email=mail,subject=sub,message=mesg)
        con.save()
        messages.success(request,'Your profile updated successfully')
    return render(request,'home/contact.html',{'cont':contact,'info':info})

'''
def myskills(request):
    info=home.objects.all()
    sk=skills.objects.all()
    return render(request,'home/skill.html',{'sk':sk,'info':info})
'''
   #this is for my ref.... 

def myreference(request):
    info=home.objects.all()
    ref=References.objects.all()
    return render(request,'home/reference.html',{'ref':ref,'info':info})

#this file is for myportfolio
def myportfolio(request):
    info=home.objects.all()
    portfolio=myPortfolio.objects.all()
    return render(request,'home/portfolio.html',{'portfo':portfolio,'info':info})


def OthersInfo(request):
   info=home.objects.all()
   otherinfo=ExtraAct.objects.all()
   return render(request,'home/extra.html',{'ex':otherinfo,'info':info})

def myGallery(request):
    return render(request,'home/gallery.html')
