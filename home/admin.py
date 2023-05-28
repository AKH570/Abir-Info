from django.contrib import admin
from . models import home,experience,Educations,skills,References,myPortfolio,ExtraAct,Contact

# Register your models here.
class HomeAdmin(admin.ModelAdmin):
    list_display=['myname','title','about_me','objective','email','address','phone','remarks','my_image']
admin.site.register(home,HomeAdmin)

class ExperienceAdmin(admin.ModelAdmin):
    list_display=['id','designation','field_name','company_name','responsibility','from_date','to_date','totalyr','remarks']
admin.site.register(experience,ExperienceAdmin)

class EduAdmin(admin.ModelAdmin):
    list_display=['id','degee_name','subject','school_name','start_dt','end_dt','gpa','imgs','cert_imgs']
admin.site.register(Educations,EduAdmin)

class SkillAdmin(admin.ModelAdmin):
    list_display=['id','s_name','portfolio_name','port_file','port_img','skill_range']
admin.site.register(skills,SkillAdmin)

class RefAdmin(admin.ModelAdmin):
    list_display=['id','name','positions','org_name','pic','comments']
admin.site.register(References,RefAdmin)

class PortfolioAdmin(admin.ModelAdmin):
    list_display=['name','portfile','portimg']
admin.site.register(myPortfolio,PortfolioAdmin)

@admin.register(ExtraAct)
class ExtraActAdmin(admin.ModelAdmin):
    list_display=['name','details','img']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=['name','email','subject','message']