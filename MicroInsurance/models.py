from django.db import models
from django.utils import timezone

class Branch(models.Model):
	branchName = models.CharField(default='', max_length=100, verbose_name='Branch Name')
	branchAddress =  models.TextField(default='', max_length=200, verbose_name='Branch Address')

	def test_verbose_name_for_branchName_and_branchAddress(self):
		for field in Branch._meta.fields:
			if field.name == 'branchName':
				self.assertEquals(field.verbose_name, 'Branch Name')
			if field.name == 'branchAddress':
				self.assertEquals(field.verbose_name, 'Branch Address')

	def __str__(self):
		return self.branchName

	class Meta:
		verbose_name_plural = "Branches"

class UnderWriter(models.Model):
	underWriterName = models.CharField(default='', max_length=100, verbose_name='Under Writer Name')
	underWriterAddress = models.TextField(default='', max_length=200, verbose_name='Under Writer Address')
	underWriterContact = models.CharField(default='', max_length=13, verbose_name='Under Writer Contact No')
	def test_verbose_name_for_underWriterName_and_underWriterAddress(self):
		for field in UnderWriter._meta.fields:
			if field.name == 'underWriterName':
				self.assertEquals(field.verbose_name, 'Under Writer Name')
			if field.name == 'underWriterAddress':
				self.assertEquals(field.verbose_name, 'Under Writer Address')
			if field.name == 'underWriterContact':
				self.assertEquals(field.verbose_name, 'Under Writer Contact No')

	def __str__(self):
		return self.underWriterName

