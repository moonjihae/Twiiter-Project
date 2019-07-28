from django.shortcuts import render
from twitter.models import Twit
from .forms import UploadFileForm
from django.http import HttpResponseRedirect

# Create your views here.
def feed(request):
    posts=Twit.objects.all()
    return render(request,'feed.html',{'posts':posts})

count=0
def play2(request):

    global count
    count+=1
    user='문지해'
    diary=['빨래하기-20190717','공공즈 브이앱 보기-20190716','장보기-20190718']
    return render(request,'play2.html',{'name':user,'cnt':count,'diary':diary})

def my_profile(request):
    return render(request,'profile.html')

def fail(request):
    return render(request,'fail.html')

def detail_feed(request,pk):
    posts=Twit.objects.get(pk=pk)
    return render(request,'detail_feed.html',{'feed':posts})

def post(request):
     if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
        return render(request,'profile.html')
     else:
        form = UploadFileForm()
     return render(request, 'upload_doc.html', {'form': form})    
   