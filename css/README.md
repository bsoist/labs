# CSS

In your last lab, you practiced your HTML skills a little. 

Today, you will learn a little bit about how to "style" your HTML with CSS.

Let's start by watching a short introduction to CSS.

{% video https://www.youtube.com/watch?v=EP9QMdoXvXE&feature=youtu.be %}

{% next "Let's get started!" %}

## Your Environment

Take a look at your development environment. You should notice two tabs near the top. One for each of the two files you'll be using - `mypage.html` which is the HTML for Mrs. Soistmann's website, and `style.css` which is where you will be adding all of your CSS.

Down below, you should notice a tab for the terminal. Just like the last lab, we don't really need the terminal until we submit, so let's open a browser tab down there by clicking the + next to the terminal tab and clicking _Browser_.

Then type in `/mypage.html` after the 8083 just like you did in the last lab and then press return (or enter).

You should now see a preview of Mrs. Soistmann's website. You might notice that it looks a bit different than yours. Click on the `mypage.html` tab and see where her HTML is a little different than yours.

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

No changes, right?

{% next "Let's fix that" %}

## Using an external stylesheet

We need to tell the html page to use our stylesheet.

Click on the `mypage.html` tab and inside of the `<head></head>` type in the following:

`<link href="style.css" rel="stylesheet" />`

It can go on the line before or after the title.

So that the head of your page looks like this.

```
<head>
    <title>happy, html</title>
    <link href="style.css" rel="stylesheet" />
</head>
```

*OR* like this

```
<head>
    <link href="style.css" rel="stylesheet" />
    <title>happy, html</title>
</head>
```

Refresh your mini-browser now and you should see the changes.

Click back into your `style.css` file and let's add more style.

{% next "Starting with color" %}

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
    color: black;
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
    font-size: 4em;
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

Change that rule you just pasted in so it reads like this...

```
ul {
  list-style-type: none;
}
```

and then add this rule

```
ul li:before {
  content: '✓ ';
}
```

{% next "Let's dress up the links a little %}

## Styling Links

Let's get rid of the underline and change up the colors a bit.

```
a, a:visited, a:active {
    color: white;
    text-decoration: none;
}
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

First, let's put borders around the paragraphs so we can see what's happening.

```
p {
    border: solid #ffffff;
}
```

Refresh your mini-browser and see the changes.

Now, let's add some margin.

Add these rules to your paragraph ruleset

```
    margin-top: 50px;
    margin-left: 100px;
```

{% spoiler %}

```
p {
    border: solid #ffffff;
    background: rgb(20, 55, 32);
    margin-top: 50px;
    margin-left: 100px;
}
```

{% endspoiler %}

Refresh your mini-browser and see the changes.

Notice that the paragraph itself is pushed down 50px and over to the right by 100px. You can see this because we have a border around it. 

Now add some padding

```
    padding-left:50px;
```

{% spoiler %}

```
p {
    border: solid #ffffff;
    background: rgb(20, 55, 32);
    margin-top: 50px;
    margin-left: 100px;
    padding-left:50px;
}
```

{% endspoiler %}

Refresh your mini-browser and see the changes.

Notice this time that the paragraph itself is not moved, but that the content inside the border is moved instead. This is the difference between margin and padding.

{% next %}

## Let's check your work

Raise your hand so your teacher can review your work.

{% next "Click here after your work is approved" %}

## How to submit

In the terminal, type the following command

`submit50 tsoistmann/problems/2019/css`

and press return (or enter)

{% next %}

## Now it's time to experiment

### To get more help with HTML and CSS

Go back and edit the page so the colors, font-sizes, and other styles are more like you like them.

If you'd like some inspiration, or would like to learn more, the videos and links below are a good place to start.

{% video https://www.youtube.com/watch?v=YK78KhMf7bs&feature=youtu.be %}

{% video https://www.youtube.com/watch?v=Ub3FKU21ubk&feature=youtu.be %}

* [HTML](https://www.w3schools.com/html/)

* [CSS](https://www.w3schools.com/css/)

