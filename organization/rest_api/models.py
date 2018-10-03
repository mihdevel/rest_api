from django.db import models
from django.contrib.auth.models import User

class words(models.Model):
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)  # settings.AUTH_USER_MODEL,
  word = models.CharField(max_length=200)
  date_add = models.DateField()
  
  def __str__(self):
    return self.word


class video(models.Model):
  title = models.CharField(max_length=200)
  url = models.CharField(max_length=100)
  
  def __str__(self):
    return self.title

class word_requests(models.Model):
  word_id = models.ForeignKey(words, on_delete=models.CASCADE)
  date_add = models.DateField()
  
  def __str__(self):
    return 'Word id:', self.word_id


class list_video(models.Model):
  video_id = models.ForeignKey(video, on_delete=models.CASCADE)
  word_request_id = models.OneToOneField(word_requests, on_delete=models.CASCADE)
  
  def __str__(self):
    return 'Word request id:', self.word_request_id