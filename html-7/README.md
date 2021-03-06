# Hello, HTML

## A Word About Doing These Labs

If you just scan, copy, paste, and click next on every section... you are **doing it wrong**

Read every word of each section, figure out what it is you should be doing, then do it.

Don't just guess.

Don't rush.

{% next %}

## Getting Ready.  

Beyond introducing you to web programming, the overarching goal of this problem is to empower you to teach yourself new languages so that you can stand on your own at the end of the year. We’ll guide you through each, but if you nonetheless find yourself Googling and asking lots of questions of classmates and staff, rest assured you’re doing it right!

Let's get started!

{% next %}

## IMPORTANT - Joining Mr. Sharon's Class

In order for Mr. Sharon to see your work, you'll need to click the link below and join the class by granting access to your code.

**NOTE: the link will open in a new tab or window. Just come back here when you're done.**

<a target="_blank" href="https://submit.cs50.io/invites/7588b3946d504b4b9c05b8fa1d657944">JOIN THE CLASS</a>


{% next %}

## Setting Up Your Sandbox

Before we begin drafting some HTML, let's get our environment set up. Some of this is a little tedious, so be careful to follow the directions carefully.

First, let's opan a web browser to view our page.

Click on the little plus sign next to the Terminal tab.

![Plus button](plus_button.png)

Click _Browser_ to open a browser window.

![Click browser](click_browser.png)

You should now note that there is a link to `mypage.html` but we are going to navigate to the page a little differently so we don't have to keep clicking on the link.

Click into the address bar and add `/mypage.html` to the end and hit enter. You should see your page rendered now.

![Address bar](mypage.png)

Now note that you can...

1. Refresh your page whenever you want with that little refresh arrow.
2. Toggle between the browser and the terminal if you need to.

![Tabs and refresh arrow](options.png)


{% next %}

## Personalize the page

**NOTE: Everything you add to your page will be inside the `body` of the page. The only part of the `head` you will edit is the title.**

1. Change the title of the page
2. Add a heading with your name by adding code like this `<h1>Name</h1>`
3. Add a paragraph with this code `<p></p>` 
4. Inside that paragraph `<p>HERE</p>` type two sentences about yourself.
5. Refresh the page and make sure you like it. If not, go back a few steps and edit your markup.


{% next %}

## A Few of My Favorite Things

Now you will add two different lists of some favorite things. One of the lists will be ranked (ordered) and one not - so choose wisely. Many students like to do their favorite foods, books, movies, sports, etc, but you can choose anything that's appropriate for a school assignment.

Each list will have the items marked up like this `<li>item</li>`

Ordered lists have those list items inside of `<ol></ol>`.

Un-ordered lists have those list items inside of `<ul></ul>`.

Something like this...

```
<ul>
    <li>item one</li>
    <li>item two</li>
    <li>item three</li>
</ul>
```

**NOTE: Each list should have at least 3 items and no more than 10.**

{% spoiler "An Example of Favorite Things" %}
```
<p>Favorite Movies</p>
<ul>
    <li>The Lion King</li>
    <li>The Empire Strikes Back</li>
    <li>Planet of the Apes</li>
    <li>Godzilla</li>
</ul>

<p>Favorite Foods</p>
<ol>
    <li>Pizza</li>
    <li>Cookies</li>
    <li>Ice Cream</li>
</ol>
```
{% endspoiler %}

1. Refresh your browser, if your not done, edit and try again.


{% next %}

## Now let's add a picture

There are a lot of ways to add images to your page, but let's start with making sure you know how to use your own images.

Click the little folder icon to the left of your `mypage.html` tab.

![folder](folder.png)

Hover your mouse just to the left of that and you should find three dots appear (above those you can already see). Click on those and then click _New File_

![new file menu](new_file.png)

Click on the upload icon.

![upload icon](upload.png)

Now upload one of your own pictures. You should now see it listed in the sidebar.

### Add the markup for the image.

Image elements look like this

`<img src="" alt="" />`

Where src is set to the URL of the image and alt is set to a description of the image. URLs can be absolute or relative. Relative is always better if you can use it. So, let's use a relative URL for this image.

Paste this code into the `body` of your page somewhere.

`<img src="NAMEOFIMAGE" alt="The world's coolest dog!" />`

where `NAMEOFIMAGE` is the name of the file you uploaded.

Refresh the page. If the image appears, click next

{% next %}

## Now let's add a couple of links

Let's add a link to a new page on your site and a link to an external site.

Click the plus sign next to the `mypage.html` tab and create a new file named `newpage.html`

Copy the markup below.

```
<!DOCTYPE html>
<html>
    <head>
        <title>New Page</title>
    </head>
    <body>
        <h1>Welcome!</h1>
        <a href="mypage.html">Go back home</a>
    </body>
</html>
```

Paste that code into the new page, save it, and then click on `mypage.html` to get back to that page's markup.

Copy the markup below and paste it somewhere in the `body` of `mypage.html`

```
<a href="newpage.html">My New Page</a>
<a href="http://duckduckgo.com/">Duck Duck Go</a>
```

**NOTE how the `<a>` element works - href is set to a relative or absolute URL and the text you want the visitor to click on is "inside" the opening and closing tags.**

Refresh the page. If the links appear, click Next

{% next %}

## How to Submit

To ensure that your page is well formed, you can use the [W3Schools HTML Validator service](https://validator.w3.org/#validate_by_input), copying and pasting your HTML directly into the provided text box. 

Before you can submit, you need to make a copy of your wepage.

**Click in the terminal window and then**

Type the following command and press enter

```
cp mypage.html index.html
```

**Still in the terminal**

You may then submit by typing in at the command line:

```
submit50 cs50/problems/2019/ap/homepage
```

and pressing enter.

{% next "See if you're submission was received" %}

## Check your submission

**NOTE: The link below will open in a new tab. Just come back here to see the instructions.**

Visit <a target="_blank" href="https://submit.cs50.io/">submit.cs50.io</a> to see if you're submission is listed. 

If no, try again.

If yes, click the button below.

{% next "Now, build some more" %}

## Add more to your page

**NOTE: The link below will open in a new tab. You will need to go back and forth between that tab and this one until you get the hang of what you're doing.**

* Visit <a target="_blank" href="https://ide.cs50.io/">ide.cs50.io</a> 
* Grant permission to CS50 to access your code
* If you don't see a terminal window over on that page, click the plus sign and choose new terminal
* **in the terminal window,** type `touch index.html` and press enter/return
* **in the terminal window,** type `http-server` and press enter/return
* You will see a link there, click it
* If a menu pops up, click "Open"
* Now you will see a new tab or window in which you can see your files
* Click the link which reads `index.html` - you should see a blank page
* Now go back into your IDE and see if you can add content to your page 
* Then you can go back to the preview tab, refresh, and see your changes

## To get more help with HTML and CSS

* [HTML](https://www.w3schools.com/html/)

* [CSS](https://www.w3schools.com/css/)
