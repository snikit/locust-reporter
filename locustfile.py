from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):
	@task(1)
	def index(self):
		self.client.get("/v2/api-docs")
		self.client.get("/users/ashish.jaiswal@siemens.com/productGroups/default")
	@task(5)
	def default(self):
		self.client.get("/users/kedar.joshi@siemens.com/productGroups/default")
		self.client.get("/users/ashish.jaiswal@siemens.com/productGroups/default")
	@task(2)
	def additionallinks(self):
		self.client.get("/users/kedar.joshi@siemens.com/products/additionallinks")
		self.client.get("/users/ashish.jaiswal@siemens.com/products/additionallinks")
	@task(2)
	def favorites(self):
		self.client.get("/users/kedar.joshi@siemens.com/products/favorites")
		self.client.get("/users/ashish.jaiswal@siemens.com/products/favorites")
	@task(2)
	def recent(self):
		self.client.get("/users/kedar.joshi@siemens.com/products/recents")
		self.client.get("/users/ashish.jaiswal@siemens.com/products/recents")
	@task(2)
	def favoritePut(self):
		self.client.request(method="PUT",
			url="/users/kedar.joshi@siemens.com/products/favorites",
			headers={
				"Content-Type": 'application/json'},
			data='["SE788-ENG"]'
			)
		self.client.request(method="PUT",
			url="/users/ashish.jaiswal@siemens.com/products/favorites",
			headers={
				"Content-Type": 'application/json'},
			data='["SE788-ENG"]'
			)
	@task(2)
	def favoriteDelete(self):
		self.client.request(method="DELETE",
			url="/users/kedar.joshi@siemens.com/products/favorites",
			headers={
				"Content-Type": 'application/json'},
			data='["SE788-ENG"]'
			)
		self.client.request(method="DELETE",
			url="/users/ashish.jaiswal@siemens.com/products/favorites",
			headers={
				"Content-Type": 'application/json'},
			data='["SE788-ENG"]'
			)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    # help(UserBehavior.client)
    min_wait = 5000
    max_wait = 9000