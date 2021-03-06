from django.db import models
from django.contrib.auth.models import User


# Create your models here.
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
	title = models.CharField(max_length = 200 , unique = True)
	slug = models.SlugField(max_length = 200 , unique = True)

	author = models.ForeignKey( User,
								on_delete = models.CASCADE,
								related_name='blog_posts'
								)
	
	
	content = models.TextField()

	updated_on = models.DateTimeField('Updated On',auto_now = True)
	created_on = models.DateTimeField('Published On',auto_now_add = True)

	status = models.IntegerField(choices= STATUS, default = 0)

	class meta:
		ordering = ['-created_on']

	def __str__(self):
		return self.title