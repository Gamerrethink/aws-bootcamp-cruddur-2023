# Week 5 — DynamoDB and Serverless Caching

The following information outlines tasks that I've completed for Week 5 of the AWS bootcamp.

1. [Attended the Livestream](https://www.youtube.com/watch?v=5oZHNOaL8Og)

2. Watched [Ashish's Week 5 - DynamoDB Considerations](https://www.youtube.com/watch?v=gFPljPNnK2Q&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=52) video	

3. Implemented DynamoDB

First, I installed boto3 by adding it to the [requirements.txt](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-5/backend-flask/requirements.txt) file and subsequently running the pip intall -r requirments.txt command, which I added to my [.gitpod.yml](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-5/.gitpod.yml) file so that it runs automatically every time the workspace starts up.

In setting up the local DynamoDB, I created a schema to build the "cruddur-messages" table, seed it with mock data, then scanned it to check that the database displayed the data and was functioning properly.
