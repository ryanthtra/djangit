# djangit
A simple Reddit-like website built with the Django Python web framework.

You can find the site running at http://ryanthtra.eastus.cloudapp.azure.com.  The site is running on a Linux Ubuntu 18.04 virtual machine in Microsoft Azure using Gunicorn web server and Nginx reverse proxy.

The site has the following pages:

Page Name | Description
----------|------------
Home | Displays all posts in existence.
New Post  | Displays a form to create a new post.
User's Posts | Displays all posts posted by a specific user.
Signup | Displays a form to create a new user.
Login | Displays a form to log in an existing user.

## Other notes
- Displayed posts can be voted up or down.
  - Currently, votes are not restricted to logged in users, nore are they restricted to one vote per user/guest.
- A user's posts page can be accessed by clicking on a post's author's name.
- Forms are currently just basic HTML forms.  Future tweaks would include implementing Django Forms, though the csrf_token template tag is already being used.
- There is currently no pagination, so theoretically, the Home Page could end up getting ridiculously long.
