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

## How to **contribute**?

If you're not comfortable with the command line, [here are tutorials using GUI tools.](https://docs.github.com/en/desktop/installing-and-configuring-github-desktop/overview/getting-started-with-github-desktop). If you don't have git on your machine, [install it](https://help.github.com/articles/set-up-git/).

<img align="right" width="400" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

**1.** Fork [this](https://github.com/pratt0007/Drive_BOX) repository.

**2.** Clone your forked copy of the project.

```

git clone https://github.com/<your_name>/drive_box.git

```

**3.** Navigate to the project directory :file_folder: .

```

cd drive_box

```

**4.** Add a reference(remote) to the original repository.

```

git remote add upstream https://github.com/pratt0007/Drive_BOX

```

**5.** Check the remotes for this repository.

```

git remote -v

```

**6.** Always take a pull from the upstream repository to your master branch to keep it at par with the main project(updated repository).

```
git pull upstream main
```

**7.** Create a new branch.

```
git checkout -b <your_branch_name>
```

**8.** Perform your desired changes to the code base on that branch.

**9.** Track your changes :heavy_check_mark: .

```

git add .

```

**10.** Commit your changes.

```

git commit -m "Relevant message"

```

**11.** Push the committed changes in your feature branch to your remote repo.

```

git push -u origin <your_branch_name>

```

**12.** To create a pull request, click on `compare and pull requests. Please ensure you compare your feature branch to the desired branch of the repository you are supposed to make a PR to.

**13.** Add an appropriate title and description to your pull request explaining your changes and efforts.

**14.** Click on `Create Pull Request`.

**15** Voila! You have made a PR to Bug Buster's Community Website. Sit back patiently and relax while your PR is reviewed.

<hr>


<h2>Usage :</h2>

    python manage.py makemigrations

    python manage.py migrate

    python manage.py runserver
    
   In your web browser enter the address : http://localhost:8000 or http://127.0.0.1:8000/

## Picture of Project
### Home Page
![image](https://github.com/pratt0007/Drive_BOX/assets/100209212/5ff9ca80-f383-4214-82f8-00e0f8951faf)
### New Post Page
![image](https://github.com/pratt0007/Drive_BOX/assets/100209212/53dc0acb-f6d6-4251-83df-bbbe40da9dcf)
### Profile Page
![image](https://github.com/pratt0007/Drive_BOX/assets/100209212/04c1e09c-ec02-497e-b95a-9de0e37aad49)
### Login Page
![image](https://github.com/pratt0007/Drive_BOX/assets/100209212/d05ca788-6f40-43f1-906a-a26ca4d9d488)
### Register Page
![image](https://github.com/pratt0007/Drive_BOX/assets/100209212/588d939e-f1f8-405d-b4c6-06d4ef7a55f3)




