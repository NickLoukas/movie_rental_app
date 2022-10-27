# Movie Rental App

This is a proof of concept app of an **Online Movie Store** where users can perform all the base actions in order to search, rent and pay an online movie. We used the Django Rest Framework and provide only the API with the appropriate endpoints without the UI for the application.

### Installation

Open a terminal and run following commands:

1. Clone this repository:
   ```shell
   git clone https://github.com/NickLoukas/movie_rental_app.git --recurse-submodules
   ```

2. Change directory to movie_rental_app:
   ```shell
   cd movie_rental_app/

3. Pull the Docker images:
   ```shell
   docker pull --all-tags nickloukas/movie_rental_app

4. Run the Docker Images:
   ```shell
   docker-compose run web_migrate
   docker-compose run -d --service-ports web_run

5. Access the App at http://localhost:8000/



### Use cases

##### 1. User can get a list of all available movies

To get a list of all available movies go to the endpoint http://localhost:8000/movies/



##### 2. User can get a list of available movies based on criterias example

In order to search movies based on a criteria you just need to add a search query at the above endpoint e.g. http://localhost:8000/movies/?search=What



##### 3. User can navigate and get the details/info of a specific movie

To get the details of a specific movie just ad an id at the end of the endpoint of use case (1) e.g. http://localhost:8000/movies/2/



##### 4. User can “rent” a movie

In our app, we add an Order when we want to rent a movie. An Order has a lot of fields like:

- **created:** The datetime that the user rented the movie
- **returned:** The datetime that the user returned the movie
- **status:** The status that shows if a movie is still rented by a user `PENDING` or returned `CLOSED`
- **price:** The price of the movie per day
- **product:** The rented movie in that order
- **user:** The user that rented that movie

So if a user wants to "rent" a movie he has to add an order here http://localhost:8000/orders/



##### 5. User can “return” a movie

In order for a user to return a movie, he just has to navigate to the details of the order e.g. http://localhost:8000/orders/1/ and update the status to `CLOSED`. That means, that the movie is returned and the final price is calculated based on the day that the movie is returned minus the day that it was rented. 



##### 6. User get the charge (“amount of money”) based on days

This is basically implemented in the above use case (5) when a movie is returned, but we also provide a choice for the user to calculate the charge based on days even if the movie is still rented or returned. By going to the details of an order here http://localhost:8000/orders/1/ and changing the `Returned` date, the price also gets adjusted without the status being changed.



##### 7. User is charged 1 EU per day for the first three days and 0,5 EU per day for the days after the first three

We practically implemented this when calculating the price in the two above use cases. 