from django.contrib import admin
from .models import Post,Infomation_Post,List_Post,Sample_Post,request_text
from django.contrib import admin

admin.site.register(Post)
admin.site.register(Infomation_Post)
admin.site.register(Sample_Post)
admin.site.register(List_Post)
admin.site.register(request_text)


