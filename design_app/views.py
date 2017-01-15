from django.shortcuts import render

# Create your views here.

def index(request):
    template = 'pages/index.html'
    var = {}
    return render(request, template, var)
