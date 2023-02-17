# Week 0 — Billing and Architecture

1. [Watched Week 0 - Live Streamed Video](https://www.youtube.com/watch?v=SG8blanhAOg&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=12)

2. [Watched Chirag's Week 0 - Spend Considerations](https://www.youtube.com/watch?v=OVw3RrlP-sI&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=13)

3. [Watched Ashish's Week 0 - Security Considerations](https://www.youtube.com/watch?v=4EMWBYVggQI&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=15)


4. Cruddur Conceptual Diagram

Napkin:

<img src="https://user-images.githubusercontent.com/20970865/219132185-aaed0b6b-48a6-447b-8562-0c2a4427fdee.png" width="600">
 
Digital: [Lucid Charts](https://lucid.app/lucidchart/e8d15aeb-03a3-43e4-995b-80fd7c7a81b2/edit?invitationId=inv_213bb306-f3e1-4672-91c3-6b59d3e53874&page=0_0#)

<img src="https://user-images.githubusercontent.com/20970865/219132946-522055fc-a13c-47bf-95b1-34c5b55df973.PNG" width="800">

5. Cruddur Logical Diagram [Lucid Charts](https://lucid.app/lucidchart/58f8718e-60e1-4d51-9370-0f012dce6c20/edit?beaconFlowId=60CF032ACD2A333E&invitationId=inv_3d8eee70-0637-4958-aa89-9e37fe14b43a&page=0_0#)

<img src="https://user-images.githubusercontent.com/20970865/219141304-a23defc4-8fa9-437c-9f12-626976f890e5.PNG" width="700">

6. Create Admin User

Already had a root account prior to making an admin account. Enabled MFA on both accounts.

Homework Challenge: destroyed my root account credentials by resetting the password.

7. Use CloudShell

![cloudshellsts](https://user-images.githubusercontent.com/20970865/219497533-9553ab7d-d92c-4366-9260-a396c4ac49b7.PNG)

8. Generate AWS Credentials

Generated them for use in the CLI.

9. Installed AWS CLI

Installed it via gitpod

![gitpod1](https://user-images.githubusercontent.com/20970865/219440192-4a87abbe-1b09-4d7a-bb27-a6955ba31646.PNG)

10. Create Billing Alarm

Followed the instructions in [Chirag's Week 0 video](https://www.youtube.com/watch?v=OVw3RrlP-sI&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=13)

<img src="https://user-images.githubusercontent.com/20970865/219521544-d5539c40-aa20-49ef-b2a1-84b0da90bc33.PNG" width="700">


11. Create a Budget

Created one sample budget.

<img src="https://user-images.githubusercontent.com/20970865/219521568-b28f446e-a28e-453e-8f29-60b28a07d472.PNG" width="700">

Homework Challenges

- Destroy your root account credentials, Set MFA, IAM role - Completed
- Use EventBridge to hookup Health Dashboard to SNS and send notification when there is a service health issue.
- Review all the questions of each pillars in the Well Architected Tool (No specialized lens) - Completed
- Create an architectural diagram (to the best of your ability) the CI/CD logical pipeline in Lucid Charts - [Completed](https://lucid.app/lucidchart/950d9ac5-f9e8-4406-962d-b5f1e4e2601b/edit?beaconFlowId=4490EB0FEFB8BF7B&invitationId=inv_7ca6fc7a-50b0-430f-9e7e-71670d503dce&page=0_0#)
  <img src="https://user-images.githubusercontent.com/20970865/219716206-193d07d6-0489-4161-95f9-abe93a3bb0fe.PNG" width="600">
- Research the technical and service limits of specific services and how they could impact the technical path for technical flexibility.
- Open a support ticket and request a service limit
