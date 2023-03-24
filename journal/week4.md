# Week 4 — Postgres and RDS

The following information outlines tasks that I've completed for Week 4 of the AWS bootcamp.

1. [Attended the Livestream](https://www.youtube.com/watch?v=EtD7Kv5YCUs)

2. [Watched Ashish's Week 4 - Security Considerations	video](https://www.youtube.com/watch?v=UourWxz7iQg&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=45)

3. Create RDS Postgres Instance	

Setup an RDS instance using Gitpod, using the proper instanace class, password, avaialbility zone, and port. During the livestream I placed a temporary stop on the RDS instance. Also reated the "backend-flask/db" directory and "schema.sql" file, using the "psql cruddur < db/schema.sql -h localhost -U postgres" command to import the script.

<img src="https://user-images.githubusercontent.com/20970865/225889658-c4b68ae6-21db-4adc-bb84-96af8705acfa.PNG" width=450>

4. Bash scripting for common database actions	

Created the db-drop, db-create, db-schema-load, db-seed, and db-setup bash scripts, along with creating a db-sessions script which displays processes that are running. 
Folder: [backend-flask/bin](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/tree/week-4/backend-flask/bin)

5. Install Postgres Driver in Backend Application	

Succesfully installed the psycopg Postgres driver by adding it to the [requirements.txt](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-4/backend-flask/requirements.txt) file and running pip install via the backend-flask directory.

6. Connected Gitpod to an RDS Instance	

Succesfully connected to AWS RDS from Gitpod. Created the [rds-update-sg-rule](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-4/backend-flask/bin/rds-update-sg-rule) batch script to account for dynamic IP addresses for security group values.

7. Created Congito Trigger to insert user into database	

Created the "cruddur-post-confirmation" Lamda function. Also, when adding a [Lambda layer](https://github.com/jetbridge/psycopg2-lambda-layer), please make sure that you're using the proper ARN for your region. To test that the Lambda function is working, the account needs to be removed from the Cruddur user pool via AWS Cognito and then recreated via Cruddur.

<img src="https://user-images.githubusercontent.com/20970865/225892292-e8f30d42-17b5-48b4-9226-3f7c8ad5b91b.PNG" width=650>

8. Created new activities with a database insert	

Sucessfully managed to post a Crud into the AWS database. Files altered: [db.py](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-4-activities/backend-flask/lib/db.py), [create_activity.py](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-4-activities/backend-flask/services/create_activity.py), [home_activity.py](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-4-activities/backend-flask/services/home_activities.py), [app.py](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-4-activities/backend-flask/app.py) and [cruddur-post-confirmation.py](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-4-activities/aws/lambdas/cruddur-post-confirmation.py)
