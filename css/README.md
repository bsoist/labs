# CSS

In your last lab, you practiced your HTML skills a little. 

Today, you will learn a little bit about how to "style" your HTML with CSS.

{% next "Let's get started!" %}

## Your Environment

Take a look at your development environment. You should notice two tabs near the top. One for each of the two files you'll be using - `index.html` which is the HTML for Mrs. Soistmann's website, and `style.css` which is where you will be adding all of your CSS.

Down below, you should notice a tab for the terminal. Just like the last labe, we don't really need the terminal until we submit, so let's open a browser tab down there by clicking the + next to the terminal tab and then click Browser. 

You should now see a preview of Mrs. Soistmann's website. You might notice that it looks a bit different than yours. Click on the `index.html` tab and see where her HTML is a little different than yours.

Now, click on the `style.css` tab and let's add some style.

{% next "Let's add some color!" %}

## Adding Color

Let's start by making the background Mrs. Soistmann's favorite color - blue - and the color of everything white.

Add this bit of code to your `style.css` file.

```
body {
    background: blue;
}

* {
    color: white;
}

```

Click the refresh button on your mini-browser window to see your changes.

{% next "Now let's get a little more specific with our rules" %}

## More Color

Let's make the headings green

```
h1, h2, h3, h4, h5, h6 {
    color: green;
}
```

and the list items orange

```
li {
    color: orange;
}
```

Now, let's make every item marked with a class of `dessert` pink.

```
.dessert {
    color: pink;
}
```

{% next "Let's change the font sizes" %}

## Font Sizes

Your browser already makes the headings a little bigger, but let's really increas the main heading.

```
h1 {
    font-size: 2em;
}
```

{% next "Now, let's change up those bullets" %}

## Styling Lists

```
ul {
    list-style-type: square
}
```

That's pretty cool, but let's try something a little fancier.

```
ul {
  list-style: none;
}

ul li:before {
  content: '✓';
}
```

{% next "Let's dress up the links a little %}

## Styling Links

Let's get rid of the underline and change up the colors a bit.

```
a, a:visited, a:active {
    color: white;
    text-decoration: none;
```

Now, let's underline the link when the user hovers over it and change the color to Tower Hill green.

```
a:hover {
    text-decoration: underline;
    color: rgb(20, 55, 32);
}
```

Refresh your mini-browser and hover over the links.

{% next "Cool, right?" %}

## Positioning

This can be a little tricky, but we'll experiment a bit.

First, let's put borders around the paragraphs and change the background color so we can see what's happening.

```
p {
    border: solid #ffffff;
    background: rgb(20, 55, 32);
}
```

Refresh your mini-browser and see the changes.

Now, let's add some margin.

```
p {
    margin-top: 20px;
    margin-left: 10px;
}
```

Refresh your mini-browser and see the changes.

And some padding

```
p {
    padding-left:20px;
}
```

Refresh your mini-browser and see the changes.

{% next %}

## Let's check your work

Raise your hand so your teacher can review your work.


