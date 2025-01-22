from django.shortcuts import render,redirect

# Create your views here.
def basic_detail(request):
    if (request.method == 'POST'):
        data = request.POST
        print(data)
        return redirect('complete_profile:resume')
    return render(request,'profile/complete_detail.html')


def resume(request):
    return render(request,'profile/resume.html')

def skip(request):
    return redirect('dashboard:home')