from django.shortcuts import render

# Create your views here.
def basic_detail(request):
    return render(request,'profile/basic_detail.html')
def location(request):
    return render(request,'profile/location.html')
def education(request):
    return render(request,'profile/education.html')
def experience(request):
    return render(request,'profile/experience.html')
def language(request):
    return render(request,'profile/language.html')
def resume(request):
    return render(request,'profile/resume.html')