from django.shortcuts import render



def home(request):
    pass

def dashboard(reqest):
    return render(reqest, 'main/template.html')