# Esports Epics Testing
The deployed version of the Sorting Visualiser can be found at [Esports Epics](https://esports-epics.herokuapp.com/).

The source code for the project can be viewed at [github](https://github.com/jamesr1775/esports-epics).

## Table of Contents

1. [**Testing**](#testing)
    - [**Code Validation**](#code-validation)
2. [**User Stories Tests**](#testing-user-stories)
3. [**Manual Testing**](#manual-testing)
    - [**Site Header**](#site-header)

4. [**Further Testing**](#further-testing)
5. [**Bugs and Issues Resolved**](#bugs-and-issues-resolved)
6. [**Unsolved Bugs**](#unsolved-bugs)

## Testing
### Code Validation

### Testing User Stories

### Manual Testing
* All manual tests below:
    - were ran on chrome and firefox.
    - were repeated on various screen resolutions using the chrome and firefox developer tools that include desktops, ipad, ipad pro, iphone X, 5, 6 ,7 , 8 and the plus models.
    - were repeated on the developers own smartphone (samsung) and tablet (ipad), desktop and laptop.

#### Site Header & Hero Image
##### Device Specific Layout Checks
- The Header responsiveness was tested by varying the screen size to see that the logo and navbar links were responsive and also that the navbar becomes an expandable burger icon on smartphones.
- The logo stays to the left of the header on all screens with the my account and basket links to the right of the page.
- The website navigation links should be under the logo, the account and the basket links on large screens. When the burger icon is clicked the links should be on the left side of the screen.
- The search bar should be next to the product / offers links on large screen sizes and should be on its own row for smaller screen sizes.

##### Site Header Tests
- The logo was tested that when it is pressed it returns / refreshes to the home page.
- All the product navigation links work and bring the user to the correct products page with the correct products displayed depending on the category selected.
- The nav menu links with a drop down menu should be easily clickable and the drop down menu stays open until another click occurs.
- The search bar functions correctly and displays products related to the users search queries.

##### Site Footer Tests
- The social media icons opens up the relevant social media platforms in a new tab.
- The icons remain centered on all screen sizes.
- The Copyright Info text stays under the icons to the left side of the screen.


#### Home Page Tests

##### Home Carousel
- The Carousel should be responsive and show 3 columns / items for large screens and then 1 column / item for smaller screen sizes (less than 768px).
- The images should remain undistorted when adjusting the screen size.
- The Navigation buttons to cycle through the items in the carousel should increment / decrement the slide index by 1 shifting the cards to the right or left.
- The slider should show which card is in the left most position using carousel dots displayed at the bottom. They should remain centered on all screens at the bottom of the carousel.
- The navigation buttons should remain within the carousel card.
<!-- # TODO Test links when items hooked up to display the correct pages -->

##### Tips / Print Info Cards
- The gift tips and information callout cards should be side by side on tablets and larger screen sizes. 
- On smart phones they should be both on separate rows.
- The cards should be above the footer and under the carousel.
- The images are to remain undistorted for all supported screen resolutions.

    <div><br/></div>
    <div align="center">
    <img style="width:90%;"  src="static/read-me/test-gifs/test_home_page.gif" alt="Testing Bar Chart">
    </div>

#### Products Page Tests

##### All Products
- On large screens and laptops the products page contains 3 products per row with their image, name, price and rating showing.
- The images should adjust to not be distorted for different screen sizes.
- The images in each row remain aligned and are the same heights.
- The name, price and rating should remain under the image and hug the left side of the container they are in.
- The text should remain aligned to the other products text, left and right of the product they belong to. (The price is aligned to price, rating aligned to other ratings in the same row)
    <div><br/></div>
    <div align="center">
    <img style="width:90%;"  src="static/read-me/test-gifs/test_products_page.gif" alt="Testing Bar Chart">
    </div>

##### Product Detail Pages
- The image of a product on the products page should open up the products details page.
- The description, name, rating, price, quantity, size, add to basket and continue shopping buttons should be displayed to the user on the right of the image on large/medium screens and should appear under the image on smart phones screens.
- The continue shopping button should return the user back to the all products page.
- The reviews and other customers purchased sections should be on separate rows under the item image and description.

<!-- # TODO Reviews Section when implemented -->
<!-- # TODO Test Add to basket when implemented -->


##### Add Product
- The form and headers should remain centered on the screen for all screen sizes. On smart phones and tablets the width changes to 100% instead of 60%.
- The form text headings should remain to the left border of their input field boxes.
- The choose file and image text remain centered under the last input text field box. 
- The choose image box opens the users explorer for them to select and upload a file.
- The cancel and add product button remain centered under the choose image button.
- The cancel button returns the admin to the all products page.
- The form validators work as expected and do not allow the admin to add the product if required inputs are wrong or missing. A popup should be displayed to the user if the add product button is pressed and the form is not valid.
- If the form is valid the admin is brought to the newly created products detail page after clicking the add product button.
- The cancel button returns the admin to the all products page.

#### Further Testing



### Bugs and Issues Resolved
- Having trouble with content appearing over/under the footer, found some information that helped from [stackoverflow](https://stackoverflow.com/questions/19330611/fixed-footer-in-bootstrap) where I was suggested to use 70 or 100vh for the content block.
- Initial test_products_detail_view was throwing a 404 error. Eventually figured out that the others_bought_ids in the view was throwing the exception as the 
products_others_bought in the product created in the test case setUp function did not exist and thus trying to split an empty string in the product_detail view. 
Fixed this by adding an if clause in the view.

### Unsolved Bugs
If a product is added without an image, the website currently crashes.