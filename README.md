[![Build Status](https://travis-ci.com/OlalKeith/store-manager-api.svg?branch=ch-api-161204773)](https://travis-ci.com/OlalKeith/store-manager-api)
[![Coverage Status](https://coveralls.io/repos/github/OlalKeith/store-manager-api/badge.svg?branch=ch-api-161204773)](https://coveralls.io/github/OlalKeith/store-manager-api?branch=ch-api-161204773)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/fe4e6ffc1a564b49b37429f02dab1ed5)](https://www.codacy.com/app/OlalKeith/store-manager-api?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=OlalKeith/store-manager-api&amp;utm_campaign=Badge_Grade)
[![Maintainability](https://api.codeclimate.com/v1/badges/3c6b96e9d1dae3c79a23/maintainability)](https://codeclimate.com/github/OlalKeith/store-manager-api/maintainability)

# store-manager-api

Store Manager is a web application that helps store owners manage sales and product inventory 

## Features

* Admin can add a product

* Admin/store attendant can get all products

* Admin/store attendant can get a specific product

* Store attendant can add a sale order

* Admin can get all sale order records


### Getting started?

*Step 1*

Clone the repo
```git clone repo ```

```cd store-manager-api ```

Create and activate virtual environmnet

```virtualenv venv --distribute ```

```source venv/bin/activate```

Install project dependencies

```pip install flask-restful```

```pip freeze > requirements.txt```

```pip install -r requirements.txt```

*Step 2*

#### Running the application locally
s
```python run.py```

*Step 3*

#### Running the Tests

On the terminal, run ```pytest -v --cov-report term-missing --cov=app```

### Product API-Endpoints

| Url EndPoint           | HTTP Request| Functionality                  	       		   | 
| ---------------------  |-------------|--------------------------------------     		   |
| /api/v1/products        | GET		   | Get all the products.            		   		   |
| /api/v1/product/<int:product_id> | GET	| Fetch a specific product using a specific id       |
| /api/v1/product<name>          | POST 	   | Create a new product.             	       		   |
| /api/v1/product/<name> | PUT	| Update a product.|
| /api/v1/product/<int:product_id>| DELETE | Delete the product using a specific id 			   |


### SaleRecords API-Endpoints


| Url EndPoint           | HTTP Request| Functionality                  	       		   | 
| ---------------------  |-------------|--------------------------------------     		   |
| /api/v1/sales       | GET		   | Get all the sales.            		   		   |
| /api/v1/sale/<int:sale_id> | GET	| Fetch a specific sale using a specific id       |
| /api/v1/sale<name>          | POST 	   | Create a new sale.             	       		   |
| /api/v1/sale/<name> | PUT	| Update a sale.|
| /api/v1/product/<int:sale_id>| DELETE | Delete the sale using a specific id 			   |


# Live Application/Documentation link

https://web.postman.co/collections/2691201-63dfac9a-6b35-f598-bc3d-a7a7ec17c9e4?workspace=0cb99f11-cbb4-44d4-83a2-07f5cff8f762


## Licence
This project is licensed under the MIT License.

## Acknowledgments



