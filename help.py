import functions
import time
############################################ HELP ########################################################################
def help():
    while True:
        functions.clear_terminal()
        print( """
Initial Prompt:

Format:

Subject     Date     Hours

The subject is self-explanatory.
The date needs to have two digits for the month, day, and year. E.g 12/01/21.
The hour entry needs to be in terms of hours, not minutes, seconds, years etc.

Example:

Subject     Date     Hours

python    02/18/21   1.5
        m   d   y


    ----------------------------------------------------------------------
        """)

        cont = input('Press "Enter" to continue')
        print('----------------------------------------------------------------------')
        print( """
(1) Stopwatch: A built in stopwatch to track time studied
(2) Time Calculator: If you know when, but not how many hours you studied
(3) A list of all things tracked
(4) The last 5 Entries
(5) For Stats and Charts
(6) Backup Data
(9) To exit the program

Note: type "exit" to go back to the main screen.
        """)
        help = input('Type the number of the command you need help with. E.g. 2: ').lower().split()
        functions.clear_terminal()

########################################## Stopwatch ##########################################################################
        if '1' in help:
            print("""
(1) Stopwatch

Format: 

X XX (Hour (SPACE) Minute)

Purpose: 

The Stopwatch is designed to allow the user the ability to time themselves while 
studying a subject or doing a task. After the Stopwatch is stopped, the user can then
automatically enter in that time along with the chosen subject to the database all
at once.

Warning:

If the data the application displays looks ok, then the user should back up the data.
If I doesn't, then don't back it up. At that point, the user should be very
cautious. Manually back up data and try to rerun the program, if the same thing
happens, then it would be advisable to stop using the program.
Advice:


Example: 

1) Initially the user will be prompted to enter in a subject and date.

E.g.

python 02/20/21

2) The user will then be promted to press "Enter" to start the timer.
3) When the user is done with their task, they can press enter again
to stop the timer.
3) Immediately after the user stops the timer, the stopwatch will display
the total time spent on that task.
4) The user will then be asked if they want to enter in that time.
5) After the application enters the time, subject, and hours studied, it
will then ask the user if they would like to back the data up. If the data
the application displays looks ok, then the user should back up the data.
If I doesn't, then don't back it up. At that point, the user should be very
cautious. Manually back up data and try to rerun the program, if the same thing
happens, then it would be advisable to stop using the program.
            
            """)
            cont = input('Press "Enter" to continue or type "exit" \n'
            'to go back to the main menu ')
            if 'exit' in cont:
                break
            functions.clear_terminal()

########################################## Time Calculator #####################################################################
        elif 'exit' in help:
            print('Getting out of help. Have fun! ')
            time.sleep(1.5)
            functions.clear_terminal()
            break
        elif '2' in help:
            print("""
(2) Time Calculator

Format: 

X XX (Hour (SPACE) Minute)

Purpose: 

The Time Calculator allows you to insert the clock time (e.g. 2 14, or 16 30) 
you started and stopped studying a subject and will return the difference in 
terms of hours. For example, if you studied from 13 30 to 13 40 (i.e. 10 minutes),
the Time Calculator will return 0.17 hours.

It comes in handy when you know when you started and stopped studying, but you don't 
want to calculate the difference yourself.


Warning:

The delimiter is the space between the numbers. So it is important that you do 
not put commas or colons!

Advice:

1) If you know how many hours and minutes you studied, skip the Time 
Calculator. All you need to do is enter the information at the very first prompt.

2) If you don't want to manually keep track of time AND you have this application 
downloaded on your main computer, then you can just use the built in Stopwatch to 
track your time.

Example: 

Prompt: What would you like to do? 
Input: python 02/08/21
            
            """)
            cont = input('Press "Enter" to continue or type "exit" \n'
            'to go back to the main menu ')
            if 'exit' in cont:
                break
            functions.clear_terminal()

########################################## Subjects Tracked #####################################################################
        elif '3' in help:
            print("""
(3) Tracked Subjects

Purpose: 

This was designed to help with remembering how your tasks are spelled.
It can also be used to see if you have any tasks being tracked that are misspelled.

            
            """)
            cont = input('Press "Enter" to continue or type "exit" \n'
            'to go back to the main menu ')
            if 'exit' in cont:
                break
            functions.clear_terminal()

########################################## Last 5 Entries #####################################################################
        elif '4' in help:
            print("""
(4) Last 5 Entries

Purpose: 

This command will show the user their last 5 entries. This was originally designed
as another way to prevent duplicate entries.

            
            """)
            cont = input('Press "Enter" to continue or type "exit" \n'
            'to go back to the main menu ')
            if 'exit' in cont:
                break
            functions.clear_terminal()

########################################## Stats and Charts #####################################################################
        elif '5' in help:
            print("""
(5) Stats and Charts

Purpose: 

This command will show the user stats that pertain to the amount of hours
they have studied or done a particular task. 

The user can choose from 3 different options:

1) Graphs

This will show the user various graphs that will help them determine
whether or not they are spending enough time, or too much time, on 
a subject.

2) Data

This will show the user various dataframes that will essentially do the
same as the graphs except without the visuals.

3) Both

This command shows the user both graphs and dataframes. The graphs are 
going to be displayed first. After the graphs are closed out, the dataframes
will be left in the terminal for the user to analyize.

Warning:

This function will not really work until the user has at least 7 days of data
logged.


Example: 

            
            """)
            cont = input('Press "Enter" to continue or type "exit" \n'
            'to go back to the main menu ')
            if 'exit' in cont:
                break
            functions.clear_terminal()
########################################## Backup Save #####################################################################
        elif '6' in help:
            print("""
(6) Backup Save

Format: 

Purpose: 

Warning:

Advice:


Example: 

            
            """)
            cont = input('Press "Enter" to continue or type "exit" \n'
            'to go back to the main menu ')
            if 'exit' in cont:
                break
            functions.clear_terminal()

        elif '' in help:
            print("""
(6) Remove Entry

Format: 

Purpose: 

Warning:

Advice:


Example: 

            
            """)
            cont = input('Press "Enter" to continue or type "exit" \n'
            'to go back to the main menu ')
            if 'exit' in cont:
                break
            functions.clear_terminal()
    





