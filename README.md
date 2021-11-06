<a id="top"></a>

# Milestone Project Four - "TBD"<!-- omit in toc -->

![Am I Responsive Image - Placeholder](#)

## Project Overview<!-- omit in toc -->

- The purpose of X is to provide users with Y.

- This is a full-stack web application built with X.

[View the live project here.](#)

----

- [User Experience (UX)](#user-experience-ux)
  - [User stories](#user-stories)
  - [Design](#design)
  - [Wireframes](#wireframes)
- [Data Models](#data-models)
  - [Database Models](#database-models)
  - [Database Schema Diagram](#database-schema-diagram)
  - [Postresql Database Setup](#postresql-database-setup)
- [Features](#features)
- [Technologies Used](#technologies-used)
  - [Programming Languages Used](#programming-languages-used)
  - [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)
- [Testing](#testing)
- [Deployment](#deployment)
  - [Deployment Requirements](#deployment-requirements)
  - [Making a Local Clone](#making-a-local-clone)
  - [Working With A Local Clone](#working-with-a-local-clone)
  - [Heroku Deployment](#heroku-deployment)
- [Credits](#credits)
  - [Code](#code)
  - [Content](#content)
  - [Media](#media)
  - [Acknowledgments](#acknowledgments)

----

## User Experience (UX)

### User stories

#### First Time Visitor Goals<!-- omit in toc -->

- As a first time visitor

  - I want to x

#### Returning Visitor Goals<!-- omit in toc -->

- As a returning visitor

  - I want to x

#### Site Owner Goals<!-- omit in toc -->

- As the site owner

  - I want to x

### Design

#### Colour Scheme<!-- omit in toc -->

- x

#### Typography<!-- omit in toc -->

- x

### Wireframes

- Mobile Wireframes - [View](#)

- Tablet Wireframes - [View](#)

- Desktop Wireframes - [View](#)

#### Deviations from wireframe designs<!-- omit in toc -->

- x

## Data Models

### Database Models

- x

### Database Schema Diagram

![database schema diagram](X)

### Postresql Database Setup

- x

## Features

### All Pages<!-- omit in toc -->

- x

### Landing Page (Logged Out)<!-- omit in toc -->

- x

### Login Page<!-- omit in toc -->

- x.

### Registration Page<!-- omit in toc -->

- x

### User Friendly Error Handling<!-- omit in toc -->

- Provide user-friendly pages to mask 403, 404 and 500 responses to improve user experience and confidence in the app.

### Future Improvements<!-- omit in toc -->

- x

## Technologies Used

### Programming Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python 3.9.6](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries & Programs Used

1. [Django](https://X/)
    - x
2. [Google Fonts:](https://fonts.google.com/)
    - Google fonts are included with MBD, and this project uses the Roboto font family throughout the site.
3. [Favicon.io](https://favicon.io)
    - Favicon.io was used to generate the Favicons used for the browser tab as well as the navbar logo for the site.
4. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome icons are included with MDB, and this project uses the provided icons to provide simple, user-friendly ways to interact with different aspects of the site's functionality.
5. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the design wireframes used to outline the webpage before development.
6. [dbdiagram.io](https://dbdiagram.io/home)
    - This tool was used to create the database schema visualization found in the Database Model & Schema section above.
7. [Visual Stuido Code:](https://code.visualstudio.com/)
    - Visual Stuido code was used as the desktop development IDE for the project, managing the code and assets for the page during development.
8. [Git:](https://git-scm.com/)
    - Git was used for version control by utilizing the Windows command prompt/terminal interface to commit and push to GitHub.
9. [GitHub:](https://github.com/)
    - GitHub is used to store the project's code after being pushed from the local development machine using Git.
10. [Heroku](https://www.heroku.com/)
    - Heroku was used to deploy the site and provides cloud hosting for the live version of the site.
11. [Code Institute Full-Stack Developer Course](https://www.codeinstitute.net/)
    - Code snippets were referenced for styling various elements of the site, and organization of the social media links footer section.

## Testing

### Detailed testing information can be found in the testing file, [located here.](documentation/TESTING.md)<!-- omit in toc -->

## Deployment

### Deployment Requirements

- The following accounts and software packages are required to deploy a clone of this project.  All can be obtained free of charge from the respective providers.

1. GitHub Account
2. X
3. Heroku Account
4. Python 3.9.6

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/michaelhesch/ci-ms-3/)
2. Under the repository name, click "Code", then select the clipboard icon under "Clone with HTTPS" to copy the link.
3. Open Git Bash
4. Change the current working directory to the location where you want the cloned directory.
5. Type `git clone`, and then paste the URL you copied in Step 2 in place of the URL in quotes below.

    ```git

    # git clone "https://github.com/YOUR-USERNAME/YOUR-REPOSITORY"
    
    ```

6. Press Enter. Your local clone will be created.

    ```git
    
    # git clone "https://github.com/YOUR-USERNAME/YOUR-REPOSITORY"
    > Cloning into `Test-Clone`...
    > remote: Counting objects: 10, done.
    > remote: Compressing objects: 100% (8/8), done.
    > remove: Total 10 (delta 1), reused 10 (delta 1)
    > Unpacking objects: 100% (10/10), done.
    
    ```

[Click Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to visit GitHub Help for more detailed explanations of the cloning process.

### Working With A Local Clone

1. Setup all dependencies:
   1. Change directory to the location of the local clone.
   2. Create a new Python virtual environment to ensure no conflicts occur with locally installed Python packages.  This is done with the command "python3 -m venv venv" (if needed install the Python virtual environment package with "pip install virtualenv")
   3. Launch your virtual environment with ".\venv\Scripts\activate" (on Windows, syntax will differ for other operating systems)
   4. Install all necessary dependencies for this project as specified in the requirements.txt file with the command "pip install -r requirements.txt"

2. Ensure you have a MongoDB database set up (see MongoDB Database Setup section above).
   1. Create the following collections: comment, user, and photo.

3. Configure local environment variables *TBU*
   1. Set up your .flaskenv file and ensure that it is included in .gitignore - this is critically important to avoid exposing sensitive configuration data!
   2. Configure your .flaskenv file as follows:

        ```python
            SECRET_KEY=[your_secret_key]
            X
        ```

### Heroku Deployment

Heroku deployment is fast and efficient once the project is properly configured.  Heroku needs the requirements.txt and Procfile files included in the repository for this project to deploy the application to a live environment.

If the Procfile was not cloned, this can easily be created from the terminal on Windows using "echo web: gunicorn run:app >Procfile".  Be sure to do this in the project's root directory.

The project was deployed to Heroku using the following steps, which can be followed for a local clone:

1. Log in to your Heroku account, then create a new app with a unique name.
2. For the deployment method, select GitHub, then select "Connect to GitHub".
3. After you have connected to the repository for the cloned app, you need to configure the Heroku environment variables.
4. Open the "Settings" menu and click the "Reveal Config Vars" button to view the environment variables.
5. Add all necessary variable and value pairs exactly as used in the local environment variables file.
6. Return to the "Deploy" tab and click "Deploy Branch" (unless you opted to enable automatic deployments)
7. After the deployment process has completed, you can view your live application by clicking "View App", or navigating to the name of your app with .herokuapp.com added.

## Credits

### Code

- [Code Institute Full-Stack Developer Course](https://www.codeinstitute.net/) : Code snippets were referenced from the Task Manager mini-project, as well as the guide for configuring the MongoDB database and Heroku deployment.

- [README Template](https://github.com/Code-Institute-Solutions/SampleREADME) : Template for the README.md file for this project was sourced from Code Institute.

- Additional credits for code snippets or solutions can be found inline in the project code where applicable.

### Content

- All static text content (such as landing page text and page descriptions) was written by the developer.  In addition, demonstration user accounts were created to populate image and comment data to the site for demo purposes, written by the developer.

- All other user content, such as photos, photo descriptions, user profile details, and photo comments added are created by the respective user who added them.

### Media

- X

- Additional images may be provided by users from their own image libraries, no copyright or ownership is implied by displaying these images.

### Acknowledgments

- My Code Institute Mentor Aaron for helpful feedback on my ideas prior to development and guidance throughout the project.

[Return to the Top](#top)
