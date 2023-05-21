# Week 10 — CloudFormation Part 1

The following information outlines tasks that I've completed for Week 10 of the AWS bootcamp.

1. **[Attended the Livestream](https://www.youtube.com/watch?v=BRmEG4zicM0&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=85&pp=iAQB)**

2. Watched **[Ashish's Amazon CloudFormation Security Best Practices](https://www.youtube.com/watch?v=ctYnoDo5tWE&t=703s)** video.

3. Created a networking layer for CFN by creating the [template.yaml file](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-10-cfn-networking/aws/cfn/networking/template.yaml) in aws/cfn/networking. Deploying didn't work at first after adding everything that was needed, but adding custom YAML code into the settings.json file helped it succeed.

4. **[Created a networking diagram in Lucid Charts](https://lucid.app/lucidchart/bc3276ff-b0bb-4de7-952c-5ef95aac30d9/edit?invitationId=inv_c87816b2-fd6e-464f-bcb3-043ee7a0f891)**

     <img src=https://user-images.githubusercontent.com/20970865/234123667-a0ed2735-9a85-46ca-94ee-d75a770ab465.jpeg width=600>

5. Created a cluster layer for CFN alongside adding the config.toml file.

6. Updated the diagram to include cluster related stuff.

    <img src=https://user-images.githubusercontent.com/20970865/236802216-8a60a5a6-7a83-4ed4-8adb-f1f1c6b75277.jpeg width=800>
    
7. Created a service layer for CFN. Executing the changeset didn't work at first because the stack wasn't detecting the namespace "cruddur". Creating a new namespace via CloudMap and adjusting the template.yaml file helped fix the issue. 

8. Created and deployed an RDS layer for CFN.

   <img src=https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/assets/20970865/e7b332d5-34ad-4676-aa22-3ee6b68224fb width=800>
   
9. The CFN cluster, which came up in ECS when executing the changeset for the service layer, wasn't quite working at first because the health check kept failing. Adjusting the health-check settings to Override Port 4567 in the backend-flask target group fixed the issue.

   <img src=https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/assets/20970865/76221bb5-43e1-4fa3-a255-a5b6fc0110c0 width=800>

10. Updated the diagram to include service, RDS and DynamoDB related stuff.

   <img src=https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/assets/20970865/9d3d9644-a2c8-4c4a-b025-42cd7c926751 width=800>

11. Created and deployed a DynamoDB stack to CloudFormation.

    <img src=https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/assets/20970865/c570963a-73e0-47d1-b172-b447e9be5d15 width=800>

12. Created and deployed a frontend stack to CloudFormation.

    <img src=https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/assets/20970865/455c5d5b-d5a4-4059-bc82-c08645dc7c1c width=800>

13. Updated the diagram to include frontend stuff.

    <img src=https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/assets/20970865/8956bb05-2f40-4e5f-9ad6-f3e67d23883c width=800>
    
**Week X**
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    
1. Built up a static frontend in gitpod alongside creating and deploying the sync role in CloudFormation.

    <img src=https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/assets/20970865/6f677371-1e4b-4ce2-901e-d8fbc3cf8dc4 width=800>
    
2. Reconnected the database and updated the [post confimation lambda](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-x-static-frontend/aws/lambdas/cruddur-post-confirmation.py).

    <img src=https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/assets/20970865/0aa945c5-a897-4d64-9623-ac5b2159a952 width=800>

3. Updated the [config.toml file](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-x-refactoring/aws/cfn/service/config.toml) in aws/cfn/service and the [service file](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-x-refactoring/bin/cfn/service) in bin/cfn to fix the CORS issue.

4. Fixed up the CI/CD pipeline for CFN which is now fully working.

    <img src=https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/assets/20970865/e6df7c2c-9eb2-41e7-93b5-ff196c94930e width=800>

5. Refractored [cognito_jwt_token.py](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-x-refactoring/backend-flask/lib/cognito_jwt_token.py) to use a decorator.

6. Refactored flask and [app.py](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-x-refactoring/backend-flask/app.py). Created new files inside the [backend-flask/llb](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/tree/week-x-refactoring/backend-flask/lib) folder and created a new [backend-flask/routes](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/tree/week-x-refactoring/backend-flask/routes) folder alongside some files.
