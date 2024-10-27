from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=266)
    descriptions = models.TextField(max_length=500)
    difficulties = models.CharField(max_length=266, blank=True, null=True)
    solution = models.CharField(max_length=266, blank=True, null=True)
    link = models.CharField(max_length=266, blank=True, null=True)
    deployment_link = models.URLField(max_length=266, blank=True, null=True)  # New field for deployment link
    image = models.ImageField(upload_to='projects/%Y/%m/%d/', blank=True, null=True)
    
    def __str__(self):
        return self.title
