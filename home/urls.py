from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.myhome, name='home'),
    path('about/',views.about, name='about'),
    path('skill/',views.skill, name='skill'),
    path('myexp/',views.myexp, name='experience'),
    path('educations/',views.educations, name='educations'),
    path('contact/',views.contactme,name='contact'),
    #path('skill/',views.myskills,name='skill'),
    path('ref/',views.myreference,name='reference'),
    path('portfolio/',views.myportfolio,name='portfolio'),
    path('others/',views.OthersInfo,name='others'),
    path('gallery/',views.myGallery,name='gallery')

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)