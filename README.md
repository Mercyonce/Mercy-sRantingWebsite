
Link to youtube video presentation: https://youtu.be/vL-71H7sCCc

A. ALL THE FILES AND FOLDERS

The FINAL PROJECT folder has two additional folders within it:
a) static: this contains the main background image(rant.png) and two css files
b) templates which contains 8 html files

The FINAL PROJECT folder has five important files that aren't in folders:
a) application.py which contains the python code necessary for the website to function (the back-end)
b) rant.db which is contains two tables, ReturningUsers that keeps track of registered users of the website
and SavedQuotes which saves the quotes recomennded for a user.
c)words.txt that contains the words a users' words used in their rant/complaint is to be matched with
d)READ.md
e)Design.md


B. THE FUNCTION OF EACH IN DETAIL

Static Folder:

There are two css files:
a) style.css which is used in rantmachine.html  & response.html
b) style2.css which is used for the rest of the html files.

There is also rant.png which is the background image used in all of the html files. Its an image of a road.


Templates Folder:

There is a total of 8 html files and here is the function of each:
a) rantmachine.html is the main/welcoming page. It contains a quote which represents the motivation of this website:
A place where someone can write whatever is bothering them and then the website will redirect them to a relevant quote/
it will give them a customized response.
This web page contains two buttons, one allows the user to proceed anonymously and the other to register/login so
they may be able to save the quotes recommended for them.

b)LetItGo.html
This is the web page that someone is redirected to when they press the "Proceed Anonymously" button on rantmachine.html
It contains a form where someone inputs their name & rant/problem. The button "LetItGo" redirects them either
to a relevant quote or customized response.

c)response.html
This is "customized response" web page. It addreses the person by their name, and recommends a meditation video.

d)login.html
This contains a registration link and a form for a registered user to login.

e)register.html
This contains a form that a new user can register. After registration, they are redirected to the login page.

f)SavedQuotes.html
This is the webpage that loads when a user logs in. It contains their previous quotes in a table, and two buttons:
one that allows them to log out and another one that allows them to "LetItGo" i.e. write their problem/want and
they'll get a customized response/quote.

g)LetItGo2.html
This is a form for logged in users only to write their rant/problem and get a a customized response/quote.

h)error.html
This is the page a user is redirected to when they register with a used username, or makes errors loggin in.


Other Important Files:

a) application.py contains python code that links all the web pages together
b)words.txt contains negative words
c)README.md
d)Design.md contains explanations for design choices

C. HOW TO COMPILE

As long as every file is within the folders specified above, if you run "flask run" on the terminal at application.py
the whole website should work.