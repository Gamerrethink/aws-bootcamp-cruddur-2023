INSERT INTO public.users (display_name, email, handle, cognito_user_id)
VALUES
  ('Andrew Brown','andrew@exampro.co' , 'andrewbrown' ,'MOCK'),
  ('Andrew Bayko','bayko@exampro.co' , 'bayko' ,'MOCK'),
  ('Marquis Brown' , 'marquismb.mb@gmail.com' , 'awsbootcamp' , 'MOCK'),
  ('Marquis' , 'marquismb@hotmail.com' , 'awsbootcampalt' , 'MOCK'),
  ('Londo Mollari','lmollari@centari.com' ,'londo' ,'MOCK');
INSERT INTO public.activities (user_uuid, message, expires_at)
VALUES
  (
    (SELECT uuid from public.users WHERE users.handle = 'andrewbrown' LIMIT 1),
    'This was imported as seed data!',
    current_timestamp + interval '10 day'
  ),
  (
    (SELECT uuid from public.users WHERE users.handle = 'awsbootcampalt' LIMIT 1),
    'I am the other!',
    current_timestamp + interval '10 day'
  );