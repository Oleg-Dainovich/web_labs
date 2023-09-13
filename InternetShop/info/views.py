from django.shortcuts import render

def about_us_page(request):
    return render(request, 'info/about_us.html')


# Create your views here.
