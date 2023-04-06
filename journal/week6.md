# Week 6 — Deploying Containers

The following information outlines tasks that I've completed for Week 6 of the AWS bootcamp.

1. **[Attended the Livestream](https://www.youtube.com/watch?v=FklBsHWYvWY)**

2. **[Watched Ashish's Amazon ECS Security Best Practices video](https://www.youtube.com/watch?v=zz2FQAk1I28&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=57)**

3. Watched the Week 6-7 - ECS Fargate videos: [Part 1](https://www.youtube.com/watch?v=QIZx2NhdCMI&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=58) [Part 2](https://www.youtube.com/watch?v=HHmpZ5hqh1I&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=59)  

First, I configured a Health Check for RDS and the Flask App via creating a new file called ["test"](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-6-flask/backend-flask/bin/db/test) inside backend-flask/bin/db/ and added a health-check route to [app.py](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-6-flask/backend-flask/app.py). I also created a [health-check](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-6-flask/backend-flask/bin/flask/health-check) script in backend-flask/bin/flask/.

Created a CloudWatch log group titled cruddur1 with 1 day retention using the following code below:
```
aws logs create-log-group --log-group-name cruddur  
aws logs put-retention-policy --log-group-name cruddur --retention-in-days 1`  
```
<img src="https://user-images.githubusercontent.com/20970865/229256748-bd9ff498-d64d-4b9c-8a3f-95584fd9e3ff.PNG" width=600>

Also created an ECS cluster titled cruddur (see above image) using the following code below:

```
aws ecs create-cluster \
--cluster-name cruddur \
--service-connect-defaults namespace=cruddur
```

For the Fargate ECS cluster, I created three repositories and pushed three images (Base, Flask Backend, React Frontend). I also managed to signed into ECR from Gitpod using: 
```
aws ecr get-login-password --region $AWS_DEFAULT_REGION | docker login --username AWS --password-stdin "$AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com".
```
I also created a base repository using the following code below:
```
aws ecr create-repository \
 --repository-name cruddur-python \
 --image-tag-mutability MUTABLE
```
I also created the Flask Backend repository using the following code below:
```
aws ecr create-repository \
 --repository-name backend-flask \
 --image-tag-mutability MUTABLE
```
Alongside setting the path using this code below:
```
export ECR_BACKEND_FLASK_URL="$AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/backend-flask"
echo $ECR_BACKEND_FLASK_URL
```
Created a new directory and file titled aws/task-definitions/backend-flask.json

Set the Parameters for AWS Systems Manager Parameter Store.

I also created the IAM Roles CruddurServiceExecutionRole and CruddurTaskRole using the following codes below:
```
aws iam create-role \
    --role-name CruddurServiceExecutionRole \
    --assume-role-policy-document "{
  \"Version\":\"2012-10-17\",
  \"Statement\":[{
    \"Action\":[\"sts:AssumeRole\"],
    \"Effect\":\"Allow\",
    \"Principal\":{
      \"Service\":[\"ecs-tasks.amazonaws.com\"]
    }
  }]
}"
```
```
aws iam create-role \
    --role-name CruddurTaskRole \
    --assume-role-policy-document "{
  \"Version\":\"2012-10-17\",
  \"Statement\":[{
    \"Action\":[\"sts:AssumeRole\"],
    \"Effect\":\"Allow\",
    \"Principal\":{
      \"Service\":[\"ecs-tasks.amazonaws.com\"]
    }
  }]
}"
```

Also created the SSMAccess policy and attatched it to CruddurTaskRole using the following code below in addition to atattching the CloudWatchFullAccess and AWSXRayDaemonWriteAccess policies:
```
aws iam put-role-policy \
  --policy-name SSMAccessPolicy \
  --role-name CruddurTaskRole \
  --policy-document "{
  \"Version\":\"2012-10-17\",
  \"Statement\":[{
    \"Action\":[
      \"ssmmessages:CreateControlChannel\",
      \"ssmmessages:CreateDataChannel\",
      \"ssmmessages:OpenControlChannel\",
      \"ssmmessages:OpenDataChannel\"
    ],
    \"Effect\":\"Allow\",
    \"Resource\":\"*\"
  }]
}
```
```
aws iam attach-role-policy --policy-arn arn:aws:iam::aws:policy/CloudWatchFullAccess --role-name CruddurTaskRole
aws iam attach-role-policy --policy-arn arn:aws:iam::aws:policy/AWSXRayDaemonWriteAccess --role-name CruddurTaskRole
```
I also registered the tasks definitions, set the Default VPC and created a Security Group called crud-srv-sg.

After that, I created a backend-flask container in my ECS cluster:

<img src="https://user-images.githubusercontent.com/20970865/230449456-28726baa-09e1-4a38-b195-cceaa3b0cc56.PNG" width=600>

After creating the service-backend-flask.json file in the aws/json folder, populating it with the appropriate security groups and subnets and installing the Session Manager Plugin, I successfully connected to the backend container via the following code below:
```
aws ecs execute-command  \
--region $AWS_DEFAULT_REGION \
--cluster cruddur \
--task [your aws ecs container task arn here] \
--container backend-flask \
--command "/bin/bash" \
--interactive
```






