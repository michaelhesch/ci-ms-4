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

The W3C Markup Validator, W3C CSS Validator, PEP8 Online and PyCharm were used to validate every page of the project to ensure there were no outstanding syntax errors in the project.  Results of those checks are documented in PDFs included in the project repository and can be accessed by following the links below.

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
  - PASSING: E-Mail Address Validation - Form correctly requires a valid email address to be entered in the email field.
  - PASSING: Password Match Validation - Form correctly requires passwords entered by the user to match.
  - PASSING: Empty Form Submission Validation - Form does not proceed with posting if required fields are blank.  Tested fields username, first name, last name, and password fields.  Avatar color is pre-selected by default and cannot be de-selected before submitting.
  - PASSING: Duplicate Email Cannot Register - Form correctly prevents a user from registering a new account using an email address that is already currently in the database.
  - PASSING: Default Avatar Selected - By default the form is populated with an avatar colour selected, which can be changed by the user but cannot be de-selected entirely, which is the intended behavior.
  - PASSING: Username Regex Validation - Usernames cannot contain spaces or special characters, only upper or lower case letters and numbers.  Confirmed multiple combinations of special characters and spaces in username field are returned as invalid by the form.

### Testing User Stories from User Experience (UX) Section

#### First Time Visitor Story Testing

> x.
- x.
  
> x.
- x.

> x.
- x.

> xe.
- xe.

#### Returning Visitor Story Testing

> x.
- x.
  
> x.
- x.

> x.
- x.

> xe.
- xe.

#### Site Owner Story Testing

> x.
- x.
  
> x.
- x.

> x.
- x.

> xe.
- xe.

### Responsiveness

- All pages were tested for responsiveness and any visible bugs using Google Chrome developer tools to emulate the viewing size across all standard device sizes offered.  Media queries have been implemented in the CSS of the site to adjust various attributes as necessary to improve the viewing experience on small screen sizes, such as scaling social media icon sizes and adjusting button styling to remain easily usable.  In addition site rendering on very high resolutions (such as "4K" or 2160p) were checked to ensure consistent performance as expected.
  
  Device Screen Sizes Tested:

  ![Device Sizes Tested](screenshots/device-list.png)

- In addition, all pages on the site were tested for correct behavior on a 27" desktop monitor, a 15.1" laptop monitor, an iPhone 11 and a 10.5" iPad Pro.  The pages scale and respond as expected for a normal user experience across these viewing sizes & devices.  Improvements could be made in the future around the item quantity selector and add to cart button on the product detail page to improve styling on very small devices.

### Lighthouse

- The Lighthouse tool within Chrome Developer tools was used to generate performance scores and identify areas for improvement in both mobile and desktop views of the page.  Lighthouse scoring was performed on the main Store page, as this is the most resource intensive page in the app.  Results of this scoring can be viewed via the links below:
  
  1. [Mobile Score & Summary](lighthouse/)

    ![Mobile Lighthouse Results](screenshots/)
  
  2. [Desktop Score & Summary](lighthouse/)

    ![Desktop Lighthouse Results](screenshots/)

- Please note that while efforts to correct some defects indicated in these results are due to issues found in external dependencies, such as security vulnerabilities in the JQuery version utilized by this MDB implementation, or MDBootstrap's CSS for example, or other faults that are beyond the scope of this project to remedy.

### Noteworthy Issues & Bugs Encountered in Development

- [Open] Image handling when editing existing product

- If the user clicks the 'clear item' checkbox next to the current image when editing a product, and does not add a new image, an error warning is returned when the form is submitted.  Further investigation into how to restore the item to the default image if no image is selected upon editing is needed.

[Return to the Top](#top)