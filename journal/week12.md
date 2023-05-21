# Week 12 — Modern APIs

**Week X - Cleanup**
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
