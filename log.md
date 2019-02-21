# 100 Days Of Code - Log

### Day 1: February 20, 2019

**Today's Progress**: Refactoring and Matching Pairs. 

**Thoughts:** I have written a 200~ line script for work but after testing this today, I felt it could be done better. There's some limitations in how it runs and like to add some features. 

Also I've been thinking more about the question Max brought up and have some ideas who to get this working. 

The question was the following:

Given a line, how could you tell if the pairs (defined by `({[` or `)}[` are matching, in other words closed. 

So I thought about what you really care about is just finding out of both sides are in pairs (or two's). What about if you did a simple match of items on the string? 

```
>>> foo = "(hello))"
>>> print(foo.count("("))
1
>>> print(foo.count(")"))
2
>>> left_bracket = foo.count("(")
>>> right_bracket = foo.count(")")
>>> if left_bracket == right_bracket:
...     print("matching set")
... else:
...     print("mis-match set")
...
mis-match set
>>>
```
This might work but you need to do a few more things, one issue is you need to assume there will be multiple lines to check. Then you need to know which line was successful or has a problem. 

Also the given amount of brackets will be three types (for now), and there could be brackets entered into the string as part of the string. 

I'll need to come up with a solution for this, right now I'm thinking of adding this to a dictionary and then printing out the results. 


### Day 0: February 19, 2019 

**Today's Progress**: Discussed programming with Max. 

**Thoughts:** Starting over (heh, again) with the 100 Days of Code challenge. Partly of this delay is that I was working on other issues with work, and wanted to make sure I had the time for this blog. A few things I worked on the past month. 

1. Wrote a handy Python script that sorts data from a CSV file and adds the files into a tar file

2. A few months ago I wrote something larger for work and it worked with the Google Sheets API pulling down data for reporting

3. Learning more about coding challenges, I'm involved with a weekly Python exercises (a few cycles behind on this but I'm catching up)

4. Trying to use Python more and more at work, really you're not going to find a job doing what you want, you need to make it what you want

Going forward for this log/blog, I'm going to be adding smaller snippest of code, shorter updates, to keep on track daily. 

You can also see my [old log](https://github.com/rfreiberger/100-days-of-code/blob/master/log_old.md) here. 





## Templates

### Day 0: February 30, 2016 (Example 1)
##### (delete me or comment me out)

**Today's Progress**: Fixed CSS, worked on canvas functionality for the app.

**Thoughts:** I really struggled with CSS, but, overall, I feel like I am slowly getting better at it. Canvas is still new for me, but I managed to figure out some basic functionality.

**Link to work:** [Calculator App](http://www.example.com)

### Day 0: February 30, 2016 (Example 2)
##### (delete me or comment me out)

**Today's Progress**: Fixed CSS, worked on canvas functionality for the app.

**Thoughts**: I really struggled with CSS, but, overall, I feel like I am slowly getting better at it. Canvas is still new for me, but I managed to figure out some basic functionality.

**Link(s) to work**: [Calculator App](http://www.example.com)


### Day 1: June 27, Monday

**Today's Progress**: I've gone through many exercises on FreeCodeCamp.

**Thoughts** I've recently started coding, and it's a great feeling when I finally solve an algorithm challenge after a lot of attempts and hours spent.

**Link(s) to work**
1. [Find the Longest Word in a String](https://www.freecodecamp.com/challenges/find-the-longest-word-in-a-string)
2. [Title Case a Sentence](https://www.freecodecamp.com/challenges/title-case-a-sentence)
