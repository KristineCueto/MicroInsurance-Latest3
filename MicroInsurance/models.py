from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime

STATUS = (
	('A','Active'),
	('I', 'Inactive')
	)

class Branch(models.Model):
	branchName = models.CharField(default='', max_length=100, verbose_name='Branch Name')
	branchAddress =  models.TextField(default='', max_length=200, verbose_name='Branch Address')
	branchDateCreated = models.DateTimeField(default=datetime.now, verbose_name='Date Created')
	branchStatus = models.CharField(max_length=1, choices=STATUS, verbose_name='Status', default='A')

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
	underWriterDateCreated = models.DateTimeField(default=datetime.now, verbose_name='Date Created')
	underWriterStatus = models.CharField(max_length=1, choices=STATUS, verbose_name='Status', default='A')

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


class Insurance(models.Model):
	SKU_Name = models.CharField(default='', max_length=100, verbose_name='Insurance Name')
	SKU_BasedPrice = models.DecimalField(default=0.00, decimal_places=2, max_digits=18, verbose_name='Insurance Based Price')
	SKU_SellingPrice = models.DecimalField(default=0.00, decimal_places=2, max_digits=18, verbose_name='Insurance Selling Price')
	SKU_ValidityDays = models.IntegerField(default=0, verbose_name='Insurance Validity Days')
	SKU_EffectDate = models.DateTimeField(default=datetime.now, verbose_name='Insurance Effectivity Date')
	SKU_AgeFrom = models.IntegerField(
		default=18, validators=[MaxValueValidator(99), MinValueValidator(18)], verbose_name='Insurance Age From'
	)
	SKU_AgeTo = models.IntegerField(
		default=19, validators=[MaxValueValidator(100), MinValueValidator(19)], verbose_name='Insurance Age To'
	)
	SKU_LimitPerPerson = models.IntegerField(default=1, verbose_name='Insurance Limit Per Person')
	SKU_underWriter = models.ForeignKey(UnderWriter, default='', verbose_name='Under Writer Name')
	SKU_DateCreated = models.DateTimeField(default=datetime.now, verbose_name='Date Created')
	SKU_Status = models.CharField(max_length=1, choices=STATUS, default='A', verbose_name='Status')

	def test_verbose_name_for_attributes_of_Insurance_product(self):
		for field in Insurance._meta.fields:
			if field.name == 'SKU_Name':
				self.assertEquals(field.verbose_name, 'Insurance Name')
			if field.name == 'SKU_BasedPrice':
				self.assertEquals(field.verbose_name, 'Insurance Based Price')
			if field.name == 'SKU_SellingPrice':
				self.assertEquals(field.verbose_name, 'Insurance Selling Price')
			if field.name == 'SKU_ValidityDays':
				self.assertEquals(field.verbose_name, 'Insurance Validity Days')
			if field.name == 'SKU_EffectDate':
				self.assertEquals(field.verbose_name, 'Insurance Effectivity Date')
			if field.name == 'SKU_AgeFrom':
				self.assertEquals(field.verbose_name, 'Insurance Age From')
			if field.name == 'SKU_AgeTo':
				self.assertEquals(field.verbose_name, 'Insurance Age To')
			if field.name == 'SKU_LimitPerPerson':
				self.assertEquals(field.verbose_name, 'Insurance Limit Per Person')
			if field.name == 'SKU_underWriter':
				self.assertEquals(field.verbose_name, 'Under Writer Name')

	def __str__(self):
		return self.SKU_Name

class Promo(models.Model):
	PromoName = models.CharField(default='', max_length=50, verbose_name='Promo Name')
	Promo_SKU = models.ForeignKey(Insurance, default='', verbose_name='Insurance Name')
	PromoDateStart = models.DateTimeField(default=datetime.now, verbose_name='Date Start')
	PromoDateEnd = models.DateTimeField(default=datetime.now, verbose_name='Date End')
	PromoNoOfSku = models.IntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)], verbose_name='Number of SKU to be promo')
	PromoLess = models.DecimalField(default=1.00, decimal_places=2 , validators=[MaxValueValidator(100), MinValueValidator(1)], max_digits=18, verbose_name='Promo Less')
	PromoDateCreated =  models.DateTimeField(default=datetime.now, verbose_name='Date Created')
	PromoStatus = models.CharField(max_length=1, choices=STATUS, default='A', verbose_name='Status')

	def __str__(self):
		return self.PromoName	

class UserType(models.Model):
	userTypeName = models.CharField(default='', max_length=50, verbose_name='UserType Name')
	userTypeDateCreated = models.DateTimeField(default=datetime.now, verbose_name='Date Created')
	userTypeStatus = models.CharField(max_length=1, choices=STATUS, default='A', verbose_name='Status')

	def __str__(self):
		return self.userTypeName	