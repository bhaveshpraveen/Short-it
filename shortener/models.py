from django.db import models
from .utilities.base62 import encode, base_decode




class shortit(models.Model):
    url = models.URLField(unique=True, null=False)
    code = models.CharField(max_length=16, unique=True, null=False, default="")
    updated = models.DateTimeField(auto_now=True)
    notes = models.TextField(default="Nothing to add here")

    def save(self, *args,**kwargs):
        Here
        # When using model managers to modify data, this if statement will make sure that a copy of the same url is not added
        if self.url in shortit.objects.values_list('url', flat=True):
            print(shortit.objects.all())
            print('Already Exists')

        # Since we are using the id to create the slug, using count+1 assuming that it will the be the id of the next object
        else:
            print('Inside else')
            count = shortit.objects.count()
            self.code = encode(count+1)
            super(shortit, self).save(*args, **kwargs)


    def __str__(self):
        return str((self.id, self.url, self.code))


    def __repr__(self):
        return str(self)


