Web Based Case Study 

The requirement is to develop a Web application which will read data from a .csv file and perform various operations mentioned below. 
➢ Create a csv file by the name students.csv with the following content: 

➢ This application should be developed using combination of client/server web technologies. For the client side code, combination of HTML/CSS/JS should be used and for the server side code, you can use any technology of choice like Servlet/JSP/PHP/.NET/Python. 

➢ Create an index.html page which will display the following options to the user:
        ◦ Add new Student
        ◦ Search for a Student by Id 
        ◦ Display all the Students 

➢ Based on the selection done by the user, create separate pages for processing the request accordingly.

    • Step 1: create add-student.html page which will display a form to the user like this:

    • When the user submits the form, some server side code should be written to save the data in the students.csv file. 
          
    • Step 2: create a page called as search-student.html file which will look like this: 

    • When the user submits this form, some server side code should read the data from the csv file and display the same to the user like this: 

    • Similarly try to complete the 3rd scenario which will display all the students data in an HTML page. 

----------------------------------------------------------------------------------------------------------------------------
Technology used: HTML5, CSS3, PYTHON, Flask
Editor: Visual Studio Code

APPROACH:
    • Create the CSV file (students.csv) to store the details of the Students.
    • Write a Flask Server using Python, which redirects the user to different routes.
    • The Flask Server should also be able to read, write and manipulate the data in the CSV file.
    • Create a main HTML page (index.html) which redirects the user to the desired pages.
    • Create an add-student.html page which has a form that collects the student data entered and sends it to the back-end sever to store in the students.csv file.
    • Create a search-student.html page through which the user searches for students’ details using the student Id. The id is sent to the back-end server which then matches the id with the data in the students.csv file and a linear search algorithm is performed on the data to find the correct student record.
    • Create a display-students.html page that displays the details of all the students recorded in the students.csv file.
