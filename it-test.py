import requests

CARTS_URL = "http://carts/carts"
CUSTOMERS_URL = "http://user/customers"


# create users
def create_user(username):
	user_created = requests.models.Response
	try:
		user_created = requests.post(
			CUSTOMERS_URL,
			json = {"username": username,"password":"123","email":"1@mail.com","firstName":"foo","lastName":"bar"}
			)
	except Exception as e:
		print("Failed to create user")
		raise e

	return user_created.json()["id"]


# get id
def get_customer(user_id):
	customer = requests.models.Response
	try:
		customer = requests.get(CUSTOMERS_URL+"/"+user_id)
	except Exception as e:
		print("Failed to get customer")
		delete_customer(user_id)
		raise e
	return customer.json()["username"]

#TEST CARTS

# add item to cart for previous user
def add_item_to_cart(item_id, quantity, user_id):
	cart = requests.models.Response
	try:
		cart = requests.post(
			CARTS_URL+"/"+user_id+"/items",
			json = {"itemId":item_id, "quantity":quantity, "unitPrice":15.0}
			)
	except Exception as e:
		print("Failed to add item to cart")
		delete_customer(user_id)
		raise e

	return cart.json()


###CLEANUP### 
def delete_customer(user_id):
	try:
		cust = requests.delete(CUSTOMERS_URL+"/"+user_id)
	except Exception as e:
		print("Failed to delete customer")
		raise e
	print("Successfully deleted customer")

def delete_cart(user_id):
	try:
		carts = requests.delete(CARTS_URL+"/"+user_id)
	except Exception as e:
		print("Failed to delete cart")
		raise e
	print("Successfully deleted cart")
###CLEANUP###


def main():
	username = "foobar1"
	item_id = "510a0d7e-8e83-4193-b483-e27e09ddc34d"
	quantity = 1
	total_test = 3
	passed_test = 0

	#TEST USER SERVICE
	test_user_id = create_user(username)
	test_username = get_customer(test_user_id)
	try:
		assert test_username, username
		print("Success test : username match")
		passed_test += 1
	except AssertionError:
		print("Failed test : username match")

	#TEST CART SERVICE
	cart = add_item_to_cart(item_id, quantity, test_user_id)
	try:
		assert cart["itemId"], item_id
		print("Success test : cart item_id matched")
		passed_test += 1
		assert cart["quantity"], quantity
		print("Success test : cart item quantity matched")
		passed_test += 1
	except AssertionError:
		print("Failed test : adding item to cart")


	print("Test results : {}/{} passed".format(passed_test,total_test))
	print("cleanup starting")
	#CLEANUP
	delete_customer(test_user_id)
	delete_cart(test_user_id)


if __name__ == "__main__":
	main()