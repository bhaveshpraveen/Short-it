from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from shortener.utilities.base62 import encode, base_decode
from django.template import Template, Context, loader
from .models import shortit


class homepage(View):
    def get(self, request, *args, **kwargs):
       return render(request, 'shortener/index.html', {})

    def post(self, request, *args, **kwargs):
        print('request', request)
        print('args {}\n kwargs'.format(args, kwargs))
        return render(request, 'shortener/index.html', {})
        #obj, created = shortit.objects.get_or_create(url=link)





class redirect(View):
    def get(self, request, slug,  *args, **kwargs):
        # checks if the slug is present, if present will redirect it to that page else will show 404 error
        id1 = base_decode(slug)
        # If the slug is not part of the database return a 404 error page
        obj = get_object_or_404(shortit, id__iexact=id1)
        return HttpResponseRedirect(obj.url)