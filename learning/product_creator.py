from paypal import GenerateToken,CreateProduct,CreatePlan

token=GenerateToken()
product_id=CreateProduct(token,"1234")
plan=CreatePlan(token,299,product_id,"standard")
