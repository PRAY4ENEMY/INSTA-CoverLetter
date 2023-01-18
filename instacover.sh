#!/bin/bash

## prompt for user to enter relavant information ##

echo "ENTER: position title"
read title
echo "ENTER: Company Name"
read cona
echo "ENTER: location"
read location

## set date in (Month Day, Year) format ##

dte=$(date '+%B %d, %Y')

## basic outline for cover letter ##

text="

**[$dte]**


&nbsp;

$cona

$location


Subject: 	$title

&nbsp;

To whom it may concern, 

I hope this letter finds you well.  Please accept my resume for consideration as you seek to fill the opening for the $title role. I think that my skills and experiences would be directly leveraged within this role:

- Through my studies of Economics & Political Science, I learned how to take and clean large data sets to examine them for relevant insights. For my capstone project, I looked at the relationship between success in sports and success in admissions. This project required me to take data from multiple sources and put it in panel format. I was able to present my findings to a group of faculty and received high marks for the research. 


- As a managing member of Xavier’s Newswire, I gained the experience of working with a group of people to achieve the complicated task on editing the school’s weekly newspaper. Putting the paper required attention to detail and clear communication to ensure that the entire team understood what they were responsible for. We were able to win multiple awards with the Ohio News Media Association (ONMA). 


I am confident that these experiences and skills, along with my passion to learn, position me to contribute strongly to your team.  I hope we can meet and explore this opportunity in more detail.

&nbsp;

Best Regards,

Joseph T. Cotton
"
 
## allows file names to be formated without spaces so it doesnt look ugly as hell in the directory ##

fname=$(echo -e "$cona" | tr -d '[:space:]')

echo "$text" > "$fname"_CoverLetter.md

pandoc "$fname"_CoverLetter.md -o "$fname"_CoverLetter.pdf && echo "Cover letter for $position @ $cona successfully created"
