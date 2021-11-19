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

    <div><br/></div>
    <div align="center">
    <img style="width:70%;"  src="static/readme-images/test-gifs/test-header.gif" alt="Test Header">
    </div>

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
- The text should remain aligned to the products text left and right of the product they belong to. (The price is aligned to price, rating aligned to other ratings in the same row)
    <div><br/></div>
    <div align="center">
    <img style="width:90%;"  src="static/read-me/test-gifs/test_products_page.gif" alt="Testing Bar Chart">
    </div>
<!-- # TODO Test links when items hooked up to display the product detail pages -->



<!-- # TODO Test links when items hooked up to display the correct pages -->


#### Further Testing



### Bugs and Issues Resolved
- Having trouble with content appearing over/under the footer, found some information that helped from [stackoverflow](https://stackoverflow.com/questions/19330611/fixed-footer-in-bootstrap) where I was suggested to use 70 or 100vh for the content block.
- Initial test_products_detail_view was throwing a 404 error. Eventually figured out that the others_bought_ids in the view was throwing the exception as the 
products_others_bought in the product created in the test case setUp function did not exist and thus trying to split an empty string in the product_detail view. 
Fixed this by adding an if clause in the view.

### Unsolved Bugs
Currently there are no known bugs.