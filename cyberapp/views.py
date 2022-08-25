from django.shortcuts import render

# Create your views here.
def fnIndex(request):
    return render(request,'index.html')

def adhun(request):
    return render(request,'adhun.html')