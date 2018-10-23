from django.db import models
from django.urls import reverse

class ContactList(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('bootstrap_page/', kwargs={'pk': self.pk})