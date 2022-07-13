# Testing - SecTech CI Project 5

### [ Return to the project [README document](../README.md#testing) ]

## - Table of Contents -
* [Manual Testing](#manual-testing)
* [Automated Testing](#automated-testing)
* [Code Validation](#code-validation)


## Manual Testing

### UX Goals, User Stories

- #### As a Site Admin..
    - I want to to be able to setup and manage the product list
        - I tested that I could log into the admin panel and have ability to create, read, update or delete (CRUD) a product.  I tested that I could also do this via the main menu login.


- #### As a first time user...  
    -  I want to be able to intuitively navigate the site
        - All menu options were tested to ensure that they opened the correct functionality.  The navigation bar remains at the top of the screen so that the user can easily move between options. The current page selection remains highlighted.

    -  I want to be able to see clear messages about my actions
        - I tested that system messages are displayed during all customer processes (login, checkout etc.)  Messages are coloured according to severity (alerts - yellow, warnings - red, etc.) and are clrealy seen on teh top centre of screen.

    - I want to easily find information about the company and its products
        - I tested that I could click through the product cards on the main screen to reveal full details about the products.  I tested that the About page displays the company information.

    -  I want to be able to Register as a customer of the site
       - I tested that I could create a new registered user from the login screen.

    -  I want to be able receive a registrtion confirmation email
       - I tested that I could verify a user account via a registration email by clicking on the secure link in the email.

- #### As a returning visitor...
    - I want to be able to log into my registered account
        - I tested that I can log in as a user and view my account

      - I want to be able to easily see details of active software licences
        - I tested that when logged in as a user I can see my active software liences on my account page

      - I want to be able to easily see details of the previous purchases
        - I tested that when logged in as a user I can see my previous purchases on my account page

      - I want to be able to quickly purchase additional support or consultancy hours
        - I tested that when logged in as a user I can purchase additional products

### Further Testing

- #### As a Site Admin
    - I want to ensure that site visitors who are unauthenticated cannot access any admin functionality other then viewing site content
        - I tested that unauthenticated visitors get redirected to the sign in page if attempting to access `/customers/account/new`, for example
    - I want to ensure site visitors can't access customer pages or functionality
        - I tested to options to add/edit/delete etc. were not visible to users when not logged in
        - I tested that attempting to access `/<whatsit>/new` or `/<thisotherthing>/new` redirects to a '403 - Forbidden' error message and allows the user to link back to the main page.
    - I want to ensure that site members can not delete posts created by other members
        - I tested that attempting to access (for example) `/comments/8/delete`, which was created by a different user, redirects to a '403 - Forbidden' error message and allows the user to link back to the main page.
    - I want to ensure that site visitors or members can not delete meetups
        - I tested that attempting to access (for example) `/<somethingelse>/4/delete`, which is only allowed by admins, redirects to a '403 - Forbidden' error message and allows the user to link back to the main page.
    - I want the site to be fully responsive on different screen sizes
        - I tested that content resized properly and that the information was clearly readable and accesible on all screen sizes.
<hr>

## Automated Testing
Automated testing was not used for this project.

<hr>

## Code Validation

The [W3C Markup Validator](https://validator.w3.org/#validate_by_uri), [W3C CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator/#validate_by_uri) and the [JSHint JavaScript Code Quality Tool](https://jshint.com) were used to validate every page of the project for syntax errors. **NOTE: All validation was re-run after fixing any errors shown below to ensure that no further errors or warnings existed.**

### HTML
- **`Main home page: home.html`**
<h2 align="center"><img src="w3c-validator-html_main-home-page.html.png"></h2>


### CSS
<h2 align="center"><img src="w3c-validator-css_style.css.png"></h2>

### JavaScript
In the end, JavaScript use was minimal. JSHint returned no errors.

<!-- <h2 align="center"><img src="jshint-1_script.js.png"></h2> -->

### Python PEP8
The [Flake8](https://pypi.org/project/flake8/) linter was used to ensure the code adhered to the Python Style Guidelines. Additionally, [autopep8](https://pypi.org/project/autopep8/) was used to correct code layout in some files to break long lines in a compliant way.

Example usage in the terminal (taking just `home` app in this example):
```
(.venv) ~/dev/code-institute/sectech-pp5%[docs] flake8 --exclude .venv,migrations,tests.py |grep home
./home/models.py:1:1: F401 'django.db.models' imported but unused
./home/admin.py:1:1: F401 'django.contrib.admin' imported but unused
./home/urls.py:16:1: F401 'django.contrib.admin' imported but unused
./home/views.py:9:45: W291 trailing whitespace
./home/views.py:13:80: E501 line too long (92 > 79 characters)
./home/views.py:19:1: W293 blank line contains whitespace
(.venv) ~/dev/code-institute/sectech-pp5%[docs] autopep8 --in-place --aggressive --aggressive home/views.py
```
Just to confirm compliance, here's the result of checking the above `home/views.py` file with [PEP8 Online](http://pep8online.com/checkresult):

<h2 align="center"><img src="pep8-home_views.py.png"></h2>



<hr>

### [ [Click here to return to the project README document](../README.md#testing) ]
