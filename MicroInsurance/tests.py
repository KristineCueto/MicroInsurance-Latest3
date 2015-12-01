from django.test import TestCase
from MicroInsurance.models import Branch, UnderWriter, Insurance, Promo, UserType
from datetime import datetime, timedelta
from unittest import skip
from django.utils import timezone

class BranchModelTest(TestCase):

	def test_creating_a_new_branch_and_saving_it_to_the_database(self):
		#start by creating a new Branch object with its name and address
		branch = Branch()
		branch.branchName = "M LHullier"
		branch.branchAddress = "Sta. Mesa Manila"
		branch.branchDateCreated = timezone.now()
		branch.branchStatus = "A"

		#Check we can save it to the database
		branch.save()

		#now check we can find it in the database again
		all_branches_in_the_database = Branch.objects.all()
		self.assertEquals(len(all_branches_in_the_database), 1)
		only_branch_in_database = all_branches_in_the_database[0]
		self.assertEquals(only_branch_in_database, branch)

		#and check that it's saved its attributes
		self.assertEquals(only_branch_in_database.branchName, "M LHullier")
		self.assertEquals(only_branch_in_database.branchAddress, "Sta. Mesa Manila")
		self.assertEquals(only_branch_in_database.branchDateCreated, branch.branchDateCreated)
		self.assertEquals(only_branch_in_database.branchStatus, "A")

class UnderWriterTest(TestCase):

	def test_creating_a_new_under_writer_and_saving_it_to_the_database(self):
		#start by creating a new Under Writer object with its name and address
		under_writer = UnderWriter()
		under_writer.underWriterName = "Pro Life"
		under_writer.underWriterAddress = "Ortigas city"
		under_writer.underWriterContact = "+639276325934"
		under_writer.underWriterDateCreated = timezone.now()
		under_writer.underWriterStatus = "A"

		#Check we can save it to the database
		under_writer.save()

		#now check we can find it in the database again
		all_under_writers_in_the_database = UnderWriter.objects.all()
		self.assertEquals(len(all_under_writers_in_the_database), 1)
		only_under_writer_in_database = all_under_writers_in_the_database[0]
		self.assertEquals(only_under_writer_in_database, under_writer)

		#and check that it's saved its attributes
		self.assertEquals(only_under_writer_in_database.underWriterName, "Pro Life")
		self.assertEquals(only_under_writer_in_database.underWriterAddress, "Ortigas city")		
		self.assertEquals(only_under_writer_in_database.underWriterContact, "+639276325934")
		self.assertEquals(only_under_writer_in_database.underWriterDateCreated, under_writer.underWriterDateCreated)	
		self.assertEquals(only_under_writer_in_database.underWriterStatus, "A")	

class InsuranceTest(TestCase):

	def test_creating_a_new_insurance_and_saving_it_to_the_database(self):
		#start by creating a new insurance object with its name and address
		under_writer = UnderWriter()
		under_writer.underWriterName = "Pro Life"
		under_writer.underWriterAddress = "Ortigas city"
		under_writer.underWriterContact = "+639276325934"
		under_writer.underWriterDateCreated = timezone.now()
		under_writer.underWriterStatus = "A"

		#Check we can save it to the database
		under_writer.save()

		under_writer_data = UnderWriter.objects.get(underWriterName = 'Pro Life')

		insurance = Insurance()
		insurance.SKU_Name = "Car Insurance"
		insurance.SKU_BasedPrice = 10.00
		insurance.SKU_SellingPrice = 15.00
		insurance.SKU_ValidityDays = 30
		insurance.SKU_EffectDate = timezone.now()
		insurance.SKU_AgeFrom = 25
		insurance.SKU_AgeTo = 60
		insurance.SKU_LimitPerPerson = 3
		insurance.SKU_underWriter = under_writer_data
		insurance.SKU_DateCreated = timezone.now()
		insurance.SKU_Status = "A"

		#Check we can save it to the database
		insurance.save()

		#now check we can find it in the database again
		all_insurances_in_the_database = Insurance.objects.all()
		self.assertEquals(len(all_insurances_in_the_database), 1)
		only_insurance_in_database = all_insurances_in_the_database[0]
		self.assertEquals(only_insurance_in_database, insurance)

		#and check that it's saved its attributes		
		self.assertEquals(only_insurance_in_database.SKU_Name, "Car Insurance")
		self.assertEquals(only_insurance_in_database.SKU_BasedPrice, 10.00)
		self.assertEquals(only_insurance_in_database.SKU_SellingPrice, 15.00)
		self.assertEquals(only_insurance_in_database.SKU_ValidityDays, 30)
		self.assertEquals(only_insurance_in_database.SKU_EffectDate, insurance.SKU_EffectDate)
		self.assertEquals(only_insurance_in_database.SKU_AgeFrom, 25)
		self.assertEquals(only_insurance_in_database.SKU_AgeTo, 60)
		self.assertEquals(only_insurance_in_database.SKU_LimitPerPerson, 3)
		self.assertEquals(only_insurance_in_database.SKU_underWriter, under_writer_data)
		self.assertEquals(only_insurance_in_database.SKU_DateCreated, insurance.SKU_DateCreated)
		self.assertEquals(only_insurance_in_database.SKU_Status, "A")
		
class PromoTest(TestCase):

	def test_creating_a_new_promo_and_saving_it_to_the_database(self):
		#start by creating a new promo object with its attributes
		under_writer = UnderWriter()
		under_writer.underWriterName = "Pro Life"
		under_writer.underWriterAddress = "Ortigas city"
		under_writer.underWriterContact = "+639276325934"
		under_writer.underWriterDateCreated = timezone.now()
		under_writer.underWriterStatus = "A"

		#Check we can save it to the database
		under_writer.save()
		under_writer_data = UnderWriter.objects.get(underWriterName = 'Pro Life')

		insurance = Insurance()
		insurance.SKU_Name = "Life Insurance"
		insurance.SKU_BasedPrice = 15.00
		insurance.SKU_SellingPrice = 20.00
		insurance.SKU_ValidityDays = 30
		insurance.SKU_EffectDate = timezone.now()
		insurance.SKU_AgeFrom = 20
		insurance.SKU_AgeTo = 65
		insurance.SKU_LimitPerPerson = 3
		insurance.SKU_underWriter = under_writer_data
		insurance.SKU_DateCreated = timezone.now()
		insurance.SKU_Status = "A"

		#Check we can save it to the database
		insurance.save()

		insurance_data = Insurance.objects.get(SKU_Name = 'Life Insurance')

		date_data = timezone.now()
		promo = Promo()		
		promo.PromoName = "Life Promo"
		promo.Promo_SKU = insurance_data
		promo.PromoDateStart = timezone.now()
		promo.PromoDateEnd = date_data + timedelta(days=30)
		promo.PromoNoOfSku = 10
		promo.PromoLess = 100.00
		promo.PromoDateCreated =  timezone.now()
		promo.PromoStatus = "A"

		promo.save()

		#now check we can find it in the database again
		all_promos_in_the_database = Promo.objects.all()
		self.assertEquals(len(all_promos_in_the_database), 1)
		only_promo_in_database = all_promos_in_the_database[0]
		self.assertEquals(only_promo_in_database, promo)

		#and check that it's saved its attributes		
		self.assertEquals(only_promo_in_database.PromoName, "Life Promo")
		self.assertEquals(only_promo_in_database.Promo_SKU, insurance_data)
		self.assertEquals(only_promo_in_database.PromoDateStart, promo.PromoDateStart)
		self.assertEquals(only_promo_in_database.PromoDateEnd, promo.PromoDateEnd)
		self.assertEquals(only_promo_in_database.PromoNoOfSku, 10)
		self.assertEquals(only_promo_in_database.PromoLess, 100.00)
		self.assertEquals(only_promo_in_database.PromoDateCreated, promo.PromoDateCreated)
		self.assertEquals(only_promo_in_database.PromoStatus, "A")

class UserTypeTest(TestCase):

	def test_creating_a_new_usertype_and_saving_it_to_the_database(self):
		#start by creating a new usertype object with its name 
		usertype = UserType()
		usertype.userTypeName = "Manager"
		usertype.userTypeDateCreated = timezone.now()
		usertype.userTypeStatus = "A"

		#Check we can save it to the database
		usertype.save()

		#now check we can find it in the database again
		all_usertype_in_the_database = UserType.objects.all()
		self.assertEquals(len(all_usertype_in_the_database), 1)
		only_usertype_in_database = all_usertype_in_the_database[0]
		self.assertEquals(only_usertype_in_database, usertype)

		#and check that it's saved its attributes
		self.assertEquals(only_usertype_in_database.userTypeName, "Manager")
		self.assertEquals(only_usertype_in_database.userTypeDateCreated, usertype.userTypeDateCreated)
		self.assertEquals(only_usertype_in_database.userTypeStatus, "A")