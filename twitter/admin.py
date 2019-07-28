from django.contrib import admin

# Register your models here.
from twitter.models import Twit

admin.site.register(Twit)
from .models import UploadFileModel

# Register your models here.
admin.site.register(UploadFileModel)