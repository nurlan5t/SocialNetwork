Test task: Python Developer
1. Social Network
Object of this task is to create a simple REST API. You can use one framework from this list
(Django Rest Framework, Flask or FastAPI) and all libraries which you are prefer to use with
this frameworks.

Executor: Nurlan Toktobekov

Date: 2021-06-15

Basic models:

● User

    users/models

● Post (always made by a user)

    posts/models

Basic Features:

● user signup

    http://127.0.0.1:8000/api/auth/users/
    body'
        {"username":"username", "password":"password"}

● user login

    http://127.0.0.1:8000/api/token/
    body:
        {"username":"username", "password":"password"}

● post creation

    http://127.0.0.1:8000/api/posts/create
    (in Postman) Headears: Authorization 
    Bearer ("access":token) 

● post like

    http://127.0.0.1:8000/api/likes/create
    body:
        {"post":1, "like":1}

● post unlike

    http://127.0.0.1:8000/api/likes/create
    body:
        {"post":1, "like":2}

● analytics about how many likes was made. Example url
/api/analitics/?date_from=2020-02-02&date_to=2020-02-15 . API should return analytics
aggregated by day.
    
    http://127.0.0.1:8000/api/likes/all?date_from=2021-06-15&date_to=2021-06-16

● user activity an endpoint which will show when user was login last time and when he
mades a last request to the service.

    http://127.0.0.1:8000/api/users/all

Requirements:

● Implement token authentication (JWT is prefered)

    ✓✓✓


Notes:

● Clean and usable REST API is important

● the project is not defined in detail, the candidate should use their best judgment for every
non-specified requirements (including chosen tech, third party apps, etc), however

● every decision must be explained and backed by arguments in the interview

● Result should be sent by providing a Git url. This is a mandatory requirement.
   
    ✓✓✓