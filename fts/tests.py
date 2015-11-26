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

		#She types a branch Name
		branch_name_field = self.browser.find_element_by_name('branchName')
		branch_name_field.send_keys("Cebuana Pasig")
		branch_address_field = self.browser.find_element_by_name('branchAddress')
		branch_address_field.send_keys("Pasig City")

		#Kristine clicks the save button
		save_button = self.browser.find_element_by_css_selector("input[value='Save']")
		save_button.click()

		#She is returned to the "Branch" listing, where she can see her
		#new branch, listed as a clickable link
		saved_branch_link = self.browser.find_elements_by_link_text("Cebuana Pasig")
		self.assertEquals(len(saved_branch_link), 1)

		#TODO: use the admin site to create maintenance of the platform
		self.fail('Finish the Test') 
