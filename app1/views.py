from django.shortcuts import render
from django.http      import HttpResponse

# Create your views here.

def home_page(request):
  #return HttpResponse('====== 1 ========')
  return render(request, 'app1/home_page.html')
