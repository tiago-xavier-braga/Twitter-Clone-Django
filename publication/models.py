from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):

	title = models.CharField(
		max_length = 255,
		null = False,
		blank=False
		)
	body = models.TextField(
		null = False
		) 
	created = models.DateTimeField(
		auto_now_add=True
		)
	slug = models.SlugField(
		max_length=255, 
		unique=True
		)
	class Meta:
		ordering = ("-created",)
	
	def __str__(self):
		return self.title
    
	def get_absolute_url(self):
		return reverse("blog:detail", kwargs={"slug": self.slug})