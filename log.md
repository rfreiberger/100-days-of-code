# 100 Days Of Code - Log

### Day 6: February 25, 2019

**Today's Progress**: Less time but more valued 

**Thoughts**: As I'm writing in this journal I'm having a hard time keeping it updated, given that work is my main priority when I'm on the computer. So I'm spending less larger chunks of time and more shorter but intense amount of thought on a problem. It's a bit frustrating since I'm not able to really spend hours focusing on a problem but it's part of working where you need to context switch often, leading to problems. 

The better idea is moving away from trying to get that time block and more about constantly thinking about the goal of the problem or task at hand. Taking more frequent breaks as well. This is part of the Learning how to Learn class I'm taking, which is very helpful. I find that if I step away from a coding problem, I'll think about it on the drive home, or doing something else, the answer or another idea will come up in my head shortly. 

### Day 5: February 24, 2019

**Today's Progress**: Using Mindmaps

**Thoughts**: While programming, I often get confused on which part does what, especially when looking at someone else's code. At work, I'm making small changes to Puppet and while it's pretty straight forward, I do need to take notes in order to "get it". Often times I'm slower at this since I believe I'm more of a visual person over simply reading lines of code. 

Previously I would take my laptop and head to a whiteboard, sketching out the code, making lines between variables, until I finally got it. But work doesn't have an abundance of whiteboards and while I could use a simple notebook to draw my ideas out, it's difficult to transscribe these back into digital format. From a previous manager, I was introduced to [mindmapping](https://en.wikipedia.org/wiki/Mind_map) as a way to make sense of a complex problem or understand connections. 

So far I used this process a few times, between understanding how a Puppet Forge module works, to how I can map out a complex set of tasks, also to understand a design for writing a new script. What is very helpful from using a mindmap is that you can reference back to a common point, for example if you are writing a program that has a library or function which is repeated, no need to re-write that function, just point an arrow back to it. But you might think well why not use a flow chart? 

The problem with flow charts is that making something very complex takes up space and it's difficult to write this out clearly. Mindmapping doesn't offer the same level of logical flow, but it does allow for a better depth of the problem and allows you to design a flow chart later. 

For me, I'm been on this kick that if I get stuck for more than an hour on a problem, either coding or something work related, I'll break out the mindmapping app and start "drawing". Just a note, I'm mostly working on a Mac and I use the [Mindnode](https://mindnode.com/) but it's slightly expensive at $40 from the app store. Check out some of the free versions of mindmapping before making this purchase. 


### Day 4: February 23, 2019

**Today's Progress**: Refactoring work script

**Thoughts**: A few days ago I wrote this script to automate part of my work, maybe saving 30 minutes. It doesn't sound that big of a difference, since you could technically do this using system commands. But the nice thing is you can share this code (I wrote it using the Python standard library) with others, as long as they are using Python3. 

My next goal is improving this script, where I'll add the module for accessing [Google Sheets](https://pypi.org/project/gsheets/), I'm hoping this doesn't impact the sharing of the script, so I'll need to figure out how to package it. But so far, it's been super helpful, at least to me! 

[My Repo Fetch Script Example](https://github.com/rfreiberger/100-days-of-code/blob/master/code/fetch_repo_sort_example.py)

### Day 3: February 22, 2019

**Today's Progress**: SQL thoughts

**Thoughts**: At work we use MySQL pretty heavily and while I can manage some smaller tasks, I'm building up my knowlege how to run queries and build around joins. I found some handy documents about this but what makes the best process to learn is how to view this from a vendi diagram. 

[SQL Joins](https://www.sql-join.com/sql-join-types/)

On a side note, I was surprised how often this was asked in interview questions and I had little experience working with SQL. It's something important to improve. 

### Day 2: February 21, 2019

**Today's Progress**: Working on Matching Pairs.

**Thoughts**: I'm writing this from today (the 25th) since I'm a few days in my log but still working on programming daily. This might be slow going but with work taking up most of my time and the weekend with other duties, I dedicate about 15 minutes to update this log and other times to work on code. 

For the problem back on day 1, I'm thinking of a few different ways to solve this but I like to stick with something that is the easiest. I was at first looking at how we can take the count into a dictionary but this ended up a slight mess as the searching of an item in a filed wasn't very straight forward. 

So I tried something like this:

```
# iterate over the dictionary
left_count = 0
right_count = 0
for num in range(1, dict_length):
    # print(line_dict[(num)])
    # now we need to scan each line for the brackets
    left_count = line_dict[(num)]
    mystr = ''.join(left_count)
    print(type(mystr))
    print(mystr)
    if re.search(r"\[", mystr):
        print("Yes")
    else:
        print("No")
```

But I don't think this is really clean or works well. Hmm...more thought on this one. 

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
