from django.db import models
from django.contrib.contenttypes.models import generic

"""
The Document model can generically relate to a model for querying.

In some cases this is simple--someone has signed a petition (class Petition). Use it!

In other cases its not so simple--someone has signed a weekly timeclock report which
contains dozens of clock-ins and clock-outs. There's no object to speak of, however, one
may still want to display whether a particular range has been signed. In this case, simply
create a placeholder object which represents this date-range, and use it.

eg:

	class TimeclockRange(models.Model):
		start_date = ...
		end_date = ...
		user = ...

Then link your Document to this object.

"""

class Document(models.Model):
	title = models.CharField(max_length=55)
	date_created = models.DateTimeField(editable=False)
	content_type = models.ForeignKey('contenttypes.ContentType',null=True,blank=True)
	object_pk = models.IntegerField(null=True,blank=True)
	author = models.ForeignKey('auth.User',null=True,blank=True)

class Signatory(models.Model):
	document = models.ForeignKey('Document')
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	auth_token = models.CharField(max_length=255) # last 4 of social, pet's name, etc.
	user = models.ForeignKey('auth.User',blank=True,null=True)
	date_signed = models.DateTimeField(editable=False)
