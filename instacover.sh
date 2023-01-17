#!/bin/bash

dte=$(date '+%B %d, %Y')

var="

**[$dte]**


&nbsp;

$2

$3


Subject: 	$1

&nbsp;

To whom it may concern, 

I hope this letter finds you well.  Please accept my resume for consideration as you seek to fill the opening for the $1 role. I think that my skills and experiences would be directly leveraged within this role:

- Through my studies of Economics & Political Science, I learned how to take and clean large data sets to examine them for relevant insights. For my capstone project, I looked at the relationship between success in sports and success in admissions. This project required me to take data from multiple sources and put it in panel format. I was able to present my findings to a group of faculty and received high marks for the research. 


- As a managing member of Xavier’s Newswire, I gained the experience of working with a group of people to achieve the complicated task on editing the school’s weekly newspaper. Putting the paper required attention to detail and clear communication to ensure that the entire team understood what they were responsible for. We were able to win multiple awards with the Ohio News Media Association (ONMA). 


I am confident that these experiences and skills, along with my passion to learn, position me to contribute strongly to your team.  I hope we can meet and explore this opportunity in more detail.

&nbsp;

Best Regards,

Joseph T. Cotton
"

echo "$var" > $2_CoverLetter.md

pandoc $2_CoverLetter.md -o $2_CoverLetter.pdf
