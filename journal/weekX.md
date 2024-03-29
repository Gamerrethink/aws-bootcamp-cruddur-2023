# Week X - Cleanup

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  

1. [**Attended the Livestream**](https://www.youtube.com/watch?v=Bi_pjuM3u2o&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=111&pp=iAQB)

2. Built up a static frontend in gitpod alongside creating and deploying the sync role in CloudFormation.

    <img src=https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/assets/20970865/6f677371-1e4b-4ce2-901e-d8fbc3cf8dc4 width=800>
    
3. Reconnected the database and updated the [post confimation lambda](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-x-static-frontend/aws/lambdas/cruddur-post-confirmation.py).

    <img src=https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/assets/20970865/0aa945c5-a897-4d64-9623-ac5b2159a952 width=800>

4. Updated the [config.toml file](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-x-refactoring/aws/cfn/service/config.toml) in aws/cfn/service and the [service file](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-x-refactoring/bin/cfn/service) in bin/cfn to fix the CORS issue.

5. Fixed up the CI/CD pipeline for CFN which is now fully working.

    <img src=https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/assets/20970865/e6df7c2c-9eb2-41e7-93b5-ff196c94930e width=800>

6. Refractored [cognito_jwt_token.py](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-x-refactoring/backend-flask/lib/cognito_jwt_token.py) to use a decorator.

7. Refactored flask and [app.py](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-x-refactoring/backend-flask/app.py). Created new files inside the [backend-flask/llb](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/tree/week-x-refactoring/backend-flask/lib) folder and created a new [backend-flask/routes](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/tree/week-x-refactoring/backend-flask/routes) folder alongside some files.

8. Implemented the reply function. When I was troubleshooting, I kept getting an AttibuteError, followed by a "LINE 27: replies.reply_to_actvitiy_uuid = activities.uuid" error after further troubleshooting. 

   My solution was copying and pasting the following commands manually inside gitpod (courtesy of the uuid_to_string.py file inside the db/migrations folder) after using the ./bin/db/connect command.

    `ALTER TABLE activities DROP COLUMN reply_to_activity_uuid;`
    
    `ALTER TABLE activities ADD COLUMN reply_to_activity_uuid uuid;`
    
    <img src=https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/assets/20970865/a6fc4e17-3d56-47d9-8ce7-0c7c174faedb width=800>

9. Refactored the error handling and fetch requests.

10. Refactored the Activity Show page. 

11. Did some cleanup alongside implementing timezone fixes.

12. Did some more cleanup on the frontend side of things alongside fixing an issue on the backend related to messaging which took a ton of troubleshooting.

    <img src=https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/assets/20970865/fb8cd01e-f7c3-477d-a7e8-fedbc97aabb4 width=800>

**Bootcamp Complete**: The completed application can be found at [https://cruddr.click](https://cruddr.click).
