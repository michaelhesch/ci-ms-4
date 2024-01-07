<a id="top"></a>

# Milestone Project Four - "Liffey"<!-- omit in toc -->

## Project Overview<!-- omit in toc -->

- The purpose of Liffey is to provide users with an e-commerce marketplace to buy and sell computer graphics hardware from brand stores as well as other users on the platform.  The site provides users with the ability to create accounts so that they can shop for computer graphics cards (GPUs), or utilize their own store page to list a GPU for sale to other users.  The platform collects a 5% fee from each sale for providing the marketplace for buyers and sellers to interact.  In addition, user's can leave reviews on products on the platform to provide feedback for the store owner and other users shopping for that item.

- This is a full-stack web application built with Material Design Bootstrap, Python, Django, Stripe, and AWS S3.  The project is deployed with and hosted on Heroku.

----

- [User Experience (UX)](#user-experience-ux)
  - [User stories](#user-stories)
  - [Design](#design)
  - [Wireframes](#wireframes)
- [Data Models](#data-models)
  - [Database Models](#database-models)
  - [Database Schema Diagram](#database-schema-diagram)
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
  - [Media](#media)
  - [Acknowledgments](#acknowledgments)

----

## User Experience (UX)

### User stories

#### First Time Visitor Goals<!-- omit in toc -->

- As a first time visitor

  - I want to understand what service the website provides.
  - I want to easily create a new account and log in.
  - I want to easily identify products from the store and view their details.
  - I want to be able to add multiple products to my shopping cart and eaisly checkout.
  - I want to be able to list and sell my own products on the store.

#### Returning Visitor Goals<!-- omit in toc -->

- As a returning visitor

  - I want to easily log in to my account and access my profile.
  - I want to view my past orders to review the details.
  - I want to view my sales total if I have listed any items in the store.
  - I want to request payment for my item sales if I have sold any items in the store.
  - I want to leave a review on a product I have purchased or used.

#### Site Owner Goals<!-- omit in toc -->

- As the site owner

  - I want to provide an easy to use registration and log in system.
  - I want to provide a streamlined store experience for users to find products.
  - I want to provide an easy checkout system for users to purchase products.
  - I want to allow users to view their saved details and past orders.
  - I want to provide users with the ability to easily add their products to the store.
  - I want to provide users with an easy way to manage their store including their products.
  - I want to provide users with the ability to request payment for the sales they have made on the platform.

### Design

#### Colour Scheme<!-- omit in toc -->

- The page color scheme is based on the Material Design Bootstrap colour theme.
- Button call to action color is MDB "Primary" (#1266F1), used for important buttons and icons.
- The full palette containing all colors used in the site can be found [here](https://mdbootstrap.com/docs/standard/content-styles/colors/#section-full-palette).

#### Typography<!-- omit in toc -->

- [Roboto](https://fonts.google.com/specimen/Roboto) : Roboto from Google Fonts was used as the font of choice throughout the project.  This font provides a clean and easy to read aesthetic across font weights.

### Wireframes

- Mobile Wireframes - [View](documentation/wireframes/mobile-wireframes.pdf)

- Tablet Wireframes - [View](documentation/wireframes/tablet-wireframes.pdf)

- Desktop Wireframes - [View](documentation/wireframes/desktop-wireframes.pdf)

#### Deviations from wireframe designs<!-- omit in toc -->

- Notable deviations from the wireframe design:
  - Ability to sort the store page and vendor store pages by price, etc. was not implemented in this release due to time constraints.
  - Removed filtering and search navigation bar from the vendor store page view.  Due to time constraints, this functionality was not added to the individual vendor page for this release and would be a planned feature to add in a future release.
  - Removed pagination from vendor store page view, similar to the navigation and filtering bar, this would be a planned feature for a future release.

## Data Models

### Database Models

#### Checkout App Models<!-- omit in toc -->

- `Order` Model
  - Contains the details to create and display an order in the store.
  - Fields include: order number, user, user profile, created date, ordered date, ordered (boolean), shipping details, shipping cost, order grand total, and stripe pid.
  - Foreign Keys to User (user), UserProfile (user_profile) and ShippingDetails (shipping_details) models.

- `OrderItem` Model
  - Contains the details to create and display an order line item (individual item within an order).
  - Fields include: related order, buyer, vendor, item, quantity, item subtotal (item_total), ordered (boolean), vendor revenue amount, store revenue amount, and vendor paid (boolean).
  - Foreign Keys to Order (related_order), User (buyer), VendorProfile (vendor) and Product (item).

- `ShippingDetails` Model
  - Contains the details to create and display the shipping details for an order.
  - Fields include: user, order number, full name, email, phone number, address line one, address line two, state, city, zipcode and country.
  - Forein Key to User (user).
  - OneToOne to Order (order_num).

#### Product App Models<!-- omit in toc -->

- `Category` Model
  - Contains the details to create and hold product category details for items listed in the store.  In this application, this is the manufacturer of a graphics card, which will be either Nvidia or AMD.  
  - Fields include: category name, slug, and category order.

- `ProductName` Model
  - Contains the model names of various graphics cards that can be listed in the store, in order to give structure to the listings on the site.
  - Fields include: product name and category.
  - Foreign key to Category (category).

- `Product` Model
  - Contains the key details of items listed for sale on the platform.
  - Fields include: category, sku, seller, product name, slug, description, brand, boost clock, memory clock, memory type, interface type, price, image, thumbnail and date added.
  - Foreign keys to Category (category), UserProfile (seller) and ProductName (product_name).

- `Review` Model
  - Contains the details to create and display a product review on a product listed on the platform.
  - Fields include: title, content, added by, rating, product reviewed and date added.
  - Foreign keys to User (added_by) and Product (product_reviewed).
  
#### Profiles App Models<!-- omit in toc -->

- `Profile` Model
  - Contains the details to create and display a user's default shipping details, email and phone number on their profile.
  - Fields include: user (User), email address, phone number, address line one, address line two, city, state, zipcode, country and created date.
  - OneToOne to User (user).

- `UserProfile` Model
  - Extends the Profile class to add ability for a user to add an avatar photo and the ability for the store owner to grant accounts the 'verified' status.  
  - Original intention was to create a two tier user system where users were given basic UserProfile access when signing up, and could upgrade to Vendor status later.  This was not implemented due to time constraints.
  - If given more time for this release, this would have been refactored with VendorProfile to simplify this model.
  - Fields include: avatar, avatar url, verified (boolean), and created date.

- `VendorProfile` Model
  - Extends the UserProfile class to add ability for users to have and edit a store name on their profile.
  - Original intention was to create a two tier user system where users were given basic UserProfile access when signing up, and could upgrade to Vendor status later.  This was not implemented due to time constraints.
  - If given more time for this release, this would have been refactored with UserProfile to simplify this model.
  - Fields include: store name and store slug.

### Database Schema Diagram

![database schema diagram](/documentation/liffey-db-diagram.png)

## Features

### All Pages<!-- omit in toc -->

- Navigation: Clear, concise and easy to use navigation system visible across all pages, including when logged out.
  - Logged Out navigation choices: Home, Register or Log In
  - Logged In navigation choices: Store, Sell Product, Cart, Profile, Log Out.
- Logged in users will have the ability to add a product to the store with the "Sell Product" button on the navbar.  This will open a new product form where the user can add the details of their item, as well as upload an image of their product.
- Footer: Easy to identify social media links as well as a basic business style copyright for Liffey in the footer.

### Landing Page (Logged Out)<!-- omit in toc -->

- Clearly displayed summary of the purpose of the site.
- Two large buttons directing users to either register or log in to their account, in addition to the navigation bar buttons.

### Login Page<!-- omit in toc -->

- Simple login page directing the user to enter their username or email address and password.
- Ability for users to reset their password if needed.
- Link to the registration page if a user needs to create an account and arrives at the login page by mistake.
- Redirection to the home page with a banner message indicating the user has logged in successfully.

### Registration Page<!-- omit in toc -->

- Simple and brief registration form for users to create a new account, requiring only a valid email address, username and password.
- Link to the log in page if a user already has an account and arrives at the registration page by mistake.

### Main Store<!-- omit in toc -->

- Logged in users will be presented with a feed of all items listed in the store, with an additional navigation bar for filtering and searching the products in the store.
- Ability to select a product and open the product's detailed view, where a user can adjust the desired quantity of the item and add the item(s) to their cart.
- Product cards will display the "new" tag for the first 30 days they are active on the platform, after that point this tag will disappear.
- Product detail page also contains hepful detailed specification information about the product, and the description added by the owner/uploader of the product.
- Product detail page also contains a section to display product reviews from other users, and the ability for a user to add their own review.
- Product detail page also contains a section to display similar products which the user may be interested in.  Up to four similar products will be displayed at one time.

### Vendor Store<!-- omit in toc -->

- Similar functionality to the main store page, however only products added by the current user will be displayed.
- Store management panel at the top of the store will display the user's current sales balance and paid sales balance, if they have sold any products on the platform.
- Store management panel also contains buttons to change the user's store name and request a payment for their current sales balance (if applicable).
- Ability to "modify" and "remove" user's own products via buttons displayed in the store view only.
- Modify product button which opens a new product form with the current product details pre-populated for the user to edit.
- Remove button will remove the product completely after a confirmation window is opened and confirmed.
- Ability to view other user's stores, which will only display their products for sale, and not the user-specific controls and sales details.

### User Profile<!-- omit in toc -->

- Provides a summary of the user's store details, default shipping details, and purchase history.
- Provides the ability for a user to open an order they have placed by clicking the order number, and review the order confirmation details for past orders.
- Provides the ability to navigate to the user's vendor store, where they can manage their store name, products and payments.

### Shopping Cart<!-- omit in toc -->

- Summary of the items that a user has in their cart at any given time and the associated order subtotal and total.
- Provides ability for user to increase the quantity of individual items in their cart.
- Provides ability for user to decrease the quantity of individual items in their cart (if greater than one).
- Provides ability for user to remove an entire line item, regardless of quantity, from their cart.
- Provides the ability to go directly to a specific product's page by clicking the product name.
- Provides the ability to go to an item's seller's store directly by clicking their store name.
- Provides the ability to easily continue shopping or go directly to the checkout.

### Checkout<!-- omit in toc -->

- Provides a brief summary of the items and their quantity in a user's order, along with the item subtotals and order total.
- Provides a clear and concise checkout form for a user to add their contact and shipping details.
- Provides an easy to use credit card payment system via Stripe integration.
- Provides the ability to easily go back to the cart if a user needs to modify their order.
- Provides the ability to save shipping details to the user's profile.
- Provides an order confirmation summary with the key details of the items in the order and the total, as well as the order number.
  
### Future Improvements<!-- omit in toc -->

- Due to time constraints in producing an MVP release of this project, several desired features had to be removed or omitted from the deployed project.  In future releases, I would like to enhance the functionality and user experience with the following items (to start):
  - Filter, Search and Sort on Vendor Store pages.
  - Pagination on Vendor Store pages.
  - Sorting on main store page.
  - User friendly error message pages (404, 500).
  - Enhance content on logged out landing page to entice new users to join.
  - Expanded profile page functionality - edit defaults, user avatar photo.
  - Expanded vendor profile page functionality - more choice/structure around vendor payments from the store.

## Technologies Used

### Programming Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python 3.9.6](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries & Programs Used

1. [Django](https://www.djangoproject.com/)
    - The Django framework (v3.2.9) was used as the full stack framework for this project.  Django is a python framework which provides a vast range of heplful features used in this project.
2. [Google Fonts:](https://fonts.google.com/)
    - Google fonts are included with MBD, and this project uses the Roboto font family throughout the site.
3. [Favicon.io](https://favicon.io)
    - Favicon.io was used to generate the custom "L" Favicon used for the browser tab for the site.
4. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome icons are included with MDB, and this project uses the provided icons to provide simple, user-friendly ways to interact with different aspects of the site's functionality.
5. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the design wireframes used to outline the webpage before development.
6. [drawSQL](https://drawsql.app/)
    - This tool was used to create the database schema visualization found in the Database Model & Schema section above.
7. [Stripe](https://stripe.com/en-ie/)
    - Stripe provides an easy to use card payment integration utilized in the checkout process of this project.
8. [Amazon AWS S3](https://aws.amazon.com/s3/?nc2=h_ql_prod_st_s3)
    - Amazon simple storage system service provides hosting for the project's static and media files.
9. [Visual Stuido Code:](https://code.visualstudio.com/)
    - Visual Stuido code was used as the desktop development IDE for the project, managing the code and assets for the page during development.
10. [Git:](https://git-scm.com/)
    - Git was used for version control by utilizing the Windows command prompt/terminal interface to commit and push to GitHub.
11. [GitHub:](https://github.com/)
    - GitHub is used to store the project's code after being pushed from the local development machine using Git.
12. [Heroku](https://www.heroku.com/)
    - Heroku was used to deploy the site and provides cloud hosting for the live version of the site and the production Postgres database.
13. [Code Institute Full-Stack Developer Course](https://www.codeinstitute.net/)
    - Code snippets were referenced for styling various elements of the site, and organization of the social media links footer section.

## Testing

### Detailed testing information can be found in the testing file, [located here.](documentation/TESTING.md)<!-- omit in toc -->

## Deployment

### Deployment Requirements

- The following accounts and software packages are required to deploy a clone of this project.  All can be obtained free of charge from the respective providers.
- This deployment assumes the user is working in a Windows environment - please consult the doucmentation specific to your operating system if needed.

1. Git / GitHub Account
2. Python 3
3. Heroku Account
4. Stripe Account
5. Visual Studio Code / Other IDE

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/michaelhesch/ci-ms-4/)
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

1. Setup/install all dependencies:
   1. Change directory to the location of the local clone.
   2. Create a new Python virtual environment to ensure no conflicts occur with locally installed Python packages.  This is done with the command "python3 -m venv venv" (if needed install the Python virtual environment package with "pip install virtualenv")
   3. Launch your virtual environment with ".\venv\Scripts\activate" (on Windows, syntax will differ for other operating systems)
   4. Install all necessary dependencies for this project as specified in the requirements.txt file with the command "pip install -r requirements.txt"
   5. Create your SQL database by running intial migrations with the command "python manage.py migrate"
   6. Create a superuser account by running "python manage.py createsuperuser".  This will allow you to access the admin panel to fully manage the project.

2. Configure local environment variables
   1. Set up your .env file and ensure that it is included in .gitignore - this is critically important to avoid exposing sensitive configuration data!
   2. Configure your .env file as follows:
      1. Note: A secret key will be included in your Django settings file by default, it is recommended to generate a new key with a tool such as [Django Secret Key Generator.](https://miniwebtool.com/django-secret-key-generator/)
      2. Development must only be set to True in a local build, when deployed ensure this variable is set to False!
      3. Stripe keys are provided in your Stripe developer account once registered.
      4. Email configuration is required if you plan to utilize emails sent by Django.

        ```python
            SECRET_KEY=[your_secret_key]
            DEVELOPMENT=True
            STRIPE_PUBLIC_KEY=[your_public_key]
            STRIPE_SECRET_KEY=[your_secret_key]
            STRIPE_WH_SECRET=[your_webhook_key]
            EMAIL_USER=[your_account]
            EMAIL_PASS=[your_password]
        ```

    3. Start the application locally by running "python manage.py runserver".
  
### Heroku Deployment

Heroku deployment is fast and efficient once the project is properly configured.  Heroku needs the requirements.txt and Procfile files included in the repository for this project to deploy the application to a live environment.

If the Procfile was not cloned, this can easily be created from the terminal on Windows using "echo web: gunicorn run:app >Procfile".  Be sure to do this in the project's root directory.

The project was deployed to Heroku using the following steps, which can be followed for a local clone:

1. Log in to your Heroku account, then create a new app with a unique name.
2. Once your app is created, go to the "Resources" tab, and under "Add-ons" search for "Heroku Postgres", select Postgres and press "Submit Order" to provision a new database.
3. For the deployment method, navigate to the "Deploy" tab, select GitHub, then select "Connect to GitHub".
4. After you have connected to the repository for the cloned app, you need to configure the Heroku environment variables.
5. Open the "Settings" menu and click the "Reveal Config Vars" button to view the environment variables.
6. Add all necessary variable name and value pairs exactly as used in the local environment variables file.
7. Return to the "Deploy" tab and click "Deploy Branch" (unless you opted to enable automatic deployments)
8. On your local machine, add the "DATABASE_URL" variable from your Heroku config vars to the .env file.  This will allow you to migrate the new database on your Heroku app.
   1. If you wish, you can dump your local database data and load it to your Heroku app.  This must be done before adding the DATABASE_URL to your .env file.
   2. This can be done with the command "python manage.py dumpdata > db.json"
9. Once the DATABASE_URL is included in your environment, run "python manage.py makemigrations" and then "python manage.py migrate" to migrate your Heroku database.
   1.  If you want to load your local database dump, you can now run "python manage.py loaddata db.json".
10. Once migrated, comment out or remove the DATABASE_URL from your local .env file to return to using the SQLite local database.
11. After the deployment and migrations are completed, you can view your live application by clicking "View App", or navigating to the name of your app with .herokuapp.com added.

## Credits

### Code

- [Code Institute Full-Stack Developer Course](https://www.codeinstitute.net/) : Code snippets were referenced for various components of the project, as well as the guide for configuring AWS, the Gmail smtp server and Heroku deployment.

- [Django Documentation](https://docs.djangoproject.com/en/4.0/) : Django official documentation was referenced extensively, particualry around class based views, signals, querying and filtering, and many other aspects of Django.

- [Stripe Payments Documentation](https://stripe.com/docs/payments/online-payments) : Stripe official documentation referenced around implementation of stripe payments widget and utilization of webhooks.

- [Django Multi-Vendor e-Commerce Website by Code With Stein](https://www.youtube.com/playlist?list=PLpyspNLjzwBkeyP_4_bZBdtRjZQreDR_H) : Tutorial was referenced for multiple components of the project, particularly around the setup of vendor stores and handling of user uploaded images.

- [Python Django Tutorial by Corey Schafer](https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p) : Tutorial series was referenced for further background and examples on use of Django to create a web application after completing the CI Boutique Ado project.

- [MDB Bootstrap 4 E-Commerce Template](https://mdbootstrap.com/freebies/jquery/e-commerce/) : MDB Bootstrap 4 e-Commerce template was utilized for multiple components across the site and the general layout.  Code from this template was adpated and integrated into the project.

- [How to Highlight Active Links in your Django Website](https://valerymelou.com/blog/2020-05-04-how-to-highlight-active-links-in-your-django-website) : Code referenced to create dynamic highlighting behind active navigation links in the base template.

- [Format numbers in Django templates](https://stackoverflow.com/questions/346467/format-numbers-in-django-templates) : Stackoverflow solution utilized to comma format numbers in the UI - such as product prices, order subtotals & totals, etc.

- [Django file upload and rename](https://coderedirect.com/questions/227021/django-file-upload-and-rename) : Solution used as the foundation for the solution implemented in this project to update file names for user uploaded photo files captured when adding a new product to the platform.

- [How to remove arrows from input type](https://stackoverflow.com/questions/13107118/how-to-remove-the-arrows-from-inputtype-number-in-opera) : CSS solution to remove spinner arrows from number input field which were visible in the product details page.

- [README Template](https://github.com/Code-Institute-Solutions/SampleREADME) : Template for the README.md file for this project was sourced from Code Institute.

### Media

- Product images featured on the site uploaded by the developer were sourced using [GPUTracker.eu](https://www.gputracker.eu/en/category/1/graphics-cards) and are utilized in this project for demonstration purposes only.

- Product descriptions featured on the site, uploaded by the developer, were sourced using [GPUTracker.eu](https://www.gputracker.eu/en/category/1/graphics-cards) and are utilized in this project for demonstration purposes only.

- Additional images, descriptions and review content may be provided by users from their own image libraries, no copyright or ownership is implied by displaying these images.

### Acknowledgments

- My Code Institute Mentor Aaron for helpful feedback on my ideas prior to development and guidance throughout the project.

[Return to the Top](#top)
