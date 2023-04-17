# Week 8 — Serverless Image Processing

The following information outlines tasks that I've completed for Week 8 of the AWS bootcamp.

1. **[Attended the Livestream](https://www.youtube.com/watch?v=YiSNlK4bk90&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=70&pp=iAQB)**

2. **[Week 8 - Serverless Image Process CDK](https://www.youtube.com/watch?v=jyUpZP2knBI&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=71&pp=iAQB)**

    I configured the env vars, the s3 bucket and permissions, the lambda, and the SNS. I also setup CloudFront to log the image process.

3. **[Implemented the Users Profile Page](https://www.youtube.com/watch?v=WdVPx-LLjQ8&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=73&pp=iAQB)** by following Andrew's instructions in the linked video. Files created: [ProfileHeading.css](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-8-fix-cors/frontend-react-js/src/components/ProfileHeading.css), [ProfileHeading.js](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-8-fix-cors/frontend-react-js/src/components/ProfileHeading.js), [EditProfileButton.css](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-8-fix-cors/frontend-react-js/src/components/EditProfileButton.css), and [EditProfileButton.js](https://github.com/Gamerrethink/aws-bootcamp-cruddur-2023/blob/week-8-fix-cors/frontend-react-js/src/components/EditProfileButton.js)

4. **[Implemented Migrations Backend Endpoint and Profile Form](https://www.youtube.com/watch?v=PTafksks528&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=74&pp=iAQB)** by following Andrew's instructions in the linked video. I configured the migration and rollback database functions and setup the popup form to capture bio information. Please be sure to use your own handle when viewing and editing your profile, otherwise your information won't save in the right spot.

5. **[Implemented Avatar Uploading](https://www.youtube.com/watch?v=Bk2tq4pliy8&t=5011s)** by implementing the client side upload for the "Edit Profile" popup. I also leveraged my API gateway and installed aws jwt verify using `npm install aws-jwt-verify --save`.

6. **[Attempted to fix CORS for the API gateway](https://www.youtube.com/watch?v=eO7bw6_nOIc&t=389s)** by following Andrew's instructions in the linked video, and while the preflight optin is working fine, the CORS error still appears in the console. I managed to get that fixed following Andrew's insturctions in [the video after that](https://www.youtube.com/watch?v=xrFo3QLoBp8&t=16s), alongside creating a JWT lambda layer.

7. **[Rendered the avatar](https://www.youtube.com/watch?v=xrFo3QLoBp8&t=16s)** by following Andrew's instructions in the linked video.
