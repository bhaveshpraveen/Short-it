from django.db import models
from .utilities.base62 import encode, base_decode


class shortit(models.Model):
    url = models.URLField(unique=True, null=False)
    code = models.TextField(unique=True, null=False, default="")
    updated = models.DateTimeField(auto_now=True)
    notes = models.TextField(default="Nothing to add here")

    def save(self, *args, **kwargs):
        # When using model managers to modify data, this if statement will make sure that a copy of the same url is not added
        if self.url in shortit.objects.values_list('url', flat=True):
            print('Already Exists')

        # Since we are using the id to create the slug, using count+1 assuming that it will the be the id of the next object
        else:
            print('Inside else')
            obj = shortit.objects.latest('id')
            count = obj.id
            self.code = encode(count+1)
            super(shortit, self).save(*args, **kwargs)


    def __str__(self):
        return str((self.id, self.url, self.code))


    def __repr__(self):
        return str(self)

# Instead of the two methods below use reverse

    def get_short_url(self):
        link = self.code
        print('link being passed:', link)
        return link

    def get_url(self):
        link = "www.si.com:8000/{}".format(self.code)
        return link
