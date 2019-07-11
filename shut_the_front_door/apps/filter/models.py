from ..login_reg.models import User
from django.db import models
from datetime import datetime
from django.contrib import messages

date = datetime.now()
# MODELS FOR FILTER APP
# Create your models here.

class KeywordManager(models.Manager):
    def keyword_validator(self, postData):
        errors = {}
        grab = Keyword.objects.filter(title_to_filter=postData['title_to_filter'])
        if len(postData['filter_end_date']) <= 0:
            errors['filter_end_date'] = "Please input a date"
        if postData['filter_end_date'] <= str(date):
            errors['filter_end_date'] = "Date cannot be in the past!"
        return errors

class Keyword(models.Model):
    user_id = models.ForeignKey(User, related_name="filterer")
    title_to_filter = models.CharField(max_length=255)
    genre_to_filter = models.CharField(null=True, blank=True, max_length=255)
    filter_end_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    query_data = models.TextField()

    objects = KeywordManager()

    def __repr__(self):
        return f"<Keyword object: {self.id}, ({self.title_to_filter}), ({self.genre_to_filter})>"