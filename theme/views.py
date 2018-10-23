from django.shortcuts import render

def home(request):
    return render(request, "home.html")
#def bootstrap(request):
#    return render(request, "bootstrap_page.html");