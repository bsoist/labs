# Bleep

## tl;dr

Implement a program that censors messages that contain words that appear on a list of supplied "banned words."

```
$ python bleep.py banned.txt
What message would you like to censor?
What the heck
What the ****
```

```
$ python bleep.py banned.txt
What message would you like to censor?
gosh darn it
**** **** it
```

{% next %}

## Understanding

This program defines only one function, `main`, which gets called per the file’s last line. Within `main` …​ ugh, looks like that’s just a big `TODO`!

{% next %}

## Specification

Complete the implementation of `bleep.py` in such a way that:

* Accepts as its sole command-line argument the name (or path) of a dictionary of banned words (i.e., text file).
* Opens and reads from that file the list of words stored therein, one per line, and stores each in a Python data structure for later access. While a Python `list` will work well for this, you may also find a [`set`](https://docs.python.org/3/tutorial/datastructures.html#sets) useful here.
* If no command line argument (e.g., `banned.txt`) is provided, be sure to have your program exit with a status code of 1.
* You may assume that any text files the staff tests with will have one word per line (each line terminated with a `\n`), and any alphabetic characters in those words will be lowercase.
* Prompts the user to provide a message.
* Tokenizes that message into its individual component words, using the `split` method on the provided string, and then iterates over the `list` of "tokens" (words) that is returned by calling `split`, checking to see whether any of the tokens match, case-insensitively, any of the words in the banned words list.
* Prints back the message that the user provided, except if the message contained any banned words, each of its characters is replaced by a `*`.
* For example, `gosh` should be replaced with four `*` characters, while `fudge` should be replaced with five.
* You should not censor words that merely contain a banned word as a substring. For example, if **bar** is a banned word in the provided list, then none of **bar**ns nor crow**bar** nor wheel**bar**row should be censored.
* You explicitly **do not** need to support input strings that contain punctuation marks. You may assume we will only test your input where each word is only separated by whitespace.

{% next %}

## Usage

Your program should behave per the examples below. Assume that the underlined text is what some user has typed.

```
$ python bleep.py
Usage: python bleep.py dictionary
```

```
$ python bleep.py list1.txt list2.txt list3.txt
Usage: python bleep.py dictionary
```

```
$ python bleep.py banned.txt
What message would you like to censor?
hello world
hello world
```

```
$ python bleep.py banned.txt
What message would you like to censor?
what the heck
what the ****
```

```
$ python bleep.py banned.txt
What message would you like to censor?
gosh darn it
**** **** it
```

{% spoiler "Hint - splititng strings" %}

In Python, you can split a string using whitespace as a delimeter using the built in string method `split`. Consider the following code:

```
phrase = 'CS is awesome'
words = phrase.split()
len(words)
type(words)
type(words[0])
```

{% endspoiler %}

{% spoiler "Hint - iterating over the words" %}

In Python, you can iterate over a list as follows:

```
for word in words:
    print(len(word))
    print(word)
```

{% endspoiler %}

{% spoiler "Hint - reading from files" %}

If filename is set to a string representing the path to a file...

```
fh = open(filename)
lines = fh.readlines()
```

{% endspoiler %}

{% spoiler "Hint - dealing with the newlines" %}

Read the lines of a file and print out the length of each line. Compare that length to the length you get when you count the letters.

{% endspoiler %}

{% next %}

### Testing

Does your code work as prescribed when you input each of the examples above from the `Usage` section?

Did you try embedding "bad words" like the **bar** examples above?

When these tests seem to work, test your code with check50!

```
check50 cs50/problems/2019/ap/bleep
```

Once you see all happy smiles, you are done! Congratulations!

You should also test your style with

```
style50 bleep.py
```


{% next "Ready to submit?" %}

### Submit50

In the terminal, type in:

```
submit50 cs50/problems/2019/ap/bleep
```
