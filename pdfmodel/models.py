from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CustomerPdf(models.Model):
    pdf_file = models.FileField(upload_to="media", null=True, blank=True, default=None)
