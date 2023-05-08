# Week 10 — CloudFormation Part 1

The following information outlines tasks that I've completed for Week 10 of the AWS bootcamp.

1. **[Attended the Livestream](https://www.youtube.com/watch?v=BRmEG4zicM0&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=85&pp=iAQB)**

2. Created a networking layer for CFN by creating the [template.yaml file](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-10-cfn-networking/aws/cfn/networking/template.yaml) in aws/cfn/networking. Deploying didn't work at first after adding everything that was needed, but adding custom YAML code into the settings.json file helped it succeed.

3. **[Created a networking diagram in Lucid Charts](https://lucid.app/lucidchart/bc3276ff-b0bb-4de7-952c-5ef95aac30d9/edit?invitationId=inv_c87816b2-fd6e-464f-bcb3-043ee7a0f891)**

     <img src=https://user-images.githubusercontent.com/20970865/234123667-a0ed2735-9a85-46ca-94ee-d75a770ab465.jpeg width=600>

4. Created a cluster layer for CFN alongside adding the config.toml file.

5. Updated the diagram to include cluster related stuff.

    <img src=https://user-images.githubusercontent.com/20970865/236802216-8a60a5a6-7a83-4ed4-8adb-f1f1c6b75277.jpeg width=800>
    
6. Created a service layer for CFN. Executing the changeset didn't work at first because the stack wasn't detecting the namespace "cruddur". Creating a new namespace via CloudMap and adjusting the template.yaml file helped fix the issue.
