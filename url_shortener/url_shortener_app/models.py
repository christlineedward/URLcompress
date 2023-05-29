from django.db import models

# Create your models here.
class URLMapping(models.Model):
    short_code = models.CharField(max_length=8, unique=True) # short code representing the URL mapping (8 ch max)
    long_url = models.URLField() # long URL to be shortened and mapped

    def __str__(self) -> str:
        return self.short_code #return the short code as the string representation of the instance