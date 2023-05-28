from django.db import models
from datetime import date

# Create your models here.

class home(models.Model):
    myname = models.CharField(max_length=200)
    title =models.CharField(max_length=300)
    about_me= models.TextField()
    objective=models.TextField()
    email=models.EmailField()
    address=models.CharField(max_length=300)
    phone=models.CharField(max_length=100)
    remarks=models.CharField(max_length=300)
    my_image=models.ImageField(upload_to='allpic')

    def __str__(self):
        return str(self.id)
    
class experience(models.Model):
    designation=models.CharField(max_length=100)
    field_name=models.CharField(max_length=150)
    company_name =models.CharField(max_length=200)
    responsibility=models.TextField(max_length=1000)
    from_date=models.DateField(auto_now_add=False,auto_now=False,blank=True)
    to_date=models.DateField(auto_now_add=True,blank=True)
    #odl_date =models.DateField(auto_now_add=False,auto_now=False,blank=True)
    remarks=models.DateField(auto_now_add=False,auto_now=False,blank=True)
    
    def __str__(self):
        return str(self.id)
    
    @property
    def totalyr(self):
        #presentdt=self.to_date
        if self.remarks==self.to_date:
            totalyr=self.to_date.year - self.from_date.year
        else:
            totalyr=self.remarks.year - self.from_date.year
        return totalyr

class Educations(models.Model):
    degee_name=models.CharField(max_length=50)
    subject=models.CharField(max_length= 100)
    school_name=models.CharField(max_length=100)
    start_dt=models.DateField(auto_now_add=False,auto_now=False,blank=True)
    end_dt=models.DateField(auto_now_add=False,auto_now=False,blank=True)
    gpa=models.CharField(max_length=50)
    imgs=models.ImageField(upload_to='school',blank=True,null=True)
    cert_imgs=models.ImageField(upload_to='certifications',blank=True,null=True)

    @property
    def ins_imgs(self):
        if self.imgs:
            return self.imgs.url
        return ''
    @property
    def cert_img(self):
        if self.cert_imgs:
            return self.cert_imgs.url
        return ''

class skills(models.Model):
    s_name=models.CharField(max_length=100)
    skill_range=models.IntegerField(blank=True)
    portfolio_name=models.CharField(max_length=100,blank=True)
    port_file=models.FileField(upload_to='vediofile',blank=True)
    port_img=models.ImageField(upload_to='portfolio',blank=True)

    def __str__(self):
        return str(self.s_name)

class References(models.Model):
    name=models.CharField(max_length=100)
    positions=models.CharField(max_length=150)
    email=models.EmailField(max_length=100)
    org_name=models.CharField(max_length=100)
    pic=models.ImageField(upload_to='refer_pic',blank=True)
    comments=models.TextField(max_length=500)

    def __str__(self):
        return str(self.id)

class myPortfolio(models.Model):
    name=models.CharField(max_length=150,blank=True)
    portfile=models.FileField(upload_to='portfoliofile',blank=True)
    portimg=models.ImageField(upload_to='portimg',blank=True)

    def __str__(self):
        return str(self.name)
    @property
    def my_portfolio(self):
        if self.portfile:
            return self.portfile.url
        return ''

class ExtraAct(models.Model):
    name=models.CharField(max_length=200)
    details=models.CharField(max_length=200)
    img=models.ImageField(upload_to='extrapic',blank=True)

    def __str__(self):
        return str(self.name)
    
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    subject=models.CharField(max_length=200)
    message=models.TextField(max_length=300)

    def __str__(self):
        return str(self.name)

