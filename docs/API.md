# API

## Contents
- [Endpoints](#endpoints)
- [Menu](#menu)
    - [The items object](#the-items-object)
    - [Retrieve all menu items](#retrieve-all-menu-items)
    - [Retrieve specific menu item](#retrieve-specific-menu-item)

- [Orders](#orders)
    - [The order object](#the-order-object)
    - [Get all orders](#get-all-orders)
    - [Get an order](#get-an-order)
    - [Create an order](#create-an-order)
    - [Update an order](#update-an-order)
    - [Cancel an order](#cancel-an-order)

- [Delivery](#delivery)
    - [The delivery object](#the-delivery-object)
    - [Create a delivery method](#create-a-delivery-method) 


## Endpoints
```
/v1/menu
    - GET

/v1/menu/:item_name
    - GET

/v1/order
    - POST

/v1/order/:order_id
    - GET
    - PUT
    - DELETE

/v1/delivery
    - POST
```

---
## Menu
### The items object
```js
{
    "name": "",
    "price": 0.00,
    "size": "",
    "category": "",
}
```

### Retrieve all menu items
`GET /v1/menu`

Body:
```
None
```

Curl Example:
```sh 
curl http://localhost:3000/v1/menu \
    -X GET
```

### Retrieve specific menu item
`GET /v1/menu/:name/:size`

Body:
```
None
```

Curl Examples:
```sh 
curl http://localhost:3000/v1/menu/margherita \
    -X GET

curl http://localhost:3000/v1/menu/margherita/s \
    -X GET
```

---

## Orders

### The order object
```js
{
    "id": "order_1",
    "total_price": 0.0,
    "items": [],
    "delivery": {},
}
```

### Get all orders

`GET /v1/order`

Body:
```
None
```

Curl Examples:
```sh 
curl http://localhost:3000/v1/order \
    -X GET
```

### Get an order

`GET /v1/order:order_id`

Body:
```
None
```

Curl Example:
```sh 
curl http://localhost:3000/v1/order/:order_id \
    -X GET
```

### Create an order
`POST /v1/order`

Body:
```js
{
    "items": "[ valid item names and optional size ]" // REQUIRED
    "delivery": "{ valid delivery object }" // OPTIONAL
}
```

Curl Example:
```sh 
curl http://localhost:3000/v1/order \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"items":  [{"name": "pepsi" }, {"name": "margherita", "size": "m"}]}'
```


### Update an order
`PUT /v1/order/:order_id`

Body:
```js
{
    "items": "[valid items object]" // OPTIONAL
    "delivery": "{ valid delivery object}" // OPTIONAL
}
```

Curl Example:
```sh 
curl http://localhost:3000/v1/order/:order_id \
    -X PUT \
    -H "Content-Type: application/json" \
    -d '{"items":  [{"name": "coke" }, {"name": "pepperoni", "size": "l"}]}'
```

### Cancel an order
`DELTE /v1/order/:order_id`

Body:
```
None
```

Curl Example:
```sh 
curl http://localhost:3000/v1/order/:order_id \
    -X DELETE 
```


---
## Delivery

### The delivery object
```js
{
    "service": "",
    "address": "",
    "order_details": "",
    "service_order_id": "",
}
```

### Create a delivery method
`POST /v1/delivery`

Body:
```js
{
    "service": "valid service provider", // REQUIRED
    "address": "valid address string", // REQUIRED
    "order_details": "[ valid item objects ]", //REQUIRED
    "service_order_id": "valid order id", // REQUIRED
}
```

Curl Example:
```sh 
curl http://localhost:3000/v1/delivery \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"service": "UberEats", "address": "123 Queen St., Toronto, ON", "service_order_id": "UberEats_1234", "order_details": [{"name": "pepsi"}] }'
```
