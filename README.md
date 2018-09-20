# Jively
This was a 10 day project to kickstart Boston University's Class of 2019 Senior Design Course. The goal was practice core skills to cooperative engineering such as agile methodology, git code management, and project management. Another goal was to familiarize ourselve with using cloud services, APIs, databases, simulation, and testing. 

## Timeline

On recieving the project, we met to define the system requirements and conceptualize unit tests to ensure the requirements were met. We divided tasks to sprint for first and a second tier of tasks to sprint for after the base design was accomplished. 

# First four to five days : research
Html, javascript, APIs, and databases (pretty much all of this project), was new material for us. On one side we were contemplating using AWS for making the entire web app, because that way the app is in the cloud and we didn't need to have a server running on our computer. But after a couple days, of researching and working independently on our tasks, we regrouped to assess our progress. We decided that AWS has too many apps to learn in order to assimilate them all. While we had not accomplished our tasks, due to the learning curve that we were still overcoming, we decided to shift our focus to making maximum progress over the remaining days. We decided to redefine our short term sprint to research a simpler method of accomplishing similar goals to the project definition. 

# Second meeting: 

After finding our framework in using Flask with MySQL hosted on a AWS instance, we divided tasks again and split to work independently. 
After creating a website with login interface, and a database, we had trouble connecting the database to the flask session. We could fill the database with simulated sensor values, and link them to users, but users recieved the same user ID. 

## Design

The first design was to implement an serverless AWS Web Application. According to that design AWS uses DynamoDB at the backend to serverlessly store information so we don't have to think of hosting a server ourselves. The Amazon API Gateway, AWS Lambda for backend and S3 bucket for the content were very hard to learn and integrate in just 10 days time. 
https://cdn-images-1.medium.com/max/1600/1*eIECK-X8x_9wfu9uShspHw.png

## How to install Jively

Clone this repository to your server. Install these prerequisites. Link your sensors to ssh to your server and write to this database file. Run ```flask run``` to begin hosting the website. 

## How to use Jively

In order to use this app, several python modules must be installed like mysql or flask. A mysql Workbench may be installed to check for data storage in the database. 

## What we achieved

We successfully achieved 
