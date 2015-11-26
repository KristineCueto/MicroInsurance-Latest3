from django.test import LiveServerTestCase
from selenium import webdriver

class MicroTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_create_maintenance_via_admin_site(self):
		#opens the web browser, and goes to the admin page
		self.browser.get(self.live_server_url + '/admin/')

		#Sees the 'Django administration' heading
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Django administration', body.text)

		#TODO: use the admin site to create maintenance of the platform
		self.fail('Finish the Test') 
