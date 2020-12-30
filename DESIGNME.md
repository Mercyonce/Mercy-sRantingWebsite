A.Why I decided to have two css files:

I wanted for the mainpage & response page to have a distinct font and style from the rest of the other webpages.
To do this this the "body" part of the html had to be different and that's why there are two css files. The colors
of the texts, and links are also different between the mainpage & response page from the rest of the other
web pages.


B.Why I chose to have the same background image for all the webpages, and the same basic design?

This website is meant for someone who is overwhelmed with whatever they have in mind, for that reason, the website
is meant to be very simple and not add to the feeling of being overwhelmed that the person already has.

The background image is intended to invoke feelings of reflection, and give the user a sense of relief after
they've written their problem down and allowed it to dissapear into the internet.


C.rantmachine.html & design choice for buttons:
This is the welcome page. The last sentence of the quote on this page is "Let it go and be free" and this is the
theme for the entire website. For someone to write their problem down and let it go i.e. stop overthinking it
and focus on other things.

This is why all the buttons that redirect to the forms where someone is to write their problem are called
"Let it Go". The idea is that when the person writes their problem down, they are letting it go.

Why have the options to proceed anonymously or log in?
More often or not, when something is bothering you, you just want to unload it and forget about it. This is why
there's an option not to log in.

The logging in option allows someone to save their quote links.


D. How "Letting Go" works
Whether one logs in or proceeds anonymously, they are redirected to a form(LetItGo.html and LetItGo2.html)
where they write their name & problem.

on application.py:
i.the paragraph is saved into a variable and then by using .split() it is is split into a list
of words
ii.the list of negative words words.txt is opened and loaded as well
iii.each word on the paragraph is compared to words in the words.txt, if there is a match, the website uses that
word to find relevant quotes on brainy.quote
iv.if there is no match, the users name is acquired and then used on the response.html which is then loaded

Why did I choose to implement it this way?

I wanted the response to "feel" customized for a person rather than generic.That's why even if a quote can't be
loaded, the person is addressed by their name on the response page.

Why use a text file for storing negative words to be used when comparing?

It is much easier and cost-free to regurlarly update the text files with negative words that are commonly used
when ranting but also which have relevant quotes on brainy.quote website.


E. Registering and Logging in

rant.db contains a table known as "ReturningUsers" which contains id, username and password columns.

When registering:
a)code on application.py makes sure that the username isn't already present on ReturningUsers by comparing the
username inputted to what is already on the table.
b)if successful, the persons username and hash of the password is stored in ReturningUsers. This is done using
sqlite "INSERT INTO" query.

When logging in:
a) code on application.py will ensure the username and password match what I have stored on "ReturningUsers"

Why have a log in option?

To allow a user have an even more personalized experience by being able to save quotes


F.Saving quotes for logged in users

rant.db has another table "SavedQuotes" which contains id, user_id and Quotes columns.

When a logged in user writes a rant and they are redirected to a specific page of the brainyquotes website, this
link is saved into this table. This is done by using their session user_id to ensure that that link is saved for
the specific user, so that when the user logs in, it can be queried and added onto the table the user will see.

The users table found in SavedQuotes.html, has id and Quotes column. This information is obtained by quering the
Saved Quotes table found in rant.db by using the logged in users information.


G.Colors

All the colors were chosen to be simple, and to be similar to the main background image.