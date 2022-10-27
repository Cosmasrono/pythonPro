""" from django.db import models
import accounts.models


class members(models.Model):
    firstName=models.CharField(max_length=255)
    secondName=models.CharField(max_length=255)
    foo = accounts.models.ReporterProfile()
 
# Create your models here. """
""" from django.db import models
import collections

class ReporterProfile(models.Model):

    def published_articles_number(self):
        num = collections.models.Report.objects.filter(reporterprofile=self.id).count()
        return num """