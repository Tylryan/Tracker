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
(1) Time Calculator: If you know when, but not how many hours you studied
(2) Stopwatch: A built in stopwatch to track time studied
(3) A list of all things tracked
(4) The last 5 Entries
(5) For Stats and Charts
(6) Backup Data
(9) To exit the program

Note: type "exit" to go back to the main screen.
        """)
        help = input('Type the number of the command you need help with. E.g. 2: ').lower().split()
        functions.clear_terminal()
        if 'exit' in help:
            print('Getting out of help. Have fun! ')
            time.sleep(1.5)
            break
        elif '1' in help:
            print("""
(1) Time Calculator

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

1) If you know how many hours hours and minutes you studied, skip the Time 
Calculator. All you need to do is enter the information at the very first prompt.

2) If you don't want to manually keep track of time AND you have this application 
downloaded on your main computer, then you can just use the built in Stopwatch to 
track your time.

Example: 

Prompt: What would you like to do? 
Input: python 02/08/21
            
            """)
            cont = input('Press "Enter" to continue ')
            if 'stop' in cont:
                break
            functions.clear_terminal()



