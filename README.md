# Dubhacks2017-team

## Inspiration

After registering for classes at a local University Lit Phansiri realized the process of figuring out which classes were needed took much more time than necessary. Each and every quarter the task consists of going over a list of classes already taken, making a list of classes needed, and then writing down each and every class’s meeting times in an effort to create at a schedule of non-conflicting classes. For students taking a full course load this process can take up to a couple of hours to complete. According to the National Center for Education Statistics, “In fall the fall of 2016, some 20.5 million students are expected to attend American colleges and universities” If each student spends 2 hours on their schedule it equates to over 112,329 hours being spent each day. That’s when Lit realized computer science could give back all students much needed study and leisure time.

A-Z, B. S. (n.d.). Fast Facts. Retrieved October 16, 2016, from http://nces.ed.gov/fastfacts/display.asp?id=372

##What it does

Schedulogy is a webapp that looks at a student’s prior transcripts and the history of classes taught in order to predict possible schedules for the student. By examining prior class catalogs Schedulogy is able to predict the possibility and likely hood that courses the student needs will be offered again. Additionally, all possible course scenarios are calculated allowing the student to have a Plan B and C in the event a class should fill before they are able to register.

How I built it
Using Django, the LAMP stack, and the AWS cloud we were all able to all work on and contribute to the project simultaneously. Some of the Python libraries we used include Mechanize, Beautiful Soup, and various other packages to handle the processing of pdf files, scraping web pages, and parsing the results of the data.


Challenges I ran into
Some of the biggest challenges we ran into was creating the algorithms needed to interpret the data needed in order to prepare the student’s class schedule. DARS and tons of pitfalls we didn’t expect like tiny details of creating the relational database that helped us link the data together.
