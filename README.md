# Drive_BOX

This project was a fundamental backend project that allowed me to apply and enhance my skills in Django, specifically focusing on CRUD operations, email verification, and password handling using tokens. It was a great learning experience that provided valuable insights into model design and the workings of the Django administrator.

## Overview-

Drive-BOX is a collaborative platform where users can log in, upload their projects, and collaborate with others. The project is hosted on a web hosting website named "railway," making it accessible to users worldwide. Its functionality is similar to that of GitHub, providing a user-friendly interface for uploading and managing projects.

## Technical Details
The project consists of two main applications: "blog" and "user." In the "user" application, I implemented templates for login, logout, profile, and registration pages. Utilising Django's inbuilt crispy forms library, I ensured a responsive and visually appealing design for these pages.

For the "blog" application, I incorporated static files for basic CSS, JS, and Bootstrap to enhance the website's visual appearance. The template section includes pages like "home," "about," and a "base" page, which serves as the inherited page for the entire application. By implementing the base page, I achieved consistency throughout the project, making it more user-friendly.


<h2>Assignment Problem Statement:</h2>

<h4>Part 1:</h4>
<ol>
    <li>Create a web-app where a user can login.</li>
    <li>User can upload files.</li>
    <li>User can view his/her uploaded files.</li>
</ol>

<h4>Part 2:</h4>
<ol>
     <li>User can search and view profile of other users.</li>
     <li>They can share their uploaded files with any of those users.</li>
     <li>Users can see the shared files by other users also in uploaded files.</li>
</ol>

<h4>Additional Features:</h4>
<ol>
    <li>In users profile user can set his/her profile picture.</li>
    <li>Users can download other users uploaded files.</li>
    <li>The user can upload any type of files such as images, videos, text files and also different types of programs like python code, java code, etc.</li>
</ol>
    
<h2>Technologies Used:</h2>
<ul>
    <li>Python</li>
    <li>Django</li>
    <li>Bootstrap</li>
    <li>JavaScript</li>
</ul>
    
<h2>Additional Python Modules Required:</h2>
<ul>
    <li>Django</li>
    <li>django-crispy-forms</li>
    <li>Pillow</li>
</ul>
  
<h2>Note :</h2>

<b>The Secret_Key required for the execution and debugging of project is not removed from the project code. So you can use the project as your college mini-project or by using the project code you can build your own project.</b>

<h2>Usage :</h2>

    python manage.py makemigrations

    python manage.py migrate

    python manage.py runserver
    
   In your web browser enter the address : http://localhost:8000 or http://127.0.0.1:8000/
