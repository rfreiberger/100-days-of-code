# 100 Days Of Code - Log

### Day 1: January 1, 2018 

**Today's Progress:** Completed my personal web site update, mostly HTML/CSS code which was taken from a template. I would like to migrate this to either Python Bottle or Jekyl and process this on TravisCI. [Robaf.com](http://robaf.com)

**Thoughts:** I wanted to explore CSS in depth but I also liked to focus my time on Python development side. I hope I can move towards the Python method for creating not only my main page but also the blog as well. 

### Day 2: January 2, 2018

**Today's Progress:** I spent part of the day trying to get an working example on Heroku for a Python project using [BottlePy](http://bottlepy.com) but ran into other issues. I think Heroku might have changed their pricing as it looks like everything was now a charge. After that I preped for an interview by starting up a host with Puppet, the configuration management tool. This took a long time to install, so while waiting I took a look at a problem presented to myself during an interview. 

Given a random list of numbers, how would you find the largest sequental?

I actually got stuck on this for a while, but after switching my code "sketchboard" to Juypter Notebooks. This method is so much easier to see the code and make quick changes. While I did this, I still was stuck and finally moved to using [PythonTutor](http://pythontutor.com) that allows you to run the code in a visual mode for debugging. This was the missing step I needed to solve the logic. 

So here it is, it's rough but it works. :) 

```
python

def largest_seq(foo):
    temp_count = 0
    temp_number = 0
    temp_total_count = 1
    temp_high_count = 0
    temp_high_number = 0
    for num in foo:
        if temp_number == num:
            temp_count += 1
            print("Found match, adding to temp count")
        else:
            if temp_count > temp_high_count:
                temp_high_count = temp_count
                temp_high_number = temp_number
            else:
                temp_count = 1
                temp_number = num
            print("Found new match, restarting temp count")
    print("Temp High Number: " + str(temp_high_count))
    print("Temp High Count: " + str(temp_high_number))
```

```
largest_seq(foo)
Found new match, restarting temp count
Found new match, restarting temp count
Found new match, restarting temp count
Found match, adding to temp count
Found new match, restarting temp count
Found new match, restarting temp count
Found match, adding to temp count
Found match, adding to temp count
Found match, adding to temp count
Found new match, restarting temp count
Found new match, restarting temp count
Found match, adding to temp count
Found match, adding to temp count
Found new match, restarting temp count
Found new match, restarting temp count
Found match, adding to temp count
Found match, adding to temp count
Found new match, restarting temp count
Found new match, restarting temp count
Found new match, restarting temp count
Found new match, restarting temp count
Found new match, restarting temp count
Found match, adding to temp count
Found match, adding to temp count
Found match, adding to temp count
Found match, adding to temp count
Found new match, restarting temp count
Found new match, restarting temp count
Found new match, restarting temp count
Found new match, restarting temp count
Temp High Number: 5
Temp High Count: 5
```

**Thoughts:** I think I can make this more efficent, and this took a while to solve but keeping up my coding habits will improve my knowlege of solving these logic puzzles. 

### Day 3: January 3, 2018

**Today's Progress:** I spent half the day for an interview which gave me a coding question (and failed). The question was two parts, first sort a list of numbers, then the second was count the number of times a number appeared. I've been learning algorithms so I know about the bubble sort but trying to impletment this within 10 minutes was difficult. 

So I'm working on this now with Python and notebook. Without looking for a clue, the core idea is taking the total length of the list given, then use this as the index point. Now you can select the first two points ``mylist[0] vs mylist[1]`` if one is larger, place this into a new list ahead of the other. Continue this until all are in correct order. 

While this is easy, I'm having a hard time picturing how to do this in Python. Here's my current status. 

```
def sortlist(foo):
    new_list = []
    list_length = (len(mylist))
    for num in range(0,(list_length)):
        first_pos = num
        second_pos = (num + 1)
        print(first_pos)
        print(second_pos)
        if 
```

I should have this completed soon, I'm picturing it in my head and might need to whiteboard it out. 

**Thoughts:** It seems like most of these interview questions are based upon sorting a list or counting a list. It's a good idea to master these steps and it will helpout greatly in the future. 

### Day 4: January 4, 2018

 **Today's Progress:** Today I checked out a Python package called [Python-docx](https://python-docx.readthedocs.io/en/latest/) which allows for editing and creation of Microsoft Word documents. So my idea while job searching is using Python to create my cover letters through a script. As I worked on this script I found out that some of the template code from my current Word file do not translate over to the module. So it ended up being somewhat of a guessing game which options I could use. 

 While watching a Youtube video on Python logging [Socratica](https://www.youtube.com/watch?v=g8nQ90Hk328), I found some tips for checking a module without documentation. 

 ```
 >>> import docx
>>> dir(docx)
['Document', 'ImagePart', 'RT', 'SettingsPart', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__na
me__', '__package__', '__path__', '__spec__', '__version__', 'api', 'blkcntnr', 'compat', 'dml', 'document', 'enum', 'ex
ceptions', 'image', 'opc', 'oxml', 'package', 'parts', 'section', 'settings', 'shape', 'shared', 'styles', 'text']
```

Entries in caps are constants, in caps are classes, lower case are methods. 

After playing around with this more, I decided that for now, it's not going to give me the options to build what I want but it is helpful. 

I switched over to finish working on the question of sorting a list of random numbers. Again, it's a algo question (which I honestly haven't studied yet) but I'm going to focus on this over the weekend to solve. 

**Thoughts:** This is a side note but I have been using Windows 10 for my Python development recently. I had some issues with the module installs, so I tried using the Ubuntu shell (which also failed) but found that running Python through Windows PowerShell actually worked. Also I have been spending most of my time using the (Juypter Notebooks)[https://jupyter.org/] which is much easier to keep track of thoughts and ideas instead of 100's of random scripts. 

As I start on a deeper track of learning, I wanted to stay away from the issues I faced before. I spent hours on problems of modules not installing and platform problems, skipping out on core programming skills. Now with most of my coding focused on sorting lists, it's so much easier. 


### Day 5: January 5, 2018

**Today's Progress:** Today I spent most of the day working on completing the job questions for an interview I had last week. Got these completed and updated to my personal Github account. 

Bubblesort.py 

```
#!/usr/bin/env python3

import random

newlist = [random.randint(0,101) for r in range(50)]

def bubblesort(mylist):

    print("Starting sort on following random list: ")
    print(newlist)

    for outloop in range(0, len(mylist) -1, 1):

        for inloop in range(0, len(mylist) -1, 1):

            if mylist[inloop] > mylist[inloop + 1]:

                temp = mylist[inloop]
                mylist[inloop] = mylist[inloop + 1]
                mylist[inloop + 1] = temp

    print("Completed sort")
    print(newlist)


bubblesort(newlist)
```

countitems.py

```
#!/usr/bin/env python3

a = [1, 6, 2, 3, 5, 1, 4, 1, 2, 4]

def countitems(mylist):

    print("Starting count")

    countdict = {}

    for items in mylist:
 
        if items in countdict:

            countdict[items] =  (countdict[items] + 1)

        else:

            countdict[items] = 1

    for name in sorted(countdict):
        print("Number: " + str(name) + " Count: " + str(countdict[name]))
        
    print("Completed count")

countitems(a)
```

I was stuck on the bubblesort and after I read about I found a critical error I made. I first assumed that during the bubble sort, you would compare the values in pairs. 

For example, the following list we want to process the bubble sort. 

```
foo = [ 3, 1, 4, 2]
```

So incorrectly I assumed you would first compare ``3 > 1``, then ``4 > 2``. But you are really comparing ``3 > 1`` then ``3 > 4`` and so on. Once I had this figured out and corrected the idea of two loops made sense, since you don't run into issues extended beyond the range of the list. 

**Thoughts:** While it's tough, I am starting to feel more confident in my coding skills. I'm still far away from programming off the whiteboard but I do realized that you need to write code everyday in order to learn it best. 

### Day 6: January 6, 2018

**Today's Progress:** After reading up on Linux kernel logs, I decided to jump back into the Udemy video series on (Python and data structures)[https://www.udemy.com/python-for-data-structures-algorithms-and-interviews]. It's a decent course and so far, at lecture 46, feels like it's easy to follow and understand. The points about algorithms was difficult to get, but I'm sure this just takes time to fully set. 

**Thoughts:** Keeping up with the 100 days of code log has been fun and rewarding. I'm looking forward to seeing how far I can go and hopefully beyond 100 days. 

### Day 7: January 7, 2018 

**Today's Progress:** Today I spent the time going over some coding challenges on (CoderWars)[http://coderwars.com], which are pretty simple but took some time to make them cleaner. This is one example. 

The puzzle was to count all of the "x" and "o" in a string and compare they are matching in counts. 

```
def testfunct(foo):
    count_x_o = {
                'x_value': 0,
                'o_value': 0
                }
    for letters in foo.lower():
        if 'x' in letters:
            print("X found")
            count_x_o['x_value'] += 1
        elif 'o' in letters:
            print("O found")
            count_x_o['o_value'] += 1
        else:
            print("X or O was not found")
    print(count_x_o)
    if count_x_o['x_value'] == count_x_o['o_value']:
        print("Matching set of X and O")
    elif count_x_o['x_value'] != count_x_o['o_value']:
        print("Mismatched set of X and O")
    else:
        print("Did not find any X or O values to count")

testfunct("xoxoxoxoxoxoxxoxoxxoxoxooxoxoxoxoxoxxoxoxo")
```

So this works but it's not that efficent, when I saw the solutions they were captured in two lines, much more Pythonic as they say. This shows something interesting that with programming you can get things to work but it's not the most efficent. Of course this will improve with time but for now, it's hard to really learn and write things in the fastest method. 

**Thoughts:** I'm starting to find the challenges of Coderwars becoming easier, while I'm on the tutorial method (which are the lower skilled challenges) it's now making sense. Before I would whiteboard the script multiple times, now I'm starting to go right to the notebooks and try out a few different ideas. The speed of my turn around has increased and looking much better. 

### Day 8: January 8, 2018 

**Today's Progress:** Today I went on a short screening interview with a recruiter agency and they asked some coding questions which are early screeners for jobs. One of the questions was "how can you find the prime numbers under 100" or complete "fizzbuzz". The Fizzbuzz is a easy problem but the prime number, that sounded easy as well. It wasn't until the ride home on the train did I realize how complex the question was and found the issues during my steps to write this out in code. 

The issue is you need to find the number which is only divded by 1 or it's self. So this is hard to seperate from the rest of the numbers since it's also including non-prime numbers. I really struggled into this puzzle and found some things for later. 

This was one confusing part, how to loop through a range but skip or remove certain numbers. 

```
def testfunctrang(foo):
    for x in range(1, foo + 1):
        for y in range(1, foo + 1):
            if y != 1 and y != 7:
                print("X: " + str(x) + " " + "Y: " + str(y))
testfunctrang(10)
```

This would output the following. 

```
X: 1 Y: 2
X: 1 Y: 3
X: 1 Y: 4
X: 1 Y: 5
X: 1 Y: 6
X: 1 Y: 8
X: 1 Y: 9
X: 1 Y: 10
```

We can now see that 1 and 7 from the previous code made the skip of the range happen. Pretty handy!

Right now I'm still pretty stuck on this problem so my new rule (instead of waiting days and dropping away from coding) is to give it 24 hours and then look for the solution but actually understand it, not just copy it!

**Thoughts:** While I'm mostly practicing to increase my job skills, I'm also realizing that coding can be very confusing if you do not have solid math skills. With this prime problem, I had to understand the calculation of prime numbers before I could actually start solving the puzzle. 

### Day 8: January 8, 2018 

**Today's Progress:** So today I spent more time on this puzzle and again, I felt that it was not coming into my mind for the solution. I started to check around YouTube for the answer and found the following video. 

[Socratica Python and Prime Numbers](https://youtu.be/2p3kwF04xcA)

So like most puzzles, it's frustrating to see how simple the actual solution really is compared to the actual solution. I did try to solve it in my own method but while I was somewhat close, I made a serious mistake in the calculations. 

**Thoughts:** Most of these problems are math based and I like to refresh my skills maybe watching more Khan Academy or books for college level math. It's been a while since I have taken a math class. 

### Day 9: January 9, 2018 

**Today's Progress:** Wrapping up the prime puzzle, I didn't solve this but ran it through [Python Tutor](http://pythontutor.com/) which was really handy to show the differences in speed. 

The simple version from Socratica works using True and False, note that I added the print statements for my own use. 

```
def find_prime(n):
    
    for x in range(1, 1 + n):
        if n == 1:
            print("1 cannot be a prime!")
            return False
        
        for d in range(2, n):
            if n % d == 0:
                print(str(n) + " is not a prime number!")
                return False
        print(str(n) + " is a prime number!")
        return True
```

So this in turn checks a single number (known as n) and rolls through a range of numbers (known as d) with the exception of using 1. Since 1 is not prime, the script automatically returns False. 

Sample run with slight moditications to use a loop for numbers. 

```
def find_prime_range(input_number):
    
    def find_prime(find_prime_number):
        if find_prime_number == 1:
            return False
        for d in range(2, find_prime_number):
            if find_prime_number % d == 0:
                return False
        return True
    
    def range_count(range_number):
        for range_value in range(1, 1 + range_number):
            print(range_value, find_prime(range_value))
    
    range_count(input_number)
    
find_prime_range(10)
```

The output. 

```
1 False
2 True
3 True
4 False
5 True
6 False
7 True
8 False
9 False
10 False
```

So the tricks of doing this faster (while calcuating 100 numbers, it's fast but if you wanted 100,000 it's starting to slow down) is reducing the amount of divison. 

Here's the example from the video. 

```
import math

def find_prime_range_v2(input_number):
    
    def find_prime(find_prime_number):
        if find_prime_number == 1:
            return False
        max_divisor = math.floor(math.sqrt(find_prime_number))
        for d in range(2, 1 + max_divisor):
            if find_prime_number % d == 0:
                return False
        return True
    
    def range_count(range_number):
        for range_value in range(1, 1 + range_number):
            print(range_value, find_prime(range_value))
    
    range_count(input_number)
    
find_prime_range(100)
```

Another method shown in the video was only using even numbers as shown below. Note, this version is much faster than the previous two other versions. 

```
import math

def find_prime_range_v3(input_number):
    
    def find_prime(find_prime_number):
        if find_prime_number == 1:
            return False
        
        if n == 2:
            return True
        if n > 2 and n % 2 == 0:
            return False
        
        max_divisor = math.floor(math.sqrt(find_prime_number))
        for d in range(3, 1 + max_divisor, 2):
            if find_prime_number % d == 0:
                return False
        return True
    
    def range_count(range_number):
        for range_value in range(1, 1 + range_number):
            print(range_value, find_prime(range_value))
    
    range_count(input_number)
    
find_prime_range(100)
```

This is pretty interesting on the processing of prime numbers and simply reducing the amount of work through logic. This reminds me of the tricks in algebra where you could skip over steps if the values followed a formula. 

**Thoughts:** Today I was really frustrated with this script, to the point of just quitting and moving on. I didn't get the solution figured out but I had to call it (throw in the towel) in order to move forward and learn. It doesn't help if you get stuck and just frustrated without learning. 

### Day 10: January 10, 2018

**Today's Progress:** Today I spent time catching up on my coding and working on the prime number script. Felt like it was towards my limit of knowledge in programming and math. Something I found from these puzzles is there is a correct way to figure out the problem and a hard way. You can brute force the solution but for most of these answers, you need to have proper logic in order to fix it correctly. 

During an interview I was asked this question. 

"How can you find the solution for X + Y = Z, where Z is a given number"

When I first encountered this problem, I did something like the following (it's been a while).

Import random moudle and roll random numbers until I can find a match. Honestly this worked (well worked most of the time) and then I found out how incorrect this method of programming was. So later I did the following. 

```
# solve for x and y where z is given 

def solve_for_x_y(foo):
    
    for x in range(1, 1 + foo):
        for y in range(1, 1 + foo):
            if x + y == foo:
                print("The solution for x + y = " + str(foo) + " is: "+ (str(x)) + "," + str(y))
            else:
                continue

solve_for_x_y(10)
```

The output. 

```
The solution for x + y = 10 is: 1,9
The solution for x + y = 10 is: 2,8
The solution for x + y = 10 is: 3,7
The solution for x + y = 10 is: 4,6
The solution for x + y = 10 is: 5,5
The solution for x + y = 10 is: 6,4
The solution for x + y = 10 is: 7,3
The solution for x + y = 10 is: 8,2
The solution for x + y = 10 is: 9,1
```

This is of course much easier and faster, I actually had a problem trying to write the original code since it was so weird and just plain wrong. But this is just an idea how tough learning programming from scratch can be if you don't have a solid foundation in math or programming. I really recommend for people starting out, learning math and puzzles before trying to build large projects. 

**Thoughts:** While I have been having fun going through all of these challenges, I would like to also build up some side projects. Something I've been thinking about is a Python Django or Flask for a web game. 

### Day 11: January 11, 2018

Recently I have been focusing on these interview questions, I am still going over the Udemy video series I mentioned before and some challenges in the Codewars website. Some of the challenges I found myself trying to sort is various list questions (find the number of X in the list). While I think these are helpful in my career and with the current interviewing, I'm not really building a project or something with a goal. 

What I like to do is start moving away from the videos (seriously they are like 200+ lectures) and start planning out a project on my own. Something I'm thinking about is building a reporting page in Python that grabs data from one source, imports this into a database and then presents the data as a simple graph. I'm not entirely sure how this will work with Python or which platform I should use (Django, Flask, Bottle) but it's a project that would be handy for my portfolio and also something I could build for my next job. 

### Day 12: January 12, 2018

While this update is not much of a coding update (I'm still going over the data structures video) it's more focused on my current tool chain and how I work with Python. For years I would be working with the traditional method of writing a script in my editor of choice (vim or Sublime) and after I was done, save my work, then move to the console to execute the code. This cycle of back and forth while worked for longer scripts was not so great in terms of checking a certian function and how it works or just testing a piece of the code. 

I tried using the Python console as well but it didn't feel as straight forward and one thing I never liked is how the formatting of a loop or function would get messed up if I tried to edit it again. 

After a while, I started to try out something I haven't used much, (Jupyter Notebooks)[https://jupyter.org/]. So the thing about Jupyter Notebooks (they used to be called iPython Notebooks) is that it allows you to run the Python commands in the web page and a server is running locally to execute the commands on the page. This sounds like the Python console but the big selling point is you save your work in the file and this can be restored when you re-open the file again. 

So at any point you can come back to your work and start off. This is a huge selling point as I have my notebooks stored in Dropbox, which allows me to jump from one machine (my desktop) to another (my laptop) without any loss in notes. 

The downside is using the notebooks for longer scripts doesn't work as well and you also don't have some of the features using a proper editor or IDE. But for my current projects of learning programming challenges, it's a plus. 

### Day 13: January 13, 2018

While going over the video series I found some very handy featues of Python which I never seen before. One of them is the max. 

```
help(max)
Help on built-in function max in module builtins:

max(...)
    max(iterable, *[, default=obj, key=func]) -> value
    max(arg1, arg2, *args, *[, key=func]) -> value
    
    With a single iterable argument, return its biggest item. The
    default keyword-only argument specifies an object to return if
    the provided iterable is empty.
    With two or more arguments, return the largest argument.
```

This is actually pretty cool in that it can take either a list of numbers, or two values and find the highest value. 

```
foo = [1, 4, 6, 2, 10, 9]
max(foo)
10
max(50,100)
100
```

Some of these build in functions are extremely helpful, just this would be a time saver if you needed to find the largest item in a list. 

### Day 14: January 14, 2018

As mentioned before, I'm researching building a Python web site. My goal is making something for my portfolio but also as a side project. I would like to build a simple web game that is based off (Dungeon Crawl Classics)[http://goodman-games.com/dungeon-crawl-classics-rpg/], which is a D&D style game using the 20D system. The idea would be a user can create a character based upon a random roll and from here they could enter a world and fight monsters based on random rolls. 

It sounds simple but the characters need to follow certain rules and there is compounded rolls based upon rolls which change depending on the class or decisions made. I'm not sure how I could build this, but I could sketch it out as a text based script in Python then upgrade it to a web app later. 

As some side thoughts, I found Django has more resources then Flask and Bottle but are deeper in complexity to get going. 

### Day 15: January 15, 2018

Today I read up on Django and the books on Amazon. While I have some videos on Udemy about Django for Python development, I'm looking for some books and other resources to get started with a core site. Some of the gaps I have right now is I don't want to make a super deep project which involves less creation on the site and more digging for the platform to get it going. 

Another thing I'm looking at is Puppet configuration management which is been recently popular with my job interviews. So this is based on Ruby (eeek!) but I'll need to start understanding it a bit more than I do now, I have experience with Chef (again based on Ruby) but it's been a while since I really explored the code. 

### Day 16: January 16, 2018

I've been lacking on this 100 day challenge, the hard part is I'm prepping for interviews and focusing more on the Linux configuration tools like Puppet and Chef. Which is technically ruby programming but I tend to think it's not. The other project I'm working on is how to build out my Dungeon Crawl Classics script to play out a module. I found some ideas but for now, it's going to be a smaller prototype instead of the huge web app I originally envisioned. 

### Day 17: January 17, 2018

Today I had an interview in San Francisco for a company offering a system admin role which was some programming and use of Puppet. The interview went well and they got to the coding question, which is always my worry part. It's not that I'm not understanding programming and some of the basic programming puzzles they ask but it's the level at which they ask the questions. For one role, I presented my skills and background very clearly and mentioned that my skills are in the range of "system admin scripts" I even made multiple mentions that I do not have a formal CS background. 

While the hiring manager said not to worry, the question I was asked indeed was a harder CS question. So I feel nervous when they start to ask the questions in an interview, since "do you know Python" can mean anything from can you print "Hello World" to write out a bubble sort. Luckly for myself the question asked in the interview today was much easier and I actually practiced it before, I still felt like it's something to keep practice. 

### Day 18: January 18, 2018

So I haven't been programming much as it's been some job interviews, but I'm coming up with a rough sketch for the dungeon script. Something I found is that it's better to have something working than just a project 50% done. This is the method of how [Scrum Agile](https://www.scrumalliance.org/why-scrum) works. You develop a project a little bit at a time and each version you have something to present, then have this version audited for improvements. 

With the dungeon script, I'm going to first make the interface, which will be command line based for the simple fact it's the quickest way. The module I'm exploring is [Click](http://click.pocoo.org/4/) which makes an easier method to take in the users arguments and input instead of using the argparse method. Something else I'm working on is how can I present something graphical to the user from the command line. I was thinking about presenting objects as emoji unicode. The problem I'm having is finding the right emoji characters and how to print them. 

### Day 19: January 19, 2018

It's been a few days since I updated this log but I'm working on programming **almost** daily. 

A side project I'm still planning out is how could I work on this DCC code. I mentioned this to the group of friends I play with and they would be happy to join the project. Right now I have some ideas for the code, so it's going to be nothing too difficult. Something I have worked out is it's better to have something working instead of nothing. The core idea of "under promise, over deliver". So my initial idea was to build out a full web app, maybe in Bottle but then I started to think of what is the most simplest method? I could just tie all of the tables in the gaming manual back to a dictionary, but writing this out would be a pain. 

Without an editor than handles spaces correctly, I'm sure I'll make a mistake entering by hand 100 entries. So I wonder, well could I use this in a simple database? From there, I would also use another table that would hold the players last entries, maybe allow a "saved state"? Now I'm going to start looking for ways to simply work with a SQLite database, or if needed a MySQL data (if we want to make it more professional with PHP later).

### Day 20: January 20, 2018

The upcoming week I had a bunch of interviews lined up. (I'm writing past tense since I'm updating this log days late!) So right now I'm going over some of the common questions and how I could answer these better. I am planning to write a article on LinkedIn about interviewing since I have been doing phone screens and in person interviews this past month. In short, I really don't think a white board programming exercise works well in all cases. The cases always go through a few variations (sort a list, work with a matrix, count items in a list, basic math) which is enough that you could memorize these common questions or worse pull them from Leetcode. 

What might be a better solution is really discussing a past project, white board the plan, explain the solution and how to improve it. Or maybe work with a larger issue, and explain how this could be solved. Both cases would be longer than saying "just complete Fizzbuzz". 

### Day 21: January 21, 2018

More review for the interview week, I have mostly focused on refreshing my Python skills and back on other related skills. Something I really need to improve is my SQL knowledge, especially how to build queries. 

### Day 22: January 22, 2018

Today I had an interview for an SRE position and found the job is one of the interviews where they did not ask me any coding questions. While this is somewhat unusual, I did find it a tad of a let down, since I enjoy getting the challenge of dealing with a random problem in a given amount of time. I'm trying to stay in a coding mindset, so when I face an interview that doesn't have any mention of coding or brings up this question, it gives me a bit of insight that the job might not ask for any coding in the near future. While this can always change, if the daily work doesn't mention you have time to develop anything, you get the sense it's more focused on simple support. 

### Day 23: January 23, 2018

Traveled to SF for another interview, this time it was for a senior SRE role which I knew was over my head in terms of experience. It was a bit of a weird communication with the recruiter but she asked for me to travel out to their office without having a phone screen first. I was really going to cancel based upon my gut feeling but decided I should at least get out for the experince but also the interaction. Even if things go down in flames (which they did) I can walk away with better understanding of how a smaller company works internally. 

The technical side I honestly did poorly, one of the engineers was from Facebook so I knew the level was pretty high going in. The other engineer was pretty friendly and very experienced but gave me a bit of the answer after each question. I actually learned some new topics and everyone was very professional. The next engineer presented me a coding question and mentioned he's been following my coding blog (hey if you're reading this now). 

He presented a question to me as the following. 

**Question: How could you take the following matrix and end up with the following**

```
0001000,        =>        0011100,
0010000,        =>        0111000,
0000000,        =>        0000000,
0000100,        =>        0001110,
0000010,        =>        0000111,
```
So I first thought about this as taking the entry of numbers per line, then entering each one as a new item in a dictionary. Like this. 

```
number_dict = {'1':
                  '0001000',
               '2':
                  '0010000',
               '3':
                  '0000000',
               '4':
                  '0000100',
               '5':
                  '0000010'
              }
```

But there's a problem, how can I check each line in the dictionary as an array? This was actually mentioned by the engineer which I didn't know to solve. So I brought up another idea about using a list of lists. I haven't used list of lists much before, so I'm going to try and solve this. But it's a good problem to work on!




