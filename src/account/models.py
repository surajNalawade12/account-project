# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# from pygments.lexers import get_lexer_by_name
# from pygments.formatters.html import HtmlFormatter
# from pygments import highlight

class Account(models.Model):

	GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female')
	)

	id = models.AutoField(primary_key=True)
	accountNo = models.IntegerField( blank=True, default='')
	branch = models.TextField()
	accountType = models.TextField()
	gender = models.CharField(max_length = 1, choices=GENDER_CHOICES)

 
class Employee(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.TextField()
	account = models.ForeignKey(Account, on_delete = models.CASCADE)


	