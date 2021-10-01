# Q1
The project is in folder `q1q5/`
I have created 4 Django Models: User, Post, Comment and Connection.

The `User` model will store user data (name, email, password, etc.).
The `Post` model will store the posts made by users (title, content and author(Foreign key to User model)).
The `Comment` model will store the comments made on post (content, date, post on which comment is 
present(Foreign key to Post model), author(Foreign Key to User model), `parentComment`(Self Reference 
Foriegn key to handle comment replies)).
The `Connection` model will store two foreign keys on User model representing their friendship.

### Scalability Comments
Lets break our scalability problem into 2:
- Quick Queries
	- Fetching data for a user will be simple as email can be indexed or primary key can be used to search
	- Fetching data for posts of a user is simple again as we have the foreign key.
	- Per post we also need to query comments, this should be a different async call to load paginated comments lazily. We can move the logic of structuring the heirarchy of replies using the parentComment foreign key to the client side.
	- We can fetch friends of a user by checking both foreign keys. We can move the logic of finding if 2 users are friends to the client side.

- Storing Data and Horizontal Scaling
	- For Users model, we can have millions of entries (A few GBs) without need for horizontal scaling, but we may use sharding to scale for future.
	- Assuming an average user will make 1000 posts, this can be in billions (A few TBs). Normally dbs can handle such loads but we can implement a caching mechanism at microservice level to reduce costly fetch operations on recent data. We may also need to use sharding mechanism.
	- Assuming an average post will have 1000 comments, this data will be of a few 100 TBs. We will need both a caching mechanism and sharding of data to store it on a distributed system. We may also need a master-slave design to ensure data availability and consistency.
	- Assuming an average user will have 1000 friends, this data will again be of a few TBs. Caching could help to save costly fetch operations on highly active users. Sharding is not necessarily required but we can have that to scale for future.


# Q2
I have created an node script in `q2q3` folder.
Install the dependecies by running `npm install`.
You can run the srcipt using `npm run q2 <your_limit>`.
The default limit is 10, you can provide any number between 1 and 10 as there are only 10 entries in box office section.

I have also dockerised the script. You can simply build the docker image:
`sudo docker build . -t <your_tag>`
Then run the docker image using:
`sudo docker run <your_tag> <your_limit>`


# Q3
I have used Redis as a Messaging Service. I have a redis instance running in background.
I have written the consumer in NodeJS `q2q3/q3_consumer.js` and publisher in Python `q2q3/q3_publisher.py`.

Start the redis instance on `localhost:6379` using `redis-server`

To run the consumer:
```shell
npm install
npm start
```

To run the publisher: Install requirements: `pip install -r requirements.txt` and run `python q3_publisher.py`


# Q4
I have created a simple python script to first squeeze all question blocks together, then sort them based on question number.

```shell
rm assignmentNew.txt
python q4.py
cat assignmentNew.txt
```

Assumptions:
- Each question is in new line and starts with `Q` has a number after it and then a `)`
- Bonus Question is a part of Q5
- Subquestions will be below the parent question

# Q5
In the project same as Q1, I have added a decorater in `facebook_lite.views` named `allow_post_only`.
This decorator checks the request method and only allows POST, it responds with 405 on any other method.

You can install the requirements using: `pip install -r requirements.txt`.
You can run the django app using: 
```shell
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

You can test it by importing the postman collection file: `Facebook_Lite.postman_collection.json`.