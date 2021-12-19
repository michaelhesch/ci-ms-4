<a id="top"></a>

# Testing<!-- omit in toc -->

[Return to Readme](/README.md)

----

- [Code Validation](#code-validation)
  - [Functional Testing](#functional-testing)
- [Testing User Stories from User Experience (UX) Section](#testing-user-stories-from-user-experience-ux-section)
  - [First Time Visitor Story Testing](#first-time-visitor-story-testing)
  - [Returning Visitor Story Testing](#returning-visitor-story-testing)
  - [Site Owner Story Testing](#site-owner-story-testing)
- [Responsiveness](#responsiveness)
- [Lighthouse](#lighthouse)
- [Noteworthy Issues & Bugs Encountered in Development](#noteworthy-issues--bugs-encountered-in-development)

----

### Code Validation

The W3C Markup Validator, W3C CSS Validator, JSHint, PEP8 Online and PyCharm were used to validate every page of the project to ensure there were no outstanding syntax errors in the deployed project.  In addition, the Python and Django add-ins for VSCode were utilized for linting throughout development to help minimize errors.

- [W3C Markup Validator](https://validator.w3.org/nu/)
  - All pages were validated via direct input by inserting the base template into the W3 validator, then adding each page's content one at a time and validating.  Errors were returned due to Django template tags being used extensively in the HTML, but no HTML errors were detected.
  - Pages that are usable without being logged in were validated via URL as well, and no errors were returned.

- [W3C CSS Validator - Jigsaw](https://jigsaw.w3.org/css-validator/)
  - No errors returned when validating style.css content directly.  Warnings returned for vendor extensions used to disable spinner on number input.
  - Multiple warnings are returned if validation is run on the deployed app due to dependencies such as Bootstrap.

- [JSHint](https://jshint.com/)
  - This project uses limited custom JavaScript, but does rely on external JS from Stripe, and Material Design Bootstrap for animations, for example.  The internal JavaScript passed the JSHint linter with no errors.

- [PEP8 Online](http://pep8online.com/) - PEP8 Online is a web-based PEP8 code format compliance checker which was used to check each Python file in this app for PEP8 compliance.

- [PyCharm](https://www.jetbrains.com/pycharm/) - Pycharm Python IDE was used as an additional double-check on all Python code for PEP8 compliance after checking each file with PEP8 Online.
  
#### Functional Testing

- Below are descriptions of tests undertaken on the deployed project to ensure expected behaviors of functionality.

- Registration
  - Pass - Email, Email (again), Username, Password, Password (again) all required fields.
  - Pass - Cannot sign up unless email is in the correct format.
  - Pass - Cannot sign up with email that is already registered.
  - Pass - Passwords must contain at least 8 characters.
  - Pass - Email fields must match.
  - Pass - Password fields must match.
  
- Log In
  - Pass - Cannot access content unless logged in.
  - Pass - Login, password all required fields.
  - Pass - Logging in with correct username/password enables access to content.
  
- Log Out
  - Pass: Logging out disables access to content.

- Store
  - Pass: Can view all items listed in store with 'All' filter button selected.
  - Pass: Can view all 'AMD' items listed in store with 'AMD' filter button selected.
  - Pass: Can view all 'NVIDIA' items listed in store with 'NVIDIA' filter button selected.
  - Pass: Can search across 'title' and see matching results in store.
  - Pass: Pagination working to view next set of items in store.
  - Pass: Can see GPU manufacturer pill on details page.
  - Pass: Can see all product details on details page.
  - Pass: Can see Seller store link on details page for user who listed product.
  - Pass: Can click on Seller store link on details page, which redirects to store to see all items listed by that seller.
  - Pass: Can view 4 similar products thumbnails on details page.
  - Pass: Can click on a similar product link on details page, which redirects to that product's detail page.
  - Pass: Can view product reviews on each details page.
  - Pass: Can leave a product review on detail page.
  - Pass: Can edit a review left by my username on details page.
  - Pass: Can delete a review left by my username on details page.
  - Pass: Delete review confirmation popup appears before deleting review.
  - Pass: Can dismiss delete review popup by clicking 'close' button, will keep review on product detail.
  - Pass: Cannot decrease item quantity less than 1 on details shopping cart when clicking - button.
  - Pass: Can increase item quantity by clicking + on details shopping cart.
  - Pass: Clicking 'Add to cart' adds item with correct number to cart.

- Cart
  - Pass: Can see all products & quantities in cart.
  - Pass: Can increment quantity in cart on cart page.
  - Pass: Can decrement quantity in cart on cart page.
  - Pass: Can remove item in cart completely.
  - Pass: Cannot check out if nothing is in cart.
  - Pass: Can click 'continue shopping' from cart page to continue browsing products.
  - Pass: Can click 'checkout' from cart page to check out.
  
- Checkout
  - Pass: Cannot checkout unless all required fields are filled in.
  - Pass: Cannot checkout unless email is in the correct format.
  - Pass: Stripe integration working with '424242...'
  - Pass: Upon successful purchase, successful confirmation page appears with order details.

- Sell a Product
  - Pass: Cannot list product unless all required fields are filled in.
  - Pass: Category/Brand/Product Name fields selectable in dropdown.
  - Pass: Price is a numeric field.
  - Pass: Once able to list product, navigates to product detail page to view details.
  - Pass: Can see product owner details content for product because I have listed it.

- Profile
  - Pass: Displays profile with store balance, paid balance and default shipping information.
  - Pass: Clicking 'view store' navigates to store page.
  - Pass: Clicking 'change store name' opens popup that allows for changing of store name.
  - Pass: Can successfully change store name on clicking 'save changes' button.
  - Pass: Can bypass changing store name by clicking 'close' button.
  - Pass: Clicking 'request payment' opens popup that allows for confirmation of payment.
  - Pass: Clicking 'request payment' in popup closes popup and updates sales balance on store page.
  - Pass: Clicking 'close' in popup closes popup and does not update sales balance on store page.
  - Pass: Can only view sales balance on store page if you own the store page.
  - Pass: Can view all items listed in store with 'All' filter button selected.
  - Pass: Can view all 'AMD' items listed in store with 'AMD' filter button selected.
  - Pass: Can view all 'NVIDIA' items listed in store with 'NVIDIA' filter button selected.
  - Pass: Can search across 'title' and see matching results in store.
  - Pass: Can successfully modify product detail by clicking modify button.
  - Pass: Can navigate to product detail page by clicking product from list.
  - Pass: Can successfully delete product by clicking delete button.
  - Pass: Delete product confirmation popup appears before deleting product.
  - Pass: Can bypass delete product popup by clicking 'close' button, will keep product on store.
  - Pass: No products or sales balance is listed if you do not have any products listed.

### Testing User Stories from User Experience (UX) Section

#### First Time Visitor Story Testing

> I want to understand what service the website provides.
- The landing page provides a brief but concise description of the purpose of the site and what service is offered by the platform.
  
> I want to easily create a new account and log in.
- The sign up page allows a user to create a new account quickly with very little required information, and allows them to sign in as soon as their email address is confirmed.

> I want to easily identify products from the store and view their details.
- The store view is easily reached from any page on the site once logged in.
- The store view allows easy filtering and searching of the products on the site.
- Product details can be viewed by clicking on a product in the store, or by clicking the product name of a product in a past order, or in the user's cart.

> I want to be able to add multiple products to my shopping cart and eaisly checkout.
- Users can select the quantity of an item they want to add to their cart easily from the produc details page.
- Users can easily view related products from a given product's details page if they are interested.

> I want to be able to list and sell my own products on the store.
- The Sell a Product feature is accessible from the main navigation bar anywhere on the site.
- This simple form allows a user to select the GPU they wish to sell and add their description, photo and details.
- The product is then immediately listed for sale in the store, and can be managed from the user's store. 

#### Returning Visitor Story Testing

> I want to easily log in to my account and access my profile.
- Logging in to the site is done directly from the navigation bar link or button on the landing page if the user is logged out.
- Logging in can be done with either the user's username or email address.
- Once logged in, the profile is easily accessible from anywhere on the site via the main navigation bar.
  
> I want to view my past orders to review the details.
- Order history is available in the user's profile page.
- Orders in the order history can be opened by clicking the order number, which then displays the order's details.

> I want to view my sales total if I have listed any items in the store.
- A user's total sales (paid and unpaid) are displayed in their profile page and in their store page in the summary section.

> I want to request payment for my item sales if I have sold any items in the store.
- A user can request payment for any unpaid sales through their store page, in the summary panel.

> I want to leave a review on a product I have purchased or used.
- A product review can be left by pressing the "leave a review" button on any product's details page.

#### Site Owner Story Testing

> I want to provide an easy to use registration and log in system.
- Users can easily register with a short registration form, and log in with either their username or email address.
  
> I want to provide a streamlined store experience for users to find products.
- Products can be viewed easily at a glance in the main store page, filtered by GPU type and searched for in the store.
- Products are easy to add to the cart once a user views the product details page.

> I want to provide an easy checkout system for users to purchase products.
- Checkout can be completed by filling out one form once an item has been added to the cart.
- Stripe provides card payment integration into the site allowing users to pay without any hassle.

> I want to allow users to view their saved details and past orders.
- Users are given the option to save their shipping details to their profile when checking out.
- These saved details are visible in the user's profile summary page.

> I want to provide users with the ability to easily add their products to the store.
- Users are able to use the Sell Product form accessible anywhere on the site via the main navigation bar to list products for sale.
- Adding products requires only filling out one form and providing a product image (a default will be applied if no image is provided).

> I want to provide users with an easy way to manage their store including their products.
- Users have the ability to view their own store page and manage their store from this view.
- The store management view allows users to modify or remove products, rename their store, and request payment for their sales.

> I want to provide users with the ability to request payment for the sales they have made on the platform.
- Users can quickly and easily request payment for their unpaid sales balance from their store management view.

### Responsiveness

- All pages were tested for responsiveness and any visible bugs using Google Chrome developer tools to emulate the viewing size across all standard device sizes offered.  Media queries have been implemented in the CSS of the site to adjust various attributes as necessary to improve the viewing experience on small screen sizes.  In addition site rendering on very high resolutions (such as "4K" or 2160p) were checked to ensure consistent performance as expected.
  
  Device Screen Sizes Tested:

  ![Device Sizes Tested](screenshots/device-list.png)

- In addition, all pages on the site were tested for correct behavior on a 27" desktop monitor, a 15.1" laptop monitor, an iPhone 11 and a 10.5" iPad Pro.  The pages scale and respond as expected for a normal user experience across these viewing sizes & devices.  Improvements could be made in the future around the item quantity selector and add to cart button on the product detail page to improve styling on very small devices.

### Lighthouse

- The Lighthouse tool within Chrome Developer tools was used to generate performance scores and identify areas for improvement in both mobile and desktop views of the page.  Lighthouse scoring was performed on the main Store page, as this is the most resource intensive page in the app.  Results of this scoring can be viewed via the links below:
  
  1. [Mobile Score & Summary](lighthouse/store-mobile.pdf)

    ![Mobile Lighthouse Results](screenshots/store-mobile.png)
  
  2. [Desktop Score & Summary](lighthouse/store-desktop.pdf)

    ![Desktop Lighthouse Results](screenshots/store-desktop.png)

- Please note that while efforts to correct some defects indicated in these results are due to issues found in external dependencies, such as security vulnerabilities in the JQuery version utilized by this MDB implementation, or MDBootstrap's CSS for example, or other faults that are beyond the scope of this project to remedy.

### Noteworthy Issues & Bugs Encountered in Development

- [Open] Image handling when editing existing product

- If the user clicks the 'clear item' checkbox next to the current image when editing a product, and does not add a new image, an error warning is returned when the form is submitted.  Further investigation into how to restore the item to the default image if no image is selected upon editing is needed.

[Return to the Top](#top)