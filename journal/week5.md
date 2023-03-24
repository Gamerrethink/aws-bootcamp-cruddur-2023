# Week 5 — DynamoDB and Serverless Caching

The following information outlines tasks that I've completed for Week 5 of the AWS bootcamp.

1. **[Attended the Livestream](https://www.youtube.com/watch?v=5oZHNOaL8Og)**

2. **Watched [Ashish's Week 5 - DynamoDB Considerations](https://www.youtube.com/watch?v=gFPljPNnK2Q&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=52) video.**	

3. **Implemented DynamoDB**

First, I installed boto3 by adding it to the [requirements.txt](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-5/backend-flask/requirements.txt) file and subsequently running the pip intall -r requirments.txt command, which I added to my [.gitpod.yml](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-5/.gitpod.yml) file so that it runs automatically every time the workspace starts up.

In setting up the local DynamoDB, I created a schema to build the "cruddur-messages" table, seed it with mock data, then scanned it to check that the database displayed the data and was functioning properly.

4. **Implement Schema Load, Seed and Scan Scripts**

Created the schema-load, seed and scan files in the [/bin/ddb](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/tree/week-5/backend-flask/bin/ddb) folder.

5. **Implement Pattern Scripts for Read and List Conversations**	

Created a folder in /bin/ddb/ called patterns and created the [get-conversation](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-5/backend-flask/bin/ddb/patterns/get-conversation) and [list-conversations](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-5/backend-flask/bin/ddb/patterns/list-conversations). For a while I had trouble getting the latter file to work because when I would try to run it, it would give me a NoneType error. I eventually got it to work after doing some troubleshooting.

6. **Implement Update Cognito ID Script for Postgres Database**	

Added the file update_cognito_user_ids to [/bin/db](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-5/backend-flask/bin/db/update_cognito_user_ids). Was having trouble getting this file working the way it was supposed to at first, but got it working following some more troubleshooting.

7. **Implement (Pattern A) Listing Messages in Message Group into Application**	

<img src="https://user-images.githubusercontent.com/20970865/227585816-47e24b71-7e36-4044-b394-42a8e6aef061.PNG" width=550>

This one took nearly three days worth of troubleshooting, which at first was seemingly related to the hardcoded stuff in the database, but I eventually got it working.

8. **Implement (Pattern B) Listing Messages Group into Application**	

Same as the above in regards to troubleshooting, except I also had to deal with a 500 error popping up in the Chrome console. I eventually got this pattern working as well.

9. **Implement (Pattern C) Creating a Message for an existing Message Group into Application**

At the time I implemented this pattern and Pattern D, Pattern C wasn't working the way it was supposed to. 
In Cruddur, whenever I sent a message, the page redirected with no new message appearing at the bottom.
Altering line 233 in [/bin/ddb/seed](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-5/backend-flask/bin/ddb/seed) fixed the issue.

<img src="https://user-images.githubusercontent.com/20970865/227584748-8530ce0a-34f5-427c-ab67-6015a2145a54.PNG" width=550>

10. **Implement (Pattern D) Creating a Message for a new Message Group into Application**	

Was able to successfully implement this pattern with no errors after some troubleshooting.

11. **Implement (Pattern E) Updating a Message Group using DynamoDB Streams**	

Created a cruddur-messaging-stream lambda in AWS along with the DynamoDB table cruddur-messages.

<img src="https://user-images.githubusercontent.com/20970865/227585641-36af4fc9-dc90-4f17-aa06-659ae82eb9ec.PNG" width=750>

<img src="https://user-images.githubusercontent.com/20970865/227585680-cf17c766-28c3-4a4b-aeed-beb235b5bec6.PNG" width=750>


