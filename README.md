# Silvano-s-Portfolio
My Portfolio

This is a virtual portfolio where I can upload my projects, education, and goals. Starting with the index page, I used Django's Flatpages app to create it. For the Project app I created a model that allows me to upload an image and details about the project. In this app I also used imagekit to create different sized images and thumbnails. Next I made an Education app in which I made three models which are: Technology, My Education, and Goals. For the Technology model, I can include some basic details, a field to rate myself, and also upload a default image for that technology. In the My Education model, I used a foreign key to the Technology model and, along with some details, I included a field to upload an image for a certificate, if available. If a certificate is not available the Technology default image will be displayed. In the Accounts app, I created a CustomUser model and I also used SendGrid in the forms.py to allow for password reset for the site admin. Finally I created a Contact app to allow visitors to contact me. In this app I used SendGrid to send the message to my email.