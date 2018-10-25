from django.db import models
from django.urls import reverse


class Contact(models.Model):

    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('bootstrap:bootstrap_list', kwargs={'pk': self.pk})
