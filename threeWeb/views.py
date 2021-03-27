from django.views.generic import View
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Post,Infomation_Post,List_Post,Sample_Post,request_text
from django.forms import ModelForm
from .forms import request_Form
from django.shortcuts import get_object_or_404



class IndexView(View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.order_by("-id")
        Infomation_data = Infomation_Post.objects.order_by("-id")
        Sample_data = Sample_Post.objects.order_by("-id")
        return render(request, 'threeWeb/index.html', {
            'post_data': post_data,
            'Sample_data': Sample_data,
            'Infomation_data': Infomation_data,
        })


class List_View(View):
    def get(self, request, *args, **kwargs):
        List_data = List_Post.objects.order_by("-id")
        return render(request, 'threeWeb/list.html', {
            'List_data': List_data,
        })

class Plan_View(View):
    def get(self, request, *args, **kwargs):
        List_data = List_Post.objects.order_by("-id")
        return render(request, 'threeWeb/plan.html', {
            'List_data': List_data,
        })

class request_View(View):
    def get(self, request, *args, **kwargs):
        List_data = List_Post.objects.order_by("-id")
        return render(request, 'threeWeb/request.html', {
            'List_data': List_data,
        })


class contact_View(View):
    def get(self, request, *args, **kwargs):
        List_data = List_Post.objects.order_by("-id")
        return render(request, 'threeWeb/contact.html', {
            'List_data': List_data,
        })

        
def request_next(request, *args, **kwargs):
    if request.method == "POST":
        form = request_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:   
        form = request_Form()
    return render(request, 'threeWeb/request_next.html', {'form': form })

