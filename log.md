# 100 Days Of Code - Log

### Day 15: March 6, 2019

**Today's Progress**: Reading documents

**Thoughts**: Part of working in IT or any field with constantly changing technology is reading. I actually enjoy reading but I find that I have to dig around to find the documents that are easy to read. Part of the problem is many documents are written pretty sloppy, or they assume you know all of the prerequisites. Since I'm learning about [Apache Proxy](https://httpd.apache.org/docs/2.4/mod/mod_proxy.html) I found the following guides which have been pretty helpful. 

* [Digital Ocean - Apache Virtual Hosts](https://www.digitalocean.com/community/tutorials/how-to-set-up-apache-virtual-hosts-on-centos-7)
* [Digital Ocean - Apache TLS SSL](https://www.digitalocean.com/community/tutorials/how-to-create-an-ssl-certificate-on-apache-for-centos-7)
* [Digital Ocean - Apache Proxy](https://www.digitalocean.com/community/tutorials/how-to-use-apache-as-a-reverse-proxy-with-mod_proxy-on-centos-7)

### Day 14: March 5, 2019

**Today's Progress**: Working with Helper Script

**Thoughts**: I am using my script to help with my work and send this over to my co-worker who said it's working as well. He did find a problem which is a bit unusual. The script is command line based and you need to download a CSV file then add this file name to the command arguments as `python ./myscript -f foo.csv`. The issue he found is that if the CSV file has spaces in the name `my download.csv` his terminal wouldn't see this space. Not sure why this failed but on two other users, this wasn't an issue. 

The better fix might be to make the script use the Gspread module and bypass this downloading all together. 

### Day 13: March 4, 2019

**Today's Progress**: Refactoring Helper Script

**Thoughts**: I wrote this simple script a few weeks ago and going to work on refactoring this to use a Google API module which is [Gspread](https://pypi.org/project/gspread/). The issue I found is that the Google Sheet is downloaded as a list of lists (heh, that sounds weird but once you see it, makes sense). 

I also found some tools that would also work out for this. 

[Agate](https://agate.readthedocs.io/en/1.6.1/)

You could also use Pandas but I think this is a bit more complex for a simple task. 

[Pandas Tutorial](https://data36.com/pandas-tutorial-1-basics-reading-data-files-dataframes-data-selection/)

### Day 12: March 3, 2019

**Today's Progress**: Oncall pt 2

**Thoughts**: Second day of oncall, I found out I need to learn more about [Elasticsearch](https://www.elastic.co/), this is part of our Kibana logging tool. Elasticsearch makes up for "E" in the [ELK Stack](https://www.elastic.co/elk-stack). Again, this is more about researching than coding. But I think I could connect to Kibana for stats if I could write a script to curl various links in Kibana for stats. 

### Day 11: March 2, 2019

**Today's Progress**: Oncall 

**Thoughts**: Today I'm oncall for work and my day is spent mostly checking issues. I was thinking about writing some scripts that might help out the team. I'm not sure what I would automate but I think if we had a web frontend for the dashboars or other tools, that might help the team. 

### Day 10: March 1, 2019

**Today's Progress**: Looking forward

**Thoughts**: While working on this large upgrade project, I've been overwhelmed with the amount of details I'm gathering. It's a bit like I'm finding a bunch of information but not sure if it's important or will it be something critical later. To give an example of this, currently my mindmap has about 100 points, plus 100's of lines in my markdown notes about the software and details. I still haven't completed the rest of the work going over the Apache component yet. 

In cases where it's just a ball of wires to unravel, it might be easier to simple start over. This is something I've taken about writing code that is either sloppy or not documented well. Often times it's easier to look at something and spend hours trying to [reverse engineer](https://en.wikipedia.org/wiki/Reverse_engineering) in order to understand how it worked. But when you're building something new, you might not want to waste time figuring out how something was built, and just get started building it new from scratch. 

I learned this lesson a few times when I worked with Perl code at another job. If you're not familar with [Perl](https://www.perl.org/) it's a very flexible programming language that was popular a few years ago, but now taken over by [Python](https://www.python.org/). With Perl, it's common to find people doing the same thing, in many different ways, which is really the oppsite of how Python programming is done. So when I would look at someone's Perl code, I would go back and decide it's simply easier to write the program from scratch. It's faster to get things done looking forward, instead of trying to figure out why something did something they did with an install a few years ago. 

### Day 9: February 28, 2019

**Today's Progress**: Breaking down the large problems

**Thoughts**: At work I'm tasked with this large project of updating and installing our [Atlassian JIRA](https://www.atlassian.com/software/jira). JIRA for the most part is a Java application, running Tomcat (hosting the Java code for a web app), then behind Apache Proxy for SSL/TLS. It's pretty straight forward but I ran into so many issues with the upgrade, (note - we're a few revisions behind current). Given that you're faced with so many spinning wheels and switches to flip how can you wrap around this project? 

Honestly at first I was very confused. I have only installed applications that were straight forward, following the instructions or working with a engineer from the software vendor for help in extreme cases. Also I was used to working with larger companies like Microsoft that if the first tier of support could not fix the issue, the problem was escalated. 

Once I realized our vendor was a bit different, I started to rethink my challenge. If I cannot find the help I need, at least I could note how things work and solve them myself. I started to take notes on the problem, and making sure I was clean which step was taken for which part. If I tried a solution for the problem, I would note if it worked or not, so I didn't repeat my work. Another help was looking at the problem from a [mindmap](https://en.wikipedia.org/wiki/Mind_map) which helped me see the connections between what I was doing and what needed to be done. 

It's not easy, and I faced hours of research, testing, and yes failures, but I'm getting closer to solving the problem. I would recommend that if you're faced with a complex problem, step back, look at the big picture, then slowly zoom in.

### Day 8: February 27, 2019

**Today's Progress**: More focus on small coding bits

**Thoughts**: I've been typically heavily focused on the larger scale of writing a script or short program. With my friends we're planning to create this simple game tracker for playing a pen and paper RPG game. 

So it's easy to think of sitting down for a few solid hours and working on this project. Well, it does sound easy but if you figure we're all working, taking care of the jobs and family, it's much more difficult. Much like the coding practice that helps the most, you need to think of smaller chunks of study time and more frequent instead of spending time in one large block. 

### Day 7: February 26, 2019

**Today's Progress**: Automation at work

**Thoughts**: I have written this script with the idea of making my work easier, but I found some issues which I would like to fix, since they are not that difficult to resolve. 

* Allow the script to SCP the files directly to the jump host (reduces another step)
* Use the name of the branch instead of the user name (this makes a simpler name of the file)

Hopefully I'll have these fixed shortly! 

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
