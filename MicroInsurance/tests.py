from django.test import TestCase
from MicroInsurance.models import Branch

class BranchModelTest(TestCase):

	def test_creating_a_new_branch_and_saving_it_to_the_database(self):
		#start by creating a new Branch object with its name and address
		branch = Branch()
		branch.branchName = "M LHullier"
		branch.branchAddress = "Sta. Mesa Manila"

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
