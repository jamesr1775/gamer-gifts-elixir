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
- All the drop down product pages should retrieve and display the correct products that are related to the drop down option selected.
- The sorting drop down options should sort the products correctly depending on the sort option.

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
- The add to basket button updates the shopping bag with the correct product, product size and quantity.
- The bag in the nav bar should contain the correct grand total depending on the items in the shopping bag.
- If the user tries to add too much of one product they are not able to and thus receive a message telling them of this issue.

<!-- # TODO Reviews Section when implemented -->


##### Add Product
- Admin users can access this page by going to the product management section of My account drop down or by modifying the url.
- Non super users or logged out users should not be able to access the add products form.
- The form and headers should remain centered on the screen for all screen sizes. On smart phones and tablets the width changes to 100% instead of 60%.
- The form text headings should remain to the left border of their input field boxes.
- The choose file and image text remain centered under the last input text field box. 
- The choose image box opens the users explorer for them to select and upload a file.
- The cancel and add product button remain centered under the choose image button.
- The cancel button returns the admin to the all products page.
- The form validators work as expected and do not allow the admin to add the product if required inputs are wrong or missing. A popup should be displayed to the user if the add product button is pressed and the form is not valid.
- If the form is valid the admin is brought to the newly created products detail page after clicking the add product button.
- The cancel button returns the admin to the all products page.

##### Edit Product
- Admin users can access this page by clicking the edit button on the products and products details pages.
- Non super users or logged out users should not be able to access the edit products form.
- All fields of the form should be prefilled in with the selected products fields in their correct input box.
- The form and headers should remain centered on the screen for all screen sizes. On smart phones and tablets the width changes to 100% instead of 60%.
- The form text headings should remain to the left border of their input field boxes.
- The choose file and image text remain centered under the last input text field box. 
- The choose image box opens the users explorer for them to select and upload a file.
- The cancel and update product button remain centered under the choose image button.
- The cancel button returns the admin to the all products page.
- The form validators work as expected and do not allow the admin to update the product if required inputs are wrong or missing. A popup should be displayed to the user if the update product button is pressed and the form is not valid.
- If the form is valid the admin is brought to the updated products detail page after clicking the update product button.
- The clear checkbox if checked should remove the current image of the product.

##### Delete Product
- Admin users can access this page by clicking the delete button on the products and products details pages.
- Non super users or logged out users should not be able to access the delete products page.
- The Product image, name and description are side by side on medium screens and larger with the text under the image on mobiles.
- The cancel and delete product button remain centered under product image / info.
- The cancel button returns the admin to the all products page.
- The delete button on the delete_product.html page will delete the correct product from the store and return the user to the products page.

#### Shopping Bag Page Tests
##### Shopping Bag Layout 
- The table of products in the users bag should be the same layout wise except for on mobile phones when the continue shopping and proceed to checkout buttons are on separate rows. 
- The images in each row remain aligned and are the same heights/ widths.
- The name, price and quantity should remain in their divs and the text is smaller for small screen sizes.

##### Shopping Bag Functionality 
- When no products are in the users bag, the shopping bag page should tell the user that their bag is empty.
- When products are added to the bag they should appear in a table with the price, quantity and buttons to adjust or remove items from their bag.
- The product image loads the products detailed page view.
- The delete button removes the item completely from the users shopping bag.
- The update button changes the quantity of an item to that of the quantity input drop down.
- If a user tries to add more the the maximum threshold allowed they should receive a message telling them they have too much of one product in their bag.
- When products are removed and added the grand total, delivery and total cost is adjusted to reflect the correct value for the current state of the shopping bag.
- The continue shopping button should return the user to the products page.
- The proceed to the checkout button should bring the user to the checkout page.
- The proceed to the checkout button is only present if the bag is not empty.

#### Checkout Tests
##### Checkout Layout
- A table of the products in the shopping bag should be present on the top of the checkout page.
- The total, delivery cost and grand total text is under the products table and hugs the right side of the screen.
- The full name and phone number fields are on the same row for large screens and tablets and are on different rows for smart phones.
- The rest of the fields and the credit card details are all on different rows.
- The view shopping bag and complete checkout buttons are on the same row for all screen sizes except for small screens < 435px  where they are on separate rows.  

##### Checkout Functionality 
- The checkout forms required fields should all be complete before the form can be correctly posted.
- When a field is incorrect or missing upon trying to submit the form the user should get a pop up on the field that is incorrect telling them. 
- If the credit card fields are incorrect they should also receive feedback.
- The view shopping bag button returns the user to their shopping bag.
- When all the details in the form and credit card info are valid, the complete checkout button should process the users order. 
    - The complete checkout button is frozen and a processing spinner is loaded to stop the user from submitting the form again by accident.
    - When the order has been processed the user is brought to the checkout success page.
    - An order success message is loaded in the top right of the page.

##### Checkout Success Layout
- The checkout success page shows the user the delivery information submitted, the order details and the billing information.
- The text should hug the left side of the container.
- The fields are all on separate rows.

##### Checkout Success Functionality 
- When the continue shopping button is pressed, it should take the user back to the products page.

#### Further Testing



### Bugs and Issues Resolved
- Having trouble with content appearing over/under the footer, found some information that helped from [stackoverflow](https://stackoverflow.com/questions/19330611/fixed-footer-in-bootstrap) where I was suggested to use 70 or 100vh for the content block.
- Initial test_products_detail_view was throwing a 404 error. Eventually figured out that the others_bought_ids in the view was throwing the exception as the 
products_others_bought in the product created in the test case setUp function did not exist and thus trying to split an empty string in the product_detail view. 
Fixed this by adding an if clause in the view.
- If a product is added without an image, the website no longer crashes as a default no product image is loaded instead.

### Unsolved Bugs
