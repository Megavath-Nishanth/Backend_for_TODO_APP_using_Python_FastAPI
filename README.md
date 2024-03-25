# Backend_for_TODO_APP_using_Python_FastAPI

This is a simple backend application for to-do app using python and fastapi.
It includes endpoints that require user authentication.
The application has CRUD (Create,Read,Update,Delete) Operations.


# Installation

Clone the Repositary or Copy the code into a new folder (for example: todoapp).

To clone,use the following command:

```
git clone https://github.com/Megavath-Nishanth/Backend_for_TODO_APP_using_Python_Fastapi.git
```

If you are copying the codes and pasting into the files,use the same file names to get the clarity.

# Navigating to the directory

Navigate to the folder which you have created(i am assuming the folder name as todoapp,which was mentioned above).
you can navigate by using the command.

```
cd todoapp
```

# Installation of Requirements

After changing the directory,firstly change the directory to:

```
cd todo
```

Followed by this command to install the requirements.

```
pip3 install -r requirements.txt
```

After the installation, go back to previous directory by using commands.

```
cd
```

Followed by this command.

```
cd todoapp
```

# How to run the application

1.Check whether you are in the right directory which is ```/todoapp``` or else change the directory.
   Now to run the applcation use the following command in the terminal.

```
uvicorn todo.main:app --reload
```

This will start the FastApi server on ```http://localhost:8000``` by default.

2.Open your browser and go to ```http://localhost:8000/docs``` to access the ```Swagger UI``` for testing the API endpoints.

3.You can use tools like ```TablePlus``` or ```Postman``` application to check whether the API endpoints and database working or not.

# API Endpoints

## Authentication

- ```POST /login``` Login
  
  **Description:**
  
  In this endpoint,User need to authenticate by providing username (which is email) and password.

  If the credentials match,you can use the CRUD operrations on the Todos.
  
  If the credentials don't match with the saved credentials,it displays as ```Invalid Credentials```.

  **Parameters:**
  
  username: email of the user
    
  password: Password of the user

## Todos

- ```GET /todo/``` All

  **Description:**

  Retrives the tasks of the user.

  **Authentication required:** Yes.

- ```POST /todo/``` Create

  **Description:**

  Creates a new task for the user.

  **Parameters:**

  task: Description of the task.

  **Authentication required:** Yes.

- ```DELETE /todo/{id}``` Destroy

  **Description:**

  Deletes a task by id.

  **Parameters:**

  id: id of the task to be deleted.

  **Authentication required:** Yes.

- ```PUT /todo/{id}``` Update

  **Description:**

  Updates the task.

  **Parameters:**

  id: id of the task to be updated.

  **Authentication required:** Yes.

- ```GET /todo/{id}``` Show

  **Description:**

  Retrives the task of a particular id.

  **Parameters:**

  id: id of the task to be retrived.

  **Authentication required:** Yes.

## Users

- ```POST /user/``` Create User

  **Description:**

  Creates a new user.

  **Parameters:**

  name: Name of the new user.

  email: Email of the new user.

  password: Password of the new user.

  **Authentication required:** No.

- ```GET /user/{id}``` Get User

  **Description:**

  Retrives all the tasks by a user id.

  **Parameters:**

  id: id of the user.

  **Authentication required:** No.


  
  
