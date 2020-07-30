from django.shortcuts import render
from twitter.models import Twit
from .forms import UploadFileForm
from django.http import HttpResponseRedirect
from twitter.twitter_crawling import crawling

# Create your views here.
def feed(request):
   #검색 내용 있으면 해당 피드만 출력 없으면 모든 피드 출력
    posts=Twit.objects.all().order_by('-title')
    q=request.GET.get('q',"")
    if q:
       posts=posts.filter(text__contains=q)
    return render(request,'feed.html',{'posts':posts,'q':q})
 
count=0
def play2(request):

    global count
    count+=1
    user='문지해'
    diary=['빨래하기-20190717','장보기-20190718']
    return render(request,'play2.html',{'name':user,'cnt':count,'diary':diary})

def my_profile(request):
    return render(request,'profile.html')

def fail(request):
    return render(request,'fail.html')

def detail_feed(request,pk):
    posts=Twit.objects.get(pk=pk)
    return render(request,'detail_feed.html',{'feed':posts})



def new_feed(request):
    
   if request.method == 'POST':  
      c=crawling()
   
      for i in range(0,len(c)):
         Twit.objects.get_or_create(
            member=c[i][2],      
            title=c[i][0],
            text=c[i][3],
            link=c[i][4]
         ) 
     
      print ("end")
     

      
   return render (request,'new_feed.html')

def likes(request):
    posts=Twit.objects.filter(likes=True)
    return render(request,'likes.html',{'likes':posts})

# def click_like(request):
#    pk=request.POST.get('pk',)
#    post = get_object_or_404(Twit, pk=pk)
#    post_like,post_like_created =  post.likes.update(user=request.user)
#    if not post_like_created:
#       post_like.delete()
#    return HttpResponse(json.dumps(context), content_type="application/json") 
def like(request):
   if request.method=='POST':
      twit_id=request.POST.get('pk',None)
      that_twit=Twit.object.get(pk=twit_id)
      if that_twit.likes.filter(ikes=True):
         that_twit.likes=False
         message="you disliked this"
      else:
         that_twit.likes=True
         message="you like this"
      context={'message':message}
      return HttpResponse(json.dumps(context),context_type='application/json')


