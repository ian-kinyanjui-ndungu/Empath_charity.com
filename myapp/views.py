from django.shortcuts import render

# Create your views here.
def home (request):
    return render(request, 'index.html')

def custom_404 (request, exception):
    return render(request, '404.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request, 'contact.html')

def donation(request):
    return render(request, 'donation.html')

def event(request):
    return render(request, 'event.html')

def feature(request):
    return render(request, 'feature.html')

def service(request):
    return render(request,'service.html')

def team(request):
    return render(request,'team.html')

def testimonial(request):
    return render(request, 'testimonial.html')


