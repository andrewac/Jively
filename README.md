## Jively

This was a 10 day project to kickstart Boston University's Class of 2019 Senior Design Course. The goal was practice core skills to cooperative engineering such as agile methodology, git code management, and project management. Another goal was to familiarize ourselve with using cloud services, APIs, databases, simulation, and testing. 

## Timeline

On recieving the project, we met to define the system requirements and conceptualize unit tests to ensure the requirements were met. We divided tasks to sprint for first and a second tier of tasks to sprint for after the base design was accomplished. 

# First four days - research

Html, javascript, APIs, and databases (pretty much all of this project), was new material for us. On one side we were contemplating using AWS for making the entire web app, because that way the app is in the cloud and we didn't need to have a server running on our computer. But after a couple days of researching and working independently on our tasks, we regrouped to assess our progress. We decided that AWS has too many apps to learn in order to assimilate them all. While we had not accomplished our tasks, due to the learning curve that we were still overcoming, we decided to shift our focus to making maximum progress over the remaining days. We decided to redefine our short term sprint to research a simpler method of accomplishing similar goals to the project definition. 

# Second meeting 

We abandoned our AWS Web App research, and found a framework in Python called Flask for our web framework. After finding our framework in using Flask with MySQL hosted on a AWS instance, we divided tasks again and split to work independently. 
We then created a website with login interface, and a database, but had trouble connecting the database to the flask session. However, we could fill the database with simulated sensor values, and link them to users. 

## Design

The first design was to implement an serverless AWS Web Application. According to that design AWS uses DynamoDB at the backend to serverlessly store information so we don't have to think of hosting a server ourselves. The Amazon API Gateway, AWS Lambda for backend and S3 bucket for the content were very hard to learn and integrate in just 10 days time. 

![awsdesign](https://user-images.githubusercontent.com/18023551/45854360-b34f8d00-bd18-11e8-823c-37e3641aeb02.png)


The second design is a simple Flask Framework on python, with html templates and a MySQL database for relational database. There are two tables, one is to store the username and User ID (UID) and the other table stores the sensor data linked with the UID. 

## How to install Jively

Clone this repository to your server. Install these prerequisites. Link your sensors to ssh to your server and write to this database file. Run ```flask run``` to begin hosting the website. 

## How to use Jively

In order to use this app, several python modules must be installed like mysql or flask. A mysql Workbench may be installed to check for data storage in the database. Then users can login and their records can be checked if they are added to the database for correctness.

# What we achieved

We successfully  design a login page, generated random numbers for Humidity and Temperature sensors, exported them to a csv file and read that csv file into a MySQL database. 

We also were able to implement a login page who's username and UserID (UID) is stored in another Table in the database. 
<img width="308" alt="screen shot 2018-09-20 at 9 17 08 pm" src="https://user-images.githubusercontent.com/18023551/45854723-8603de80-bd1a-11e8-988e-5eca489ec3d8.png">

When a user logs in, the corresponding tables are updated with the sensor values and UID.

<img width="341" alt="screen shot 2018-09-20 at 9 16 15 pm" src="https://user-images.githubusercontent.com/18023551/45854726-88663880-bd1a-11e8-94bf-bb56908945e9.png">
The appropriate pages are also displayed for Login and Home tabs. 

If a user does not enter their username or password, the appropriate error message is also displayed in red.
<img width="254" alt="screen shot 2018-09-20 at 9 17 29 pm" src="https://user-images.githubusercontent.com/18023551/45854722-83a18480-bd1a-11e8-87e4-d59e4288cb17.png">

# What we are yet to achieve

We are yet to figure out how multiple users can be added, because once a user signs in, their userid is fixed to that user, and the userid doesn't get updated on a second login attempt. 
We were able to make the app work on a local database instance, but integrating with AWS cloud seemed a lot more problematic than we imagined. 
Also we were able to generate python graphs for the sensor data, but displaying them required that we have the right .js files, which were hard to figure out with just a day remaining to complete.
<img width="433" alt="screen shot 2018-09-20 at 9 09 12 pm" src="https://user-images.githubusercontent.com/18023551/45854730-8bf9bf80-bd1a-11e8-8322-d8fa00ba13ca.png">

Overall, we were able to figure out how to design and develop a Web App from scratch with minor updates remaining. Once the updates are complete and the app is made pretty with CSS style sheets, Jively would be born!

# Work Distribution
Andrew:

Nivedita: Database design, implementing MySQL local instance on local MySQL Workbench, SQL connections for python Flask- create, drop and insert commands, python code for generating sensor data, transferring sensor data into csv file, and then to SQL database, assimilating database modules with routes.py, attempted graph generating. 
