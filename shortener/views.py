from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .forms import SubmitUrlForm
from .models import KirrURL

# Create your views here.

def home_view_fbv(request, *args, **kwargs):
    if request.method == "POST":
        print(request.POST)
    return render(request, "shortener/home.html",{})

class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form=SubmitUrlForm()
        context={
            "form":the_form
        }
        return render(request, "shortener/home.html",context)
    
    def post(self, request, *args, **kwargs):
        form=SubmitUrlForm(request.POST)
        context={
            "form":form
        }
        template="shortener/home.html"

        if form.is_valid():
            new_url=form.cleaned_data.get("url")
            obj, created=KirrURL.objects.get_or_create(url=new_url)
            context["object"] = obj
            context["created"] = created
            context["shortcode"] = obj.shortcode
            if created:
                template="shortener/success.html"
            else:
                template="shortener/already-exists.html"
        else:
            context["shortcode"] = ""
    
        return render(request, template ,context)
        
class URLRedirectView(View):
   def get(self, request, shortcode=None, *args, **kwargs):
        try:
            kirr_url = KirrURL.objects.get(shortcode=shortcode)
        except KirrURL.DoesNotExist:
            return HttpResponseNotFound("Shortcode not found.")
        return redirect(kirr_url.url)

