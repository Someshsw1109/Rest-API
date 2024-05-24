# python3-rest-api
Cloud Computing - Creating a simple REST API  
"Somesh Raj" Haldia Institute of Technology 

Somesh Raj 
someshraj78669@gmail.com

## Description
Create an application that provides a RESTFull API. It is mandatory to use at
least: GET, POST, PUT, DELETE. It is very important to respect all additional
requirements specified in the laboratory.  
**Important note:** You are not allowed to use any web frameworks!

## Observations
* I have made this api purely for educational purposes.  
* The api gives access to a database of cars. For the sake of simplicity, this
"database" is nothing more than a few "Car" objects stored in a python dictionary.  
* The initialisation process populates the database with the following cars:  

    | ID  | Make  | Model | Year | Price € |
    |:---:|:-----:|:-----:|:----:|:-------:|
    | 1   | Ford  | Focus | 2012 | 8000    |
    | 2   | Dacia | Logan | 2006 | 2400    |
    | 3   | BMW   | 320d  | 2010 | 10100   |

#### What would I do differently if I decided to remake this project
* I would make it easier to introduce/remove supported calls (maybe using python decorators and regex).
* I would change the **GET** path for a single car from `/car/id` to `/cars/id`.
* Regarding unit-testing, I would use a single test suite instead of multiple small tests.
* I would make a `CarList` class to store all the cars and CRUD functions.

## Supported Calls
* **GET** `/cars`  
* **GET** `/car/id`  
* **POST** `/cars`  
* **PUT** `/car/id`  
* **DELETE** `/car/id`

**Note:** A JSON containing all the necessary attributes should be present in a
POST or PUT request's body.