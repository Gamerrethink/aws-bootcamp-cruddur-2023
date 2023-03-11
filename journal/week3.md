# Week 3 — Decentralized Authentication

The following information outlines tasks that I've completed for Week 3 of the AWS bootcamp.

1. [Attended the Livestream](https://www.youtube.com/watch?v=9obl7rVgzJw&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=40)

2. [Watched Ashish's Week 3 - Decenteralized Authentication video](https://www.youtube.com/watch?v=tEJIeII66pY&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=39)

3. [Watch Chirag Week 3 - Spending Considerations]()

4. [Watch about different approaches to verifying JWTs](https://www.youtube.com/watch?v=nJjbI4BbasU&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=43)

5. Setup Cognito User Pool

Set up a custom user pool in AWS Cognito with the right attributes.

<img src=https://user-images.githubusercontent.com/20970865/224400181-dde03d8e-b591-4f4e-9734-be9d363dd5f2.PNG width="250">

6. Implement Custom Signin And Confirmation Pages	

Implemented a custom signin page leveraging AWS Cognito. Tested and confirmed login. Files changed: [docker-compose.yml](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-3/docker-compose.yml), [app.js](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-3/frontend-react-js/src/App.js), [HomeFeedPage.js](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-3/frontend-react-js/src/pages/HomeFeedPage.js), [SigninPage.js](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-3/frontend-react-js/src/pages/SigninPage.js), and [ConfirmationPage.js](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-3/frontend-react-js/src/pages/ConfirmationPage.js).

<img src=https://user-images.githubusercontent.com/20970865/224401526-c8e0f353-63cf-4e68-afa5-72a883cf2ebc.PNG width="450">

7. Implement Custom Signup Page	

Implemented a custom signup page. Tested and confirmed signup and login. Files changed: [ConfirmationPage.js](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-3/frontend-react-js/src/pages/ConfirmationPage.js), [SignupPage.js](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-3/frontend-react-js/src/pages/SignupPage.js), [docker-compose.yml](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-3/docker-compose.yml) and other files reflected in this journal.

<img src="https://user-images.githubusercontent.com/20970865/224412439-fb0ea01e-3e2d-4b67-aac2-7ba0f35c912d.PNG" width="850">

8. Implement Custom Recovery Page	

Implemented a custom recovery page Fileschanged: [ConfirmationPage.js](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-3/frontend-react-js/src/pages/ConfirmationPage.js) and [RecoveryPage.js](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-3/frontend-react-js/src/pages/RecoverPage.js). Tested and confirmed login with new password.

<img src="https://user-images.githubusercontent.com/20970865/224412453-c0ac3f54-4928-4e15-b412-29f2c8e3e643.PNG" width="850">

Implement Server Side Verifications with JSON Web Tokens

Implemented user authentication using JSON Web Token on the backend as detailed in [Andrew's Week 3 Congito JWT Server side Verify](https://www.youtube.com/watch?v=d079jccoG-M&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=42) video. Created a token file. Files changed: [home_activities.py](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/main/backend-flask/services/home_activities.py), [docker-compose.yml](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-3/docker-compose.yml) and etc. as relfected in this very journal.

Homework Strech Assignments:

Implemented UI changes (This is not listed in either the Course Outline or the Student Portal Checklist)

Implemented UI chages using CSS as detailed in [Andrew's Week 3 Improving UI Contrast and Implementing CSS Variables for Theming](https://www.youtube.com/watch?v=m9V4SmJWoJU&list=WL&index=5&t=72s) video.

NOTE: Watched the [Week 2 X-Ray Subsegments Solved](https://www.youtube.com/watch?v=4SGTW0Db5y0&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=38) video as it was added after I submitted my Week 2 homework summary. Made and tested the suggested changes succesfully.
