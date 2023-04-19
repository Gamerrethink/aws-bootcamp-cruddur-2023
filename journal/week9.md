# Week 9 — CI/CD with CodePipeline, CodeBuild and CodeDeploy

The following information outlines tasks that I've completed for Week 9 of the AWS bootcamp.

1. **[Attended the Livestream](https://www.youtube.com/watch?v=DLYfI0ehMZE&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=81&pp=iAQB)**

2. Setup CodeBuild, created a prod branch in GitHub and created the buildspec.yml file. The CodeBuild process didn't work at first but I later realized it was because I didn't attach a few ECR policies to the service role. After adding all those the build executed successfully.

     <img src=https://user-images.githubusercontent.com/20970865/233215886-df93eba0-4edb-47ef-a668-d40ed9f0b501.PNG width=700>

3. **[Setup CodePipeline](https://www.youtube.com/watch?v=EAudiRT9Alw&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=83&pp=iAQB)** by following Andrew's instructions in the linked video. At first, deploying wasn't working because of a problem I ran into back in week 6-7 regarding the task definition for backend-flask. After some troubleshooting I realized that it was because I forgot to re-register the task definition with the new health-check path. My CodePipeline deployed successfully after making that adjustment.

      <img src=https://user-images.githubusercontent.com/20970865/233216000-b838c6f9-68c8-48c6-bb58-e1637087148c.PNG width=700>
