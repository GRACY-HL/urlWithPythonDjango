from django.conf import settings
from django.db import models
from django_hosts.resolvers import reverse


from .utils import code_generator, create_shortcode
from .validators import validate_url


SHORTCODE_MAX=getattr(settings, "SHORTCODE_MAX", 15)

class KirrURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main=super(KirrURLManager, self).all(*args,**kwargs)
        qs=qs_main.filter(active=True)
        return qs

        
class KirrURL(models.Model):
    url=models.CharField(max_length=220,validators=[validate_url])
    shortcode=models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    updated=models.DateTimeField(auto_now=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=True)

    objects=KirrURLManager()
    #some_random=KirrURLManager()

    
    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode=="":
            self.shortcode=create_shortcode(self)
        super(KirrURL, self).save(*args, **kwargs)    
    
    def __str__(self):
        return str(self.url)
    def __unicode__(self):
        return str(self.url)
    
    def get_short_url(self):
        return f"/{self.shortcode}"