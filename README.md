# MemeBase

Simple Web Application that is based around meme making, I took an idea of meme making and randomizer (like number randomizer) and combined them to make this web app although it seems random at first, it totally worked!.

## Technologies used
For this project, I used the following technologies:
1. HTML
2. CSS
3. Little bit of JS
4. Flask
5. SQLite3

## Design Styles
This website uses minimalistic design, that works on user's end, without complicating too much on the design, such as colorful buttons, navbar, font, etc, that's suitable for any users out there.

## Project Structures
This web app consists of these following structures
1. HTML templates
Consists of all the HTML used on it's respective uses, like index.html for making meme and essentially the homepage, inventory.html for checking the meme that are saved, meme.html for review the meme that is created, register.html and login.html for user to be able to have their own account.
2. Python file
Consists of 2 python files, such as app.py, the main code to ensure the website uptime, and the whole feature of the website, like authentication, meme making, and meme saving, the helper.py file is used to making sure the password is encrypted for extra security measures
3. The SQL Database
Database for storing the users and memes

### The Database
I used SQLite3 for the database, which have the following schemas
#### First Table
Consists of its respective user id, the username, and encrypted password,
#### Second Table
It is a meme storage system, it's scheme is consisted of user id (that made the meme), top text, bottom text, and the image url that's used

The process of making meme in this website is very simple, here's the step:
1. First you have to log in / register your account you should be redirected to the tab where you can make memes,
2. Then after you log in, you can fill the form of one of the input field (or both!) to make the caption of the meme (it has TOP TEXT and BOTTOM TEXT),
3. After filling out the text input, you can generate or randomize the meme by clicking the button,
4. After the user clicked the button, then the user will be redirected to meme reviewing tab where you can review the randomized meme that generated (The image of the meme will be randomized), if the user did not like the image, the user can simply refresh the site for another randomized image, if the user liked the combination, user can save the meme to the database and user will be redirected to meme inventory where the user can see their saved meme, the user can delete the saved meme if they wanted to.

How to launch the application:
1. Open / Extract and open the file
2. In the terminal, use cd to go to the folder
3. Run the command flask run
4. Open the provided link
5. Done

#### Video Demo
For checking out of how this website works, you can watch this video demo here
https://youtu.be/dmR_-Ul23dQ

#### Credit
This project is for the CS50x's final project, thank you for letting me make this website, it is quite a fun experience! :)
You can take the course here https://pll.harvard.edu/course/cs50-introduction-computer-science
Once again, thank you.
