
from django.shortcuts import render, redirect
from django.views.generic.base import View

from blog.forms import ContactForm
from blog.models import Tur, Article


def index(request):
    return render(request,'blog/index.html')
def contact(request):
    return render(request,'blog/contact.html')
def menu(request):
    return render(request,'blog/menu.html')
def blog(request):
    return render(request,'blog/blog.html')
def reserv(request):
    return render(request,'blog/reserv.html')
def timetable(request):
    return render(request,'blog/timetable.html')
def reviews(request):
    return render(request,'blog/reviews.html')
class MoviesView(View):

    def get(self,request):
        tur=Tur.objects.all()
        return render(request,"blog/Tur_menu.html",{"Tur_menu":tur})

class TursView(View):

    def get(self, request):
        tur = Tur.objects.all()
        return render(request, "blog/reserv.html", {"reserv": tur})

class BlogView(View):
     def get(self, request):
        article = Article.objects.all()
        return render(request, "blog/blog.html", {"blog": article})
class IndexView(View):
    def get(self, request):
        article = Article.objects.all()
        return render(request, "blog/index.html", {"index": article})
class TurDetalView(View):
    def get(self, request,pk):
        tur = Tur.objects.get(id_tur=pk)
        return render(request,"blog/Tur_det.html",{"tur":tur})
class AddReviews(View):
    def post(self,request,pk):
        print(request.POST)
        return  redirect("reviews/")

def contacts(request, form=None):
    context={}
    if request.method=='POST':
        pass
    else:
        form = ContactForm()
    context['form']=form
    return render(
        request,
        'contact.html',
        context=context
    )