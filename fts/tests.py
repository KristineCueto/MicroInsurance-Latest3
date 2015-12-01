from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class MicroTest(StaticLiveServerTestCase):
	fixtures = ['admin_user.json']

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_create_maintenance_via_admin_site(self):
		#Kristine opens the web browser, and goes to the admin page
		self.browser.get(self.live_server_url + '/admin/')

		#She sees the 'Django administration' heading
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Django administration', body.text)

		#She types in her username and passwords and hits return
		username_field = self.browser.find_element_by_name('username')
		username_field.send_keys('admin')

		password_field = self.browser.find_element_by_name('password')
		password_field.send_keys('admin')
		password_field.send_keys(Keys.RETURN)

		#her username and password are accepted, and she is taken to
		#the Site Administration page
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Site administration', body.text)

		#She now sees a hyperlink that says "Branches"
		branches_link = self.browser.find_elements_by_link_text('Branches')
		self.assertEquals(len(branches_link), 1)

		#she clicks the hyperlink
		branches_link[0].click()

		#She is taken to the branches listing page, which shows she has
		#no branches yet
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('0 Branches', body.text)

		#She sees a link to 'add' a new branch, so she clicks it
		new_branch_link = self.browser.find_element_by_link_text('Add branch')
		new_branch_link.click()

		#She sees some input fields for "Branch Name" and "Branch Address"
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Branch Name:', body.text)
		self.assertIn('Branch Address:', body.text)

		#She types a branch Name and its address
		branch_name_field = self.browser.find_element_by_name('branchName')
		branch_name_field.send_keys("Cebuana Pasig")
		branch_address_field = self.browser.find_element_by_name('branchAddress')
		branch_address_field.send_keys("Pasig City")

		#Kristine clicks the save button
		save_button = self.browser.find_element_by_css_selector("input[value='Save']")
		save_button.click()

		#She is returned to the "Branch" listing, where she can see her
		#new saved branch, listed as a clickable link
		saved_branch_link = self.browser.find_elements_by_link_text("Cebuana Pasig")
		self.assertEquals(len(saved_branch_link), 1)

		#She goes back to the home page to add a new under writers
		home_link = self.browser.find_elements_by_link_text("Home")
		self.assertEquals(len(home_link), 1)

		#She clicks the link of home page
		home_link[0].click()

		#she is taken to the Site Administration page again
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Site administration', body.text)		
		self.browser.implicitly_wait(10)

		#She now sees a hyperlink that says "Under writers"
		under_writers_link = self.browser.find_elements_by_link_text('Under writers')
		self.assertEquals(len(under_writers_link), 1)

		#she clicks the hyperlink
		under_writers_link[0].click()

		#She is taken to the under writers listing page, which shows she has
		#no under writers yet
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('0 under writers', body.text)

		#She sees a link to 'add under writer' , so she clicks it
		new_underWriter_link = self.browser.find_element_by_link_text('Add under writer')
		new_underWriter_link.click()

		#She sees some input fields for "Under Writer Name" and "Under Writer Address"
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Under Writer Name:', body.text)
		self.assertIn('Under Writer Address:', body.text)
		self.assertIn('Under Writer Contact No:', body.text)

		#She types a under writer Name a its address
		new_underWriter_name_field = self.browser.find_element_by_name('underWriterName')
		new_underWriter_name_field.send_keys("Sun Life")
		new_underWriter_address_field = self.browser.find_element_by_name('underWriterAddress')
		new_underWriter_address_field.send_keys("Marikina City")
		new_underWriter_contact_field = self.browser.find_element_by_name('underWriterContact')
		new_underWriter_contact_field.send_keys("+639282980493")

		#Kristine clicks the save button
		save_button = self.browser.find_element_by_css_selector("input[value='Save']")
		save_button.click()

		#She is returned to the "Under writer" listing, where she can see her
		#new saved under writer, listed as a clickable link
		saved_underWriter_link = self.browser.find_elements_by_link_text("Sun Life")
		self.assertEquals(len(saved_underWriter_link), 1)
		self.browser.implicitly_wait(10)

		#She adds new underwriter
		add_underWriter_link = self.browser.find_element_by_link_text('Add under writer')
		add_underWriter_link.click()

		#She sees some input fields for "Under Writer Name" and "Under Writer Address"
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Under Writer Name:', body.text)
		self.assertIn('Under Writer Address:', body.text)
		self.assertIn('Under Writer Contact No:', body.text)

		#She types a under writer Name a its address
		add_underWriter_name_field = self.browser.find_element_by_name('underWriterName')
		add_underWriter_name_field.send_keys("Pro Life")
		add_underWriter_address_field = self.browser.find_element_by_name('underWriterAddress')
		add_underWriter_address_field.send_keys("Taguig City")
		add_underWriter_contact_field = self.browser.find_element_by_name('underWriterContact')
		add_underWriter_contact_field.send_keys("09282980493")

		#Kristine clicks the save button
		save_button = self.browser.find_element_by_css_selector("input[value='Save']")
		save_button.click()

		#She is returned to the "Under writer" listing, where she can see her
		#new saved under writer, listed as a clickable link
		saved_underWriter_link = self.browser.find_elements_by_link_text("Pro Life")
		self.assertEquals(len(saved_underWriter_link), 1)
		self.browser.implicitly_wait(10)


		#Kristine goes back to the home page to add now a new insurance
		home_link = self.browser.find_elements_by_link_text("Home")
		self.assertEquals(len(home_link), 1)

		#She clicks the link of home page
		home_link[0].click()

		#she is taken to the Site Administration page again
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Site administration', body.text)		
		self.browser.implicitly_wait(10)

		#She now sees a hyperlink that says "Insurances"
		insurances_link = self.browser.find_elements_by_link_text('Insurances')
		self.assertEquals(len(insurances_link), 1)

		#she clicks the hyperlink
		insurances_link[0].click()

		#She is taken to the insurances listing page, which shows she has
		#no insurances yet
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('0 insurances', body.text)

		#She sees a link to 'add insurance' , so she clicks it
		new_insurance_link = self.browser.find_element_by_link_text('Add insurance')
		new_insurance_link.click()

		#She sees some input fields for attributes in adding insurance
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Insurance Name:', body.text)
		self.assertIn('Insurance Based Price:', body.text)
		self.assertIn('Insurance Selling Price:', body.text)
		self.assertIn('Insurance Validity Days:', body.text)
		self.assertIn('Insurance Effectivity Date:', body.text)
		self.assertIn('Insurance Age From:', body.text)
		self.assertIn('Insurance Age To:', body.text)
		self.assertIn('Insurance Limit Per Person:', body.text)
		self.assertIn('Under Writer Name:', body.text)

		#She types the information needed for the insurance to be added
		new_insurance_name_field = self.browser.find_element_by_name('SKU_Name')
		new_insurance_name_field.send_keys("Death Insurance")

		new_insurance_BasedPrice_field = self.browser.find_element_by_name('SKU_BasedPrice')
		new_insurance_BasedPrice_field.send_keys(100.00)

		new_insurance_SellingPrice_field = self.browser.find_element_by_name('SKU_SellingPrice')
		new_insurance_SellingPrice_field.send_keys(120.00)

		new_insurance_ValidDays_field = self.browser.find_element_by_name('SKU_ValidityDays')
		new_insurance_ValidDays_field.send_keys(30)

		new_insurance_EffectDate0_field = self.browser.find_element_by_name('SKU_EffectDate_0')
		new_insurance_EffectDate0_field.send_keys(Keys.CONTROL + "a")
		new_insurance_EffectDate0_field.send_keys(Keys.DELETE)
		new_insurance_EffectDate0_field.send_keys("2015-11-28")

		new_insurance_EffectDate1_field = self.browser.find_element_by_name('SKU_EffectDate_1')
		new_insurance_EffectDate1_field.send_keys(Keys.CONTROL + "a")
		new_insurance_EffectDate1_field.send_keys(Keys.DELETE)
		new_insurance_EffectDate1_field.send_keys("12:00")

		new_insurance_AgeFrom_field = self.browser.find_element_by_name('SKU_AgeFrom')
		new_insurance_AgeFrom_field.send_keys(Keys.CONTROL + "a")
		new_insurance_AgeFrom_field.send_keys(Keys.DELETE)
		new_insurance_AgeFrom_field.send_keys(20)

		new_insurance_AgeTo_field = self.browser.find_element_by_name('SKU_AgeTo')
		new_insurance_AgeTo_field.send_keys(Keys.CONTROL + "a")
		new_insurance_AgeTo_field.send_keys(Keys.DELETE)
		new_insurance_AgeTo_field.send_keys(60)

		new_insurance_LimitPerPerson_field = self.browser.find_element_by_name('SKU_LimitPerPerson')
		new_insurance_LimitPerPerson_field.send_keys(Keys.CONTROL + "a")
		new_insurance_LimitPerPerson_field.send_keys(Keys.DELETE)
		new_insurance_LimitPerPerson_field.send_keys(3)

		new_insurance_UnderwriterName_field = self.browser.find_element_by_name('SKU_underWriter')
		new_insurance_UnderwriterName_field.send_keys("Pro Life")
		
		#Kristine clicks the save button
		save_button = self.browser.find_element_by_css_selector("input[value='Save']")
		save_button.click()

		#She is returned to the "Insurances" listing, where she can see her
		#new saved insurance, listed as a clickable link
		saved_insurance_link = self.browser.find_elements_by_link_text("Death Insurance")
		self.assertEquals(len(saved_insurance_link), 1)
		self.browser.implicitly_wait(10)
		#TODO: use the admin site to create maintenance of the platform
		#self.fail('Finish the Test') 
