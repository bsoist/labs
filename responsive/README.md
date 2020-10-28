# Responsive Web Design

This lab is a little different than previous labs. Someone will guide you through it.

{% next "Let's get started!" %}

## Plain HTML is Responsive by Default

Open the file named `page1.html` and take a look at the small bit of HTML there. You might notice the spacing is a little odd. That's intended to make your work a little easier today. 

Open a browser window, "pop it out" into a real tab in your browser and use the inspect tool to view it.

If you adjust the width, you should notice the page responds very nicely to the changes in size.

{% next "One New Element" %}

## The Viewport

You may have noticed a new element in the HTML.

```
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

This element tells the browser to render the width of elements using the width of the device's screen as a reference point, and it sets the initial size to 1.0 (or "normal" size).

We'll come back to this.

{% next "Let's add an image" %}

## Adding an Image

Copy the snippet of HTML below and paste it in just below the `h1` 

```
<img src="baby_large.png" alt="baby yoda" />
```
So, it looks something like this...

```
<h1>Responsive Web Page</h1>
<img src="baby_large.png" alt="baby yoda" />
<p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Numquam, corporis voluptatem quaerat, dolorum, labore eveniet quibusdam sapiente obcaecati a fugit reprehenderit aut temporibus? Asperiores fugit tenetur molestias. Doloremque, magnam quam?</p
```

YES, the spacing doesn't look right. There's a reason for that. Leave it alone. :) 

View the page in the browser now and you'll notice the size is just too big. 

{% next "Let's fix that" %}

## Sizing an Image via CSS

You've already learned how to do this, but a common trick for sizing images responsively is setting the width to 100%.

Open the file named `style.css` and add the following code:

```
img {
    width: 100%;
    max-width: 100%;
    height: auto;
}
```

View this in the browser (be sure to refresh) and see the change.

This image works fine for desktop and mobile, but let's take a look at a common technique used with images.

Let's set up the page to use one image on smaller screens and another on larger ones.

{% next %}

Copy the code below

```
<picture>
    <source srcset="baby_small.jpg" media="(max-width: 600px)" />
    <source srcset="baby_large.png" media="(min-width: 600px)" />
    <img src="baby_large.png" alt="baby yoda" />
</picture>
```

and use it to replace this line

```
<img src="baby_large.png" alt="baby yoda" />
```

This section of your code should now look like this...

```
<h1>Responsive Web Page</h1>
<picture>
    <source srcset="baby_small.jpg" media="(max-width: 600px)" />
    <source srcset="baby_large.png" media="(min-width: 600px)" />
    <img src="baby_large.png" alt="baby yoda" />
</picture>
<p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Numquam, corporis voluptatem quaerat, dolorum, labore eveniet quibusdam sapiente obcaecati a fugit reprehenderit aut temporibus? Asperiores fugit tenetur molestias. Doloremque, magnam quam?</p>
```

View the page in the browser again. As you adjust the width, you should notice the image changes as you adjust the width below and above 600 pixels.

{% next "Now, let's do something about that headline" %}

## Responsive Fonts

You may have noticed that the headline is always the same size - no matter how big the screen. We can apply some CSS to set the size based on the viewport.

In `style.css`, add the following ruleset.

```
h1 {
    font-size:10vw;
}

```

A `vw` is defined as a percentage of the viewport's width. `10vw` will render the font as 10% of the viewport's width. On a screen that is 1920 pixels wide, then, this font will be 192px.

View your page in the browser again. As you adjust the size, you should notice the font now kind of fills up the page. 

Notice, too, that it wraps on very small screens, but those are screen sizes we don't really need to worry about. Of course, it depends on your webpage - and its intended audience - but most designers don't worry about screen sized smaller than about 400px.

If that's the case, `10vw` works on small screens, but it might be too big on larger screens. 

{% next "Let's fix that" %}

## Adjusting CSS for Screen Size

Let's take a look at the following CSS.

```
@media screen and (min-width:800px) {
    h1 {
        font-size:5vw;
    }
}
```

The first line and the outer set of `{}` instruct the browser to apply all the rulesets within the outer `{}` whenever the browser window width is at least 800px.

View in a browswer again, adjust the size, and see what it does.

What do you like an not like now about this behavior?

What might we do to make this smoother?

{% next "Let's add a little more content to the page" %}

## Adding Columns

Let's take everything we have in the body of the page now and put it inside of a `<div></div>`

Do you remember what a `<div></div>` is?

What we want to end up with is this...

```
        <div class="sidebar" id="sidebar1">Sidebar One</div>
        <div class="main">

        </div>
        <div class="sidebar" id="sidebar2">Sidebar Two</div>
```

but with all of the HTML we now have in the body "inside" that main div.

Try it.

Put these two lines just below the `<body>`

```
<div class="sidebar" id="sidebar1">Sidebar One</div>
<div class="main">
```

And these two just above the `</body>`

```
</div>
<div class="sidebar" id="sidebar2">Sidebar Two</div>
```

If you view your page in the browser again, you'll notice that one of our sidebars is above the main content and one is below. You probably expected that.

Let's use CSS to position them.

Copy the following code:

```
.main {
    float:left;
    width:60%;
}

.sidebar {
    float:left;
    width:20%;
}
```

and paste it at the bottom of your CSS.

View your page again in the browser. Note the difference.

{% next "Let's experiment a little bit" %}

## Padding and Borders

You may have noticed this, but the content of these elements sit sort of right up against the edges. 

If you don't notice it, it's more obvious if we add borders to the elements. This is a common trick used when trying to see what's going on with elements - especially with padding, margin, and positioning. 

Find the `div` selector in your CSS. You should see a rule that applies no border ( `border:none;` ). Change that to `border:solid;` 

View your page in the browser again and note the difference.

The issue with the padding should be more obvious now. Fix it by applying the rule below in two places - 1) for the `.main` selector and 2) for the `.sidebar` selector.

```
    padding:20px;
```

View it again in your browser and adjust the number 20 to whatever you like.

Go ahead and also experiment with `padding-left`, `padding-right`, `padding-bottom`, and `padding-top`

If you make your browser window very narrow, you should notice that one of our new elements is above the main element and one of them is below, which is what you'd expect from the HTML layout.

{% next "Let's see if we can move those" %}

## Floating Elements

CSS gives us a way to `float` elements. 

Let's try it and then look at how it works.

Copy the following CSS...

```
.main {
    float:left;
    width:60%;
    padding:20px;
}

.sidebar {
    float:left;
    width:20%;
    padding:20px;
}
```

and past it at the end of your `style.css`

Now view in your browser again, after refreshing, and note the difference.

If you make the window wide enough, the sidebars are now on each side of the main content. 

Notice what happens, though, if you make the window narrower. 

We can fix that using another breakpoint.

{% next "Now, let's create a new page" %}

## Something a little more complex

First, let's look at the HTML.

You'll notice three `div`s with a class of `container` 

Inside the "middle" `div` you should notice three inner `div`s with a class of `small-container`

Let's set the width and the float of those `small-container`s and use a property called `clear` to turn off floating specifically for the `main`s - just to be safe.

Add this CSS to your `style.css`

View page2.html in your browser and note the difference in layout.


```
.container {
    clear: both;
    padding:10px;
}

.small-container {
    float: left;
    width: 33%;
    padding:5px;
}
```
{% next %}
