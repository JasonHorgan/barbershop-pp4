# Barney's Barbershop

[Live site](https://jh-pp4-9671216aa959.herokuapp.com/)

![AmiResponsive](documentation/amiresponsive.png)

## User Experience

### Overview

Barbey's Barbershop is a website for a local barbershop based in Greystones, Ireland. I want to create a site that showcases what services are offered and allows users to easily book and manage appointments at their local barbershop 

#### First Time User

- I want to learn about a barbershop in Greystones
- I want to find clear and concise information about the barbers, services and price
- I want to be able to book appointments online and easily

#### Returning User 

- I want to be able to edit and delete appointments I have already booked 
- I want to view information on appointments I have had in the past so I can see who I booked with last time


### Agile

For this project I used the Agile approach to break each feature down into individual more managable, trackable bits of work. I really enjoyed using the Agile method as it helped me stay organised and on track. All of my user stories were tracked through the Github protects kanban board as can be seen below:

![Kanban](documentation/kanban.png)

#### User Stories 

I used the issues feature on Github to create user stories using a custom template. Once each user story was complete, it was moved from todo to in progress to done. I had 13 user stories in total with 9 complete and 4 left to be implemented at a later date on the next sprint. 

- Completed User Stories
    - As a developer I need to set up my workspace so that create my project
    - As a user I can access a calendar so that book appointments on this website
    - As a user I want to be able to cancel my booking if I can no longer attend the appointment
    - As a developer I want to set up all auth so that people can register as a user on my website to access booking features
    - As a developer I need to create the front end home page for my site
    - As a user I want to have the ability to edit bookings so I can change the date or time
    - As a developer I want to add a services page so the user can view services offered and their prices
    - As a developer I want to deploy my live site to Heroku
    - As a user I can create an account so that I can create, view, edit and delete appointments

- Incomplete User Stories
    - As a developer I want to limit appointment times so only 1 user can book each time slot
    - As a developer I can create a custom 404 page so that the 404 page is in line with the design of the rest of the site
    - As a userI can verify my email so that I can receive emails from the barbershop
    - As a user I can request a password reset email so that I can log into the account is I forget my password

All user stories can be viewed in full detail [here](https://github.com/users/JasonHorgan/projects/4)


## UI 

I made a quick Wireframe before my first meeting with my mentor to discuss project inception so I would have a rough idea of how I wanted to look, which can be seen below:


![Wireframe 1](documentation/wireframe1.png)
![Wireframe 2](documentation/wireframe2.png)

In the end I created 8 custom HTML pages, including the Base.html page, which can be seen below:

The index page is the home page where the user can find information about the barbershop and includes a book now button. If the user is not logged in and clicks the book now button, they are directed to the sign in page. If they do not have an account, they can also sign up for an account from here. 
If the user is logged in when they click te book now button, they are directed to the create appointment page where they can book an appointment. 
On succesful booking of an appointment, the user is then directed to the profile page, where they can view their appointments. This can be seen in the screenshots below. 

![Index](documentation/index_page.png)
![Book appointment](documentation/book_app.png)
![Log in](documentation/signin.png)
![Profile](documentation/profile.png)

The Nav Bar Alo changes depending on logged in state. If the user is logged in, they will see the following Nav Bar:

![Logged in](documentation/logged_in.png)

If the user is logged out, the navbar will appear like so:

![Logged out](documentation/logged_out.png)

If the user clicks on the 'Delete Appointment' button, I have added some defensive programming for good user experience so they are required to confirm cancellation before the appointment is cancelled:

![Delete app](documentation/delete_app.png)

## Testing

Manual testing was done for this project and all the info can be found [here](https://github.com/JasonHorgan/barbershop-pp4/blob/main/TESTING.md)

## Deployment

This project was deployed using Heroku. Full details of deployment seen below:



