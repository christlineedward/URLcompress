# URLcompress
Project requirements/ desired functionality:

- Allow the user to input a long URL and then receive a generated short, unique code for the URL (Initial question: how long should the short code be?)
- The application should store the long URL and corresponding short code mapping in a database
- When given the short code, the URL shortener application should be able to look up the corresponding long URL in the database and redirect users to the appropriate site
- Allow users to choose their own short codes, as long as they are not allready taken. This could be useful for branding or for creating memorable links
- (Optional): Track the number of clicks on each short code, as well as other analytics data such as the geographic location of users, the type pf device used to access the link, etc.