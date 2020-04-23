# A2: Pizza Parlour API

## Contents
1. [Set up](#set-up)
1. [API](#api)
1. [Development tools and features](#development-tools-and-features)
1. [Program design](#program-design)
1. [Troubleshooting](#troubleshooting)
1. [Pair programming review](#pair-programming-review)

## Set up

You will need `docker-compose` to run the app.

- Install dependencies:  `make install`
- Start server: `make start`
- Or run in background: `make daemon`
- Stop the containers: `make stop`
- Unit tests :`make test`
- Unit tests with coverage: `make test.coverage`
- Lint: `make test.lint`
- Refresh/clear database tables: `make database.refresh`

The API is running locally on port `3000`. You can verify the server and database were set up correctly by navigating to the [menu](http://localhost:3000/v1/menu) endpoint or by running sample commands in the [API](docs/API.md).

## API
This [document](docs/API.md) contains the API resources, JSON specs and sample curl commands. 

## Development tools and features
#### Makefile
> We added a `Makefile` to simplify running reocurring commands like installing, starting the server, setting up database tables, or running tests, and linting.

#### Containers
> To reduce issues caused from differing local development environments, we set up the flask app and database inside `docker` containers using `docker-compose` to manage our production and test stacks.

#### Continuous Integration
> We set up a CI workflow using GitHub [actions](.github/workflows/main.yml) to run unit tests  and linting on every push to remote. The action will fail if a linting rule is violated or if there is < 90% unit test coverage.

#### Linting
> To ensure consisty in code styles and to prevent compile time bugs, we've added linting using [`flake8`](setup.cfg).

#### Logging
> Our server has logging enabled using pythons `logger` to help with debugging runtime errors. They can be veiwed by running `make server.logs`

#### Database
> We're using a `Postgresql` database with `Alembic` being for setting up initial tables and handling database versioning. Database versioning is very useful for managing changes to the SQL database designs across several developers.

## Program design
- The file structure we're using allows for seperation of concerns as well as making the app highly maintainable and modifiable. It's similar to the MVC design pattern but is more tailored toward our purpose of developing a database-centric API. Inside the `src` folder, there are four main subfolders: `routes`, `resources`, `commands` and `models`. 
    
    - `routes` defines the HTTP endpoints and assigns a `resource` class to handle the needs of the request. Instead of directly adding all the business logic here we use`flask_restful` to assign classes to endpoints. We also use Flask Blueprints to allow us to define and later combine all the different routes together in the main `PizzaParlour.py`. It also lets us provide an api version prefix which is useful for supporting backwards compatability with our integrations if breaking changes are introduced. 

    - `resources` handles parsing the requests and will take care of the business logic by invoking other functions. It will then return a JSON response to the client. These classes essentially serve as interfaces for client's HTTP requests, having them as seperated classes allow us to easilly add more functionality, like authentication, later on. 
    
    - `models` serve as an ORM used for abstracting interactions with our PSQL database. The models all inherent from an abstract base class (see below) to perform generic database tasks like creating, querying or deleting entities. The models follow an [Active record pattern](https://en.wikipedia.org/wiki/Active_record_pattern) where the class attributes are columns of our database tables.
    
    - `commands` are the classes that translate and combine the generic database actions to perform higher-level operations and follows the [command pattern](https://en.wikipedia.org/wiki/Command_pattern). We found it was useful to not merge the functionality of this class with the models as it allowed us to use the commands in our unit tests when we wanted to initialize objects in our test db. Instead of repeating chunks of ORM code throughout the app, we could have these classes store commands and invoke them with simpler calls to `get(), create()`, `update()`, `delete()`, etc. This pattern can also be used to manage several requests from an invoker into a queue and can make the app more resillient to receiving many requests to our database models and could perform retries on fails caused by those CRUD requests. 

    - `database` contains all the code for managing our alembic database. It's a generic set up for database versioning, you can find more info [here](https://alembic.sqlalchemy.org/en/latest/tutorial.html).

- We used an [abstract base class](src/models/abc.py) as a parent class to inherit the common actions needed to create, read, update or delete items in our PSQL database. The `Order` and `Item` models both inherit from this class.

- We use kwargs throughout the app. This has the same benefits as telescoping args mentioned in lecture.

- We use integration tests against an identical test server and test database to check that HTTP requests made to our API return the correct response and make the correct changes to our database. Instead of unit testing every function and its logic, this approach worked well with the purpose of our API and results in fewer tests with more coverage that gives us greater confidence in our code's health.

- Our database contains two main tables, `orders` and `items`. Their rows match the objects given [here](docs/API.md). The `orders` refer to `items` using foreign keys for `name` and `size` to get specific pricing and category values to limit redundancy between tables and make updating pricing information possible.

## Troubleshooting
- For database issues, try to drop and recreate tables with `make database.refresh`
- After stopping with `make stop`, to delete all stopped docker containers, you can run `docker rm $(docker ps -a -q)`

## Pair programming review

#### Add Delivery Endpoint

**Driver:** Harsh 

**Navigator:** Luke

The pair programming session was a success as it was very productive and we were able to finish the tasks within the expected time. 

Checkpoints - 
1. Creating the Endpoint ('Delivery')
    - Defining Routes
    - Post Request
2. Creating Tests

Due to Luke's previous work experience in Flask he was able to concisely explain to me (i.e. Harsh) the working of our app. We spent approximately 2 hours figuring out the requirements of the task as some aspects of this endpoint required creativity such as deciding the JSON structure for the requests and responses. 

It was a great learning experience for me as Luke was patiently able to explain me the working of Flask. While answering my questions Luke's understanding of Flask depended as well as he was challenged to put his knowledge and understanding of the technology into words.

One major difficulty that we faced was arranging this session over the internet, as we were not able to communicate as well as we could have face to face.


#### Add Menu endpoint 

**Driver:** Luke 

**Navigator:** Harsh

Having already set up the app to handle processing and creating orders, we had a good idea of what needed to be done to set up routes to parse request args then retrieve and return the menu items. We split up the task into the following checkpoints:

1. Decide on format of the items object and store dummy data in a simple python dict
1. Set up the `/menu` endpoint for getting all and getting specific items  
1. Write tests
1. Refactor/move the dictionary to our SQL table, then re-run tests to make sure it still works

The majority of our pairing video call was spent deciding the format of the menu object that would be able to store the different values of items. I found it helpful to have someone to discuss the solution with and find ways to make improvements in the solution design phase. In my past experience it can be time consuming to pair for the entire process since there isn't much going on during the coding execution, in this case though, I used the time to show Harsh things I knew about Flask. Some of the solution design aspect was difficult without have a notepad or whiteboard and we had to type out most of our ideas. Though the experience will be useful when looking for remote jobs after I graduate this semester.