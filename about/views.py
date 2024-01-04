from django.shortcuts import render
from . models import About, Skills, Education, Experience 
# Create your views here.

def home(request):
    #f = About.objects.all()
    #print (f)
    #print (f[0].name)


    about = About.objects.last()
    coding_skills = Skills.objects.filter(type='Coding')
    design_skills = Skills.objects.filter(type='Design')
    education = Education.objects.all()
    experience = Experience.objects.all()


    return render (request, 'home.html',{
    "about":about ,  
    'coding_skills':coding_skills ,
    'design_skills':design_skills ,
    'education':education,
    'experience':experience,



        })