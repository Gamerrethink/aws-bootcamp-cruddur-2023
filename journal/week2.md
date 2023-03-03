# Week 2 — Distributed Tracing

The following information outlines tasks that I've completed for Week 2 of the AWS bootcamp.

1. [Attended the Livestream](https://www.youtube.com/watch?v=2GD9xCzRId4&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=30)

2. [Watched Ashish's Week 2 - Observability Security Considerations](https://www.youtube.com/watch?v=bOf4ITxAcXc&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=31)

4. [Watched Chirag Week 2 - Spending Considerations](https://www.youtube.com/watch?v=2W3KeqCjtDY&list=WL&index=6&t=3s)

5. [Instrument Honeycomb with OTEL](https://www.youtube.com/watch?v=2GD9xCzRId4&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=30)	

Integrated Honeycomb into the Cruddur application. Configured tracing and a custom span in the [home activities](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-2/backend-flask/services/home_activities.py) file. 

6. [Instrument AWS X-Ray](https://www.youtube.com/watch?v=n2DTsuBrD_A&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=32)	

Integrated AWS X-ray into the Cruddur application. Configured tracing, a custom segment and a custom subsegment in the [home activities](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-2/backend-flask/services/home_activities.py) file. 

7. [Configure custom logger to send to CloudWatch Logs](https://www.youtube.com/watch?v=ipdFizZjOF4&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=33)

Integrated AWS CloudWatch logs into the Cruddur application. Files: [home activities](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-2/backend-flask/services/home_activities.py) and [app.py](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-2/backend-flask/app.py).

<img src="https://user-images.githubusercontent.com/20970865/222496797-f7880d62-9720-4221-81e3-e48fbc4a6111.PNG" width="600">

8. [Instrumented Rollerbar](https://www.youtube.com/watch?v=xMBDAb5SEU4&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=35)

Instrumented Rollbar into the Cruddur app. Files: [app.py](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-2/backend-flask/app.py), [requirements.txt](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-2/backend-flask/requirements.txt), and [docker-compose.yml](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-2/docker-compose.yml).

<img src="https://user-images.githubusercontent.com/20970865/222561987-2b44ed34-1039-4086-9241-9dc36fb2b7bd.PNG" width="800">

**Homework Stretch Assignments**

- Added a custom span "home-activities..." for home activities. Reference "#Honeycomb" in the [home activities](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-2/backend-flask/services/home_activities.py) file. 

<img src="https://user-images.githubusercontent.com/20970865/222497770-52e89823-1bb5-4b07-8ace-c1a588f70369.PNG" width="1000">

- Also added two attributes to the custom span (app.now = time stamp and app.result_length)

