

#Balaaj Book Centre API

This API provides functionalities to manage a book database for Balaaj Book Centre. It utilizes FastAPI for building the web API and SQLModel for database interactions.

#Features:

    1.  Create new books
    2.  Retrieve all books
    3.  Get a specific book by ID
    4.  Update an existing book
    5.  Delete a book from the database

#Getting Started

#1. Prerequisites:

    Python 3.6 or later
    FastAPI
    SQLModel
    uvicorn
    psycopg[binary]

#2. #Installation:

    Install the required dependencies using poetry

    poetry add  fastapi sqlmodel uvicorn psycopg[binary]

#3. #Database Setup:

    The create_db function in balaaj_book_centre.book_db is responsible for creating the database tables. You might need to modify this function to connect to your specific database engine.

#4. #Running the API:
    
    Save the code in a file named main.py. Run the API using Uvicorn:

#terminal

   poetry run uvicorn balaaj_book_centre.main:app --reload
   
    This will start the API on http://localhost:8000.

#5. #API Endpoints:

1.  / (GET): Returns a simple "Hello World" message.
2.  /create_book (POST): Creates a new book in the database. 
3. Takes a JSON object representing a Book instance in the      request body.
4.  /get_books (GET): Retrieves all books from the database.
5.  /get_book/{id} (GET): Gets a specific book by its ID.
6.  /update_book/{id} (PUT): Updates an existing book. Takes a JSON object representing the updated Book instance in the request body.
7.  /delete_book/{id} (DELETE): Deletes a book from the database by its ID.


##Additional Notes:

    Error handling is implemented using HTTP exceptions. In case of any errors during database operations, a 500 Internal Server Error response will be returned with details about the exception.

    The code utilizes dependency injection to manage the database session.

    This is a basic example, and you might need to extend it further based on your specific requirements.

    ##Docker file is also created to run in docker

    Feel free to open issues or submit pull requests if you find any bugs or have improvements.
	
	 `https://github.com/wajidminhas/myapi.git` 
	 `shanitent667@example.com` 