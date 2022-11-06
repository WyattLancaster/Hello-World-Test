# Wyatt Lancaster
# 11/6/2022
# GPA Checker
# This application starts by prompting the user to input a student's last name or enter "ZZZ" to cancel.
# After that it takes the value of the studentLastName variable and starts a loop as long as it doesn't = "ZZZ".
# In this loop it asks the user to input a first name as well as the student's GPA.
# It then checks if the student made the Dean's list by having a GPA of 3.5 or higher.
# It then checks if the student made the Honor Roll by checking if they have a GPA of 3.25 or higher.
# If the GPA meets neither of those values it will return with a message saying the student didn't make either.
# The loop finishes by prompting the user to enter another last name or to end the software.

studentLastName = input("Input student\'s last name, or type \"ZZZ\" to cancel: ")

while studentLastName != "ZZZ":
    studentFirstName = input("Input student\'s first name: ")
    studentGPA = float(input("Input student\'s GPA: "))
    if studentGPA >= 3.5:
        print(studentFirstName, studentLastName, " has made the Dean\'s list.")
    if studentGPA >= 3.25:
        print(studentFirstName, studentLastName, " has made the Honor Roll.")
    else:
        print(studentFirstName, studentLastName, " did not make the Dean's list or the Honor Roll.")
    studentLastName = input("Input another student\'s last name, or type \"ZZZ\" to cancel: ")

