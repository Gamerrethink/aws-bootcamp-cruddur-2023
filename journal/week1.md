# Week 1 — App Containerization

1. [Watched How to Ask for Technical Help](https://www.youtube.com/watch?v=tDPqmwKMP7Y&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=30)

2. [Watched Grading Homework Summaries](https://www.youtube.com/watch?v=FKAScachFgk&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=25)

3. [Watched Week 1 - Live Streamed Video](https://www.youtube.com/watch?v=zJnNe5Nv4tE&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=22)

4. Remember to Commit Your Code	

   I committed my code during the livestream.

5. [Watcked Chirag's Week 1 - Spending Considerations	](https://www.youtube.com/watch?v=OAMHu1NiYoI&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=24)

6. [Watched Ashish's Week 1 - Container Security Considerations](https://www.youtube.com/watch?v=OjZz4D0B-cA&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=26)

7. Containerize Application (Dockerfiles, Docker Compose)

   Containerized my application during the livestream. The first time I tried containerizing the app, it didn't work. It took retracing my steps to realize I forgot        to set the enviorment variables. Files: [Frontend](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-1/frontend-react-js/dockerfile), [Backend](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-1/backend-flask/dockerfile), and [Composer](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-1/docker-compose.yml) 
   
8. Document the Notification Endpoint for the OpenAI Document	
Started the containers for Cruddur and created an account in the app. Documented the notification endpoint OpenAI document by updating the file [openapi-3.0.yml](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-1/backend-flask/services/notifications_activities.py).

9. Write a Flask Backend Endpoint for Notifications and Write a React Page for Notifications	

Activated the notifications feature by writing a Flask backend endpoint and writing a react page for notifications. Files: [app.js](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-1/frontend-react-js/src/App.js), [app.py](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-1/backend-flask/app.py), and [notification_activities.py](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-1/backend-flask/services/notifications_activities.py).

10. Run DynamoDB Local Container and Run Postgres Container and ensure they both work

Updated [docker-compose.yml](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-1/docker-compose.yml) to support both the DynamoDB and Postgres databases. Also updated [.gitpod.yml](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-1/.gitpod.yml) to launch postgres during workspace startup.

Homework Challenges

May need some more time to work on these. Updates for these challenges will be ongoing.
