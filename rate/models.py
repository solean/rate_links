from datetime import datetime
from django.db import models

# Create your models here.
class Link(models.Model):
	title = models.CharField(max_length = 128, unique=True)
	url = models.URLField(max_length=256, unique=True)
	avg_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
	num_ratings = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	date_added = models.DateTimeField(auto_now_add=True, default=datetime.now())

	def as_dict(self):
		d = {'title': self.title,
			 'url': self.url,
			 'avg_rating': self.avg_rating,
			 'likes': self.likes,
			 'date_added': self.date_added.strftime('%c')
			}
		return d

	def __unicode__(self):
		return self.title