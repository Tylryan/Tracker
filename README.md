# Subject Tracker
---
## Purpose
The purpose of this application is to be able to track the amount of hours spend per day on any given task/hobby. After having about a week's worth of data, the user will be able to take full advantage of the graph functions, which allows them to visually see their performance in all tracked subjects.

## Features
* My favorite: 7-Day Rolling/Moving Average
    * A 7-day rolling/moving average of the hours spent per day on every subject tracked.
    * This is the best measure I have found for assessing my own performance in any given subject.
    * Unlike other measures, such as how many days has the user studied a subject in a row, this tells them how many hours per week on average they spend on each subject. Because it's a rolling average, it is easy to compare the current week agains any previous week.
    * This allows the user easily identify their most active subject and can help them decide if they need to be spending more or less time on a specific subject.
* Built in Stopwatch: 
    * A user can activate the built in stopwatch which tracks their time studied. This will run in the background until they stop it.
    * One might wonder why they couldn't just use their own stopwatch. The cool thing about this stopwatch is that once the user stops the stopwatch, they can save that time automatically to their desired subject.
* Time Calculator:
    * This is use when the user knows the time they started and stopped an activity, but they don't want calculate the math.
    * The user can use the results of the Time Calculator to enter in time for a subject.
* Backup Saves: This help prevent lost data.
    * After the user enters in their data, they will be prompted to back up their data if they choose. 
    * This is independent of the autosave. This helps to prevent data lost due to any error that can occur.
* "Man Pages":
    * If the user doesn't know how to use a command, they can look in the "Man Pages" I created.
    * These go over format, purpose, examples, warnings, and advice I have for a particular command.

## Please Note:
As of 2-19-21, if the user are using a Linux or Mac machine, there are no prerequisites to run this (Except the correct imports. Working on that.).
* the user don't have to have any files downloaded beforehand.
    * They will be created for the user.
* the user don't have to create a csv and type in "Subject,Date,Hours".
    * That will be done for the user.

However, if the user are a Windows user, the user will have to do the two steps above for it to work. This is mainly because there is no "touch" equivalent in Windows.


