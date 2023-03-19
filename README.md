# bakery_orders_django
A little site for working with bakery orders



## Motivation

Motivation to get a job opportunity and earn more experience in backend development


## Running instructions
Running postgresql and adminer in docker containers
```sh
git clone https://github.com/ELePhanT1708/bakery_orders_django.git
cd bakery_orders_django
docker-compose up --build 
``` 

Running django up on local machine:

```sh
cd bakery_orders_django
cd bakery
py namage.py runserver   
``` 


## Implementation details

For read and write to database used Django ORM.

Relation MANY-to-MANY between product and order created by temp table OrderItem which has order_id and product_id with quantity.



## GUI
### Home page
![image](https://user-images.githubusercontent.com/58446568/226162342-f00ac739-2244-470e-9956-854ebe63dbd5.png)

### Form for creating order with several items at once:
![image](https://user-images.githubusercontent.com/58446568/226162393-b4cf1925-e6e6-4420-bb54-d6dc6c6dfe91.png)

### Orders in board with progress bar
In each request this page will update info with defined get_queryset function
![image](https://user-images.githubusercontent.com/58446568/226162662-bd33c0d2-f330-410e-ae4d-ac5c391540ca.png)


### MENU page
![image](https://user-images.githubusercontent.com/58446568/226162567-c4e5211c-1d6c-41dd-ba4a-89e55db18d1b.png)


### Form for adding new product to menu
![image](https://user-images.githubusercontent.com/58446568/226162587-537d7900-01c7-4544-bdbc-d221afe68f6d.png)



_____________________
END

