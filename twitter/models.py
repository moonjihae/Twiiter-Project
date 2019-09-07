from django.db import models
from django.conf import settings

# Create your models here.
class Twit(models.Model):
    member=models.CharField(max_length=20)  
    title=models.CharField(max_length=120)
    text=models.TextField()
    link=models.TextField()
    likes=models.BooleanField(default=False)


    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

# def user_path(instance, filename): #파라미터 instance는 Photo 모델을 의미 filename은 업로드 된 파일의 파일 이름
#     from random import choice
#     import string # string.ascii_letters : ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
#     arr = [choice(string.ascii_letters) for _ in range(8)]
#     pid = ''.join(arr) # 8자리 임의의 문자를 만들어 파일명으로 지정
#     extension = filename.split('.')[-1] # 배열로 만들어 마지막 요소를 추출하여 파일확장자로 지정
#     # file will be uploaded to MEDIA_ROOT/user_<id>/<random>
#     return '%s/%s.%s' % (instance.owner.username, pid, extension) # 예 : wayhome/abcdefgs.png

# class Photo(models.Model):
#     image = models.ImageField(upload_to = user_path) # 어디로 업로드 할지 지정
    
#     thumname_image = models.ImageField(blank = True) # 필수입력 해제
#     comment = models.CharField(max_length = 255)
#     pub_date = models.DateTimeField(auto_now_add = True) # 레코드 생성시 현재 시간으로 자동 생성
class UploadFileModel(models.Model):
    title = models.TextField(default='')
    file = models.FileField(null=True)


