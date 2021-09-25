from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Doubt(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='doubt_pics', null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
	    return reverse('doubt-detail', kwargs = {'pk': self.pk})

class Answer(models.Model):
	doubt = models.ForeignKey(Doubt, on_delete=models.CASCADE)
	votes = models.IntegerField(default=0)
	content = models.TextField()
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='answer_pics', null=True, blank=True)

	def get_absolute_url(self):
	    return reverse('doubt-detail', kwargs = {'pk': self.doubt.pk})