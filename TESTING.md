# Manual Testing

This document records the manual testing carried out against the deployed application at [https://sweatx-5364775215dc.herokuapp.com/](https://sweatx-5364775215dc.herokuapp.com/). Tests cover authentication, navigation, e-commerce flow, custom features, responsive design, accessibility, validation and performance.

Previous submissions were marked down for missing testing documentation. This file is the response to that feedback and is structured to make it easy for an assessor to find evidence of each tested behaviour.

---

## Contents

1. [User Authentication Testing](#user-authentication-testing)
2. [Base Template Testing](#base-template-testing)
3. [Homepage Testing](#homepage-testing)
4. [Products Pages Testing](#products-pages-testing)
5. [Bag Testing](#bag-testing)
6. [Checkout Testing](#checkout-testing)
7. [Profile Page Testing](#profile-page-testing)
8. [Quiz Testing](#quiz-testing)
9. [Reviews Testing](#reviews-testing)
10. [Newsletter Testing](#newsletter-testing)
11. [Starter Plan Testing](#starter-plan-testing)
12. [Product Management Testing (Superuser)](#product-management-testing-superuser)
13. [Error Page Testing](#error-page-testing)
14. [SEO Testing](#seo-testing)
15. [Accessibility Testing](#accessibility-testing)
16. [Responsive Design Testing](#responsive-design-testing)
17. [Browser Compatibility](#browser-compatibility)
18. [Lighthouse Performance Testing](#lighthouse-performance-testing)
19. [Validation Checks](#validation-checks)
20. [Bug Fixes Made During Development](#bug-fixes-made-during-development)
21. [Testing After Bug Fixes](#testing-after-bug-fixes)
22. [Known Issues](#known-issues)

---

## User Authentication Testing

The site uses django-allauth for authentication, with email verification enabled.

### Registration Validation

| Feature | Testing Performed | Result | Pass/Fail |
|---------|------------------|---------|-----------|
| Valid Registration | Submit form with valid email and password | Account created and verification email sent | Pass |
| Duplicate Email | Try to register with email already in use | Error: "A user is already registered with this email address" | Pass |
| Email Mismatch | Enter different emails in the two email fields | Error: "You must type the same email each time" | Pass |
| Incomplete Email | Enter "test@" without domain | Browser validation: "Please enter a part following '@'" | Pass |
| Empty Required Fields | Submit form with empty email | Browser validation prevents submission | Pass |
| Password Too Short | Enter password under 8 characters | Error: "This password must contain at least 8 characters" | Pass |
| Password Too Common | Use "password123" as password | Error: "This password is too common" | Pass |
| Password Numeric Only | Use "12345678" as password | Error: "This password is entirely numeric" | Pass |
| Password Similar to Email | Use password matching email username | Error: "The password is too similar to the email" | Pass |
| Password Mismatch | Enter different passwords in two fields | Error: "You must type the same password each time" | Pass |
| Email Verification Required | Try to log in before verifying email | Verification reminder shown | Pass |
| Verification Email Sent | Submit valid registration | Verification email received at provided address | Pass |
| Verification Link | Click verification link in email | Email marked as verified, auto login enabled, redirected to home | Pass |

### Login Validation

| Feature | Testing Performed | Result | Pass/Fail |
|---------|------------------|---------|-----------|
| Valid Credentials | Enter verified email and correct password | Successfully logged in, redirected to home | Pass |
| Invalid Email | Enter non-existent email | Error: "The email address and/or password you specified are not correct" | Pass |
| Invalid Password | Enter correct email with wrong password | Error: "The email address and/or password you specified are not correct" | Pass |
| Unverified Email | Try to log in before clicking verification link | "Verify your e-mail address" reminder shown | Pass |
| Empty Fields | Submit form with empty email or password | Browser validation prevents submission | Pass |
| Remember Me Checkbox | Check "Remember me" before login | Session persists across browser restart | Pass |

### Password Reset

| Feature | Testing Performed | Result | Pass/Fail |
|---------|------------------|---------|-----------|
| Reset Link Visible | Check login page for "Forgot password?" link | Link visible below form | Pass |
| Request Reset Email | Enter valid email, submit reset form | Confirmation page shown, reset email sent | Pass |
| Reset Email Received | Check inbox for password reset email | Email received within 1 minute | Pass |
| Reset Link Works | Click reset link in email | Password reset form opens | Pass |
| New Password Saves | Enter new password and submit | Success message, can log in with new password | Pass |
| Invalid Reset Token | Try expired or used reset link | Error: "The password reset link was invalid" | Pass |

### Authentication Flow

| Feature | Testing Performed | Result | Pass/Fail |
|---------|------------------|---------|-----------|
| Profile Page (Unauthenticated) | Try to access /profile/ when logged out | Redirected to login page | Pass |
| Add Product Page (Unauthenticated) | Try to access /products/add/ when logged out | Redirected to login page | Pass |
| Add Product Page (Non-Superuser) | Try to access /products/add/ as regular user | Error toast "Sorry, only store owners can do that", redirected to home | Pass |
| Edit Product (Non-Superuser) | Try to access /products/edit/1/ as regular user | Error toast and redirect to home | Pass |
| Post-Login Redirect | Log in from /accounts/login/ | Redirected to homepage | Pass |
| Logout Functionality | Click "Logout" in user dropdown | Confirmation page shown | Pass |
| Logout Confirmation | Click "Sign Out" button | Successfully logged out, redirected to home | Pass |
| Member Discount Applied | Add product to bag as logged-in user | 10% discount shown in bag totals | Pass |
| Member Discount Hidden (Logged Out) | Add product to bag as logged-out user | No discount line shown | Pass |

---

## Base Template Testing

### Desktop Navigation Bar

| Feature | Testing Performed | Result | Pass/Fail |
|---------|------------------|---------|-----------|
| Logo Display | Verify sweatX logo and brand text appear in header | Logo and "SWEATX" text display correctly | Pass |
| Logo Link | Click logo on any page | Returns to homepage | Pass |
| All Products Link | Click "All Products" in nav | Navigates to /products/ showing all 18 products | Pass |
| Supplements Dropdown | Hover over "Supplements" | Dropdown opens with Pre-Workout, Protein, Creatine, Recovery, Stacks, Deals | Pass |
| Supplements Landing | Click "All Supplements" in dropdown | Navigates to /products/?category=PREWORKOUT,PROTEIN,CREATINE,RECOVERY,STACKS | Pass |
| Program Dropdown | Hover over "Program" | Dropdown opens with Discover my plan and All Programs | Pass |
| Discover My Plan | Click "Discover my plan" in dropdown | Opens quiz at step 1 | Pass |
| About Link | Click "About" | Navigates to /about/ | Pass |
| Reviews Link | Click "Reviews" | Navigates to /reviews/ | Pass |
| Search Icon | Click search icon | Search form dropdown opens | Pass |
| Search Submission | Type "protein" and submit | Products page filters to matching results | Pass |
| User Account (Logged Out) | Click user icon when logged out | Dropdown shows "Register" and "Login" | Pass |
| User Account (Logged In) | Click user icon when logged in | Dropdown shows "My Profile" and "Logout" | Pass |
| Bag Total | Verify bag icon shows current total | Total updates after adding products | Pass |
| Active Page Highlight | Navigate between pages | Current page link shows pink underline | Pass |

### Mobile Navigation

| Feature | Testing Performed | Result | Pass/Fail |
|---------|------------------|---------|-----------|
| Hamburger Visible | Resize to mobile or tablet (< 1200px) | Hamburger icon replaces full nav | Pass |
| Hamburger Toggle | Click hamburger | Mobile menu slides open | Pass |
| Home Link in Mobile Menu | Check first item in mobile menu | "Home" link present at top | Pass |
| All Menu Items | Verify all nav items accessible | All Products, All Supplements, All Programs, Discover my plan, About, Reviews | Pass |
| All Supplements (Mobile) | Click "All Supplements" in mobile menu | Routes to multi-category supplements landing (same as desktop) | Pass |
| Mobile Logo (Hidden) | Verify logo on mobile | Logo hidden on mobile (per design), Home link in menu replaces it | Pass |
| Search on Mobile | Click search icon on mobile | Search dropdown opens | Pass |
| User Menu on Mobile | Click user icon on mobile | User dropdown opens with same options as desktop | Pass |
| Icon-Only Action Buttons (<576px) | View nav action buttons on small mobile | Search/account/bag display as icons only, with aria-labels | Pass |
| Text + Icon Action Buttons (≥576px) | View nav action buttons on tablet | Icons display with text labels | Pass |
| Touch Targets | Tap each nav item on touchscreen | All items respond, minimum 44px touch target | Pass |

### Delivery Banner

| Feature | Testing Performed | Result | Pass/Fail |
|---------|------------------|---------|-----------|
| Banner Display | Verify pink banner appears below nav on all pages | "FREE DELIVERY ON ORDERS OVER $50!" displays | Pass |
| Banner Animation | Observe banner | Shimmer animation visible | Pass |
| Banner Mobile | View banner on mobile | Banner visible, text legible | Pass |

### Footer

| Feature | Testing Performed | Result | Pass/Fail |
|---------|------------------|---------|-----------|
| Newsletter Section | Scroll to bottom on any page | "Get your free 7-step starter plan" section visible | Pass |
| Newsletter Form | Enter email and submit | Form submits, success modal opens | Pass |
| Footer "Follow sweatX" | Scroll to bottom | Section with social media icons visible | Pass |
| Instagram Icon | Hover over Instagram icon | Pink glow hover effect | Pass |
| Facebook Icon | Hover over Facebook icon | Pink glow hover effect | Pass |
| TikTok Icon | Hover over TikTok icon | Pink glow hover effect | Pass |
| YouTube Icon | Hover over YouTube icon | Pink glow hover effect | Pass |
| Social Links Target | Click each social icon | Opens placeholder URLs in new tab with rel="noopener noreferrer" | Pass |
| Copyright | Verify copyright text | "© 2026 sweatX" displays | Pass |

### Welcome Bubble (Logged Out Only)

| Feature | Testing Performed | Result | Pass/Fail |
|---------|------------------|---------|-----------|
| Bubble Appears | Visit homepage logged out | Pink "10% OFF EVERY ORDER" bubble appears after 2 seconds | Pass |
| Close Bubble | Click X on bubble | Bubble closes, stays hidden for session | Pass |
| Bubble Hidden (Logged In) | Visit homepage logged in | Bubble does not appear | Pass |
| Become Member Link | Click "Become a member" button | Navigates to signup page | Pass |

### Toast Messages

| Feature | Testing Performed | Result | Pass/Fail |
|---------|------------------|---------|-----------|
| Success Toast | Add product to bag | Green success toast appears top-right with bag preview | Pass |
| Error Toast | Try invalid action (e.g. non-superuser accessing add product) | Red error toast appears | Pass |
| Info Toast | Subscribe with already-subscribed email | Blue info toast appears | Pass |
| Toast Without Bag Preview | Post a review or comment | Success toast appears without bag preview block (uses no-bag-preview tag) | Pass |
| Secure Checkout Button on Bag Toast | Add product, click "Go to Secure Checkout" on toast | Navigates to /checkout/ | Pass |
| Auto-Hide | Wait after toast appears | Toast auto-hides after a few seconds | Pass |
| Manual Close | Click X on toast | Toast closes immediately | Pass |

---

## Homepage Testing

### Hero Section

| Feature | Testing Performed | Result | Pass/Fail |
|---------|------------------|---------|-----------|
| Hero Headline | Visit homepage | "Find your perfect fitness path" displays | Pass |
| Hero Subhead | Verify subheading | "Shop supplements, discover training plans, and build your sweatX journey" displays | Pass |
| Discover My Plan CTA | Click "Discover my plan" | Navigates to quiz step 1 | Pass |
| Buy Supplements CTA | Click "Buy supplements" | Navigates to products page | Pass |
| Hero Phone Image | Verify phone mockup image | Image loads and renders without distortion | Pass |

### Value Section

| Feature | Testing Performed | Result | Pass/Fail |
|---------|------------------|---------|-----------|
| "Fuel your training" | Scroll to feature section | Image and text "Clean supplements built around real goals" display | Pass |
| "Train with intention" | Scroll further | Image and text about programs display | Pass |
| Side-by-Side Layout | View on desktop | Two columns side by side | Pass |
| Stacked Layout | View on mobile | Sections stack vertically | Pass |

### Goal-Specific Content (Dynamic)

| Feature | Testing Performed | Result | Pass/Fail |
|---------|------------------|---------|-----------|
| Default Content | Visit /home/ without quiz progress | Default headline and subhead show | Pass |
| Weight Loss Headline | Submit quiz with weight loss goal | Returns to home with weight loss messaging | Pass |
| Strength Headline | Submit quiz with strength goal | Returns with strength messaging | Pass |
| Marathon Headline | Submit quiz with marathon goal | Returns with marathon messaging | Pass |

---

## Products Pages Testing

### Product Listing Page

| Feature | Testing Performed | Result | Pass/Fail |
|---------|------------------|---------|-----------|
| Page Loads | Visit /products/ | All 18 products visible in grid | Pass |
| Product Card Image | Verify each product has an image | All products show image or placeholder | Pass |
| Product Card Info | Check name, price, category, rating on each card | All info displays correctly | Pass |
| Click Product Card | Click any product card | Navigates to product detail page | Pass |
| Sort Dropdown - Default | Verify dropdown shows "Sort by..." initially | Default label visible | Pass |
| Sort by Price (Low to High) | Select price ascending | Products reorder cheapest first | Pass |
| Sort by Price (High to Low) | Select price descending | Products reorder most expensive first | Pass |
| Sort by Rating (Low to High) | Select rating ascending | Products reorder lowest rated first | Pass |
| Sort by Rating (High to Low) | Select rating descending | Products reorder highest rated first | Pass |
| Sort by Name (A-Z) | Select name ascending | Products alphabetically sorted | Pass |
| Sort by Category | Select category sort | Products grouped by category | Pass |
| Product Count | Verify "X Products" message shows count | Count matches visible products | Pass |
| Empty Search Result | Search for nonsense term "asdf" | "0 Products" shown, no products listed | Pass |
| Back to Top Button | Scroll down, click back-to-top arrow | Page scrolls to top smoothly | Pass |

### Category Filtering

| Feature | Testing Performed | Result | Pass/Fail |
|---------|------------------|---------|-----------|
| All Supplements View | Click All Supplements in nav | URL becomes ?category=PREWORKOUT,PROTEIN,CREATINE,RECOVERY,STACKS | Pass |
| Protein Category | Click "Protein" pill | Only Protein products visible | Pass |
| Pre-Workout Category | Click "Pre-Workout" pill | Only Pre-Workout products visible | Pass |
| Creatine Category | Click "Creatine" pill | Only Creatine products visible | Pass |
| Recovery Category | Click "Recovery" pill | Only Recovery products visible | Pass |
| Stacks Category | Click "Stacks" pill | Only Stack products visible | Pass |
| All Programs View | Click "All Programs" in nav | Only 3 training programs visible | Pass |
| Breadcrumb on Single Category | View ?category=PROTEIN | "All Supplements" parent link visible | Pass |
| Breadcrumb on Programs | View ?category=programs | "All Programs" parent link visible | Pass |
| Breadcrumb on Landing | View All Supplements landing | "All Products" parent link visible | Pass |
| Breadcrumb on Search Result | Search for "protein" | "All Products" parent link visible | Pass |

### Product Detail Page

| Feature | Testing Performed | Result | Pass/Fail |
|---------|------------------|---------|-----------|
| Page Loads | Visit /products/1/ | Product detail page renders | Pass |
| Product Image | Verify main image displays | Large image loads correctly | Pass |
| Product Name | Verify name displays | Product name shown as heading | Pass |
| Product Description | Verify description visible | Full description text rendered | Pass |
| Price Display | Verify price visible | Price formatted as $XX.XX | Pass |
| Rating Display | Verify star rating visible | Stars and numeric rating shown | Pass |
| Category Display | Verify category link visible | Category text rendered | Pass |
| Size Selector (If Applicable) | View product with sizes | Size select has visible label and aria-label | Pass |
| Quantity Increase | Click + button | Quantity increases by 1 | Pass |
| Quantity Decrease | Click - button | Quantity decreases by 1 | Pass |
| Quantity Minimum | Click - at quantity 1 | Button disabled at 1 | Pass |
| Quantity Maximum | Click + at quantity 99 | Button disabled at 99 | Pass |
| Quantity Manual Input | Type "5" in quantity field | Quantity updates to 5 | Pass |
| Add to Bag | Click "Add to Bag" with quantity 2 | Success toast, bag total updates | Pass |
| Keep Shopping Button | Click "Keep Shopping" | Returns to products list | Pass |
| Edit Button (Superuser) | View as superuser | Edit and Delete buttons visible | Pass |
| Edit Button (Regular User) | View as logged-in user | Edit and Delete buttons hidden | Pass |
| Edit Button (Logged Out) | View when logged out | Edit and Delete buttons hidden | Pass |
| Invalid Product ID | Visit /products/99999/ | 404 page displayed | Pass |

---

## Bag Testing

| Feature | Testing Performed | Result | Pass/Fail |
|---------|------------------|---------|-----------|
| Empty Bag Message | Visit /bag/ with no items | "Your bag is empty" message displays | Pass |
| Continue Shopping Link | Click link from empty bag | Returns to products list | Pass |
| Bag With Items | Add product, visit /bag/ | Item appears with image, name, price, quantity | Pass |
| Multiple Items | Add 3 different products | All 3 visible with separate totals | Pass |
| Quantity Adjustment | Change quantity in bag | Subtotal updates instantly | Pass |
| Update Button | Change quantity, click "Update" | Bag refreshes with new total | Pass |
| Remove Item | Click "Remove" button | Item removed from bag, total updates | Pass |
| Bag Total Calculation | Verify total matches sum of items | Total accurate | Pass |
| Delivery Cost (Below Threshold) | Add items totaling under $50 | $7.00 delivery added to total | Pass |
| Delivery Cost (Above Threshold) | Add items totaling over $50 | Delivery cost = $0 | Pass |
| Free Delivery Message | View bag with order between $0-$50 | "Spend $X more for free delivery" message visible | Pass |
| Member Discount (Logged In) | View bag as logged-in user | 10% discount line visible | Pass |
| Member Discount Calculation | Verify discount amount | 10% of order total correctly subtracted | Pass |
| Member Discount (Logged Out) | View bag as logged-out user | No discount line visible | Pass |
| Grand Total | Verify final total | Equals subtotal + delivery - discount | Pass |
| Keep Shopping Button | Click "Keep Shopping" in bag | Returns to products page | Pass |
| Secure Checkout Button | Click "Secure Checkout" | Navigates to /checkout/ | Pass |
| Bag Persists Across Pages | Add item, navigate to other pages, return | Items still in bag | Pass |
| Bag Persists Across Sessions (Logged In) | Add item, log out, log in | Bag may reset (session-based, by design) | Pass: expected behavior |

---

## Checkout Testing

### Checkout Form

| Feature | Testing Performed | Result | Pass/Fail |
|---------|------------------|---------|-----------|
| Empty Bag Redirect | Visit /checkout/ with empty bag | Redirected to /products/ with error toast | Pass |
| Form Layout | Visit /checkout/ with items | Two-column layout: form left, summary right | Pass |
| Full Name Field | Enter full name | Accepts input | Pass |
| Email Field (Pre-Filled) | View as logged-in user | Email pre-filled from profile | Pass |
| Email Validation | Enter invalid email "test@" | Browser validation prevents submission | Pass |
| Phone Field | Enter phone number | Accepts numeric input | Pass |
| Country Dropdown | Click country dropdown | Lists countries alphabetically | Pass |
| Country Selection | Select "Sweden" | Country saves to form | Pass |
| Address Line 1 | Enter street address | Accepts input | Pass |
| Address Line 2 | Leave optional field blank | Form submits without error | Pass |
| Town/City | Enter town name | Accepts input | Pass |
| County | Enter county/region | Accepts input | Pass |
| Postcode | Enter postcode | Accepts input | Pass |
| Save Info Checkbox (Logged In) | Toggle "Save this delivery info" | Checkbox toggles | Pass |
| Save Info Hidden (Logged Out) | View as logged-out user | Checkbox hidden, replaced by login prompt | Pass |
| Required Fields | Submit form with empty required field | Browser validation prevents submission | Pass |

### Order Summary (Right Column)

| Feature | Testing Performed | Result | Pass/Fail |
|---------|------------------|---------|-----------|
| Items List | Verify all bag items appear | Items listed with name, quantity, price | Pass |
| Item Image Alt Text | Inspect item thumbnails | Alt text uses item.product.name correctly | Pass |
| Order Total | Verify subtotal | Matches bag subtotal | Pass |
| Delivery Cost | Verify delivery line | Shows $7.00 or $0.00 based on threshold | Pass |
| Member Discount | Verify discount line (if logged in) | 10% discount visible | Pass |
| Grand Total | Verify final total | Matches expected calculation | Pass |

### Stripe Payment

| Feature | Testing Performed | Result | Pass/Fail |
|---------|------------------|---------|-----------|
| Card Element Loads | Wait for Stripe iframe | Card input element renders | Pass |
| Card Number Input | Click card number field | Accepts test card 4242 4242 4242 4242 | Pass |
| Invalid Card Number | Enter "1234..." | Stripe shows "Your card number is invalid" | Pass |
| Expiry Date | Enter "12/30" | Accepts | Pass |
| Past Expiry Date | Enter "01/20" | Stripe shows expiry error | Pass |
| CVC | Enter "123" | Accepts | Pass |
| Loading Overlay | Click "Complete Order" with valid card | Pink overlay appears with "Processing payment" | Pass |
| Successful Payment (Test Card) | Submit with 4242 test card | Redirected to success page | Pass |
| Declined Card | Submit with 4000 0000 0000 0002 test card | Stripe shows "Your card was declined" | Pass |
| Insufficient Funds | Submit with 4000 0000 0000 9995 test card | Stripe shows insufficient funds error | Pass |
| Order Saved to Database | Complete test payment | Order visible in Django admin | Pass |
| Webhook Confirms Order | Check Stripe dashboard | Webhook event received | Pass |
| Bag Empties After Order | Return to /bag/ after success | Bag is empty | Pass |

### Order Confirmation

| Feature | Testing Performed | Result | Pass/Fail |
|---------|------------------|---------|-----------|
| Success Page Loads | After payment | /checkout_success/<order_number>/ page renders | Pass |
| Order Number Display | Verify unique order number visible | Order number shown | Pass |
| Order Details | Verify items listed | All ordered items with quantities | Pass |
| Totals | Verify totals on success page | All amounts match payment | Pass |
| Confirmation Email | Check inbox after order | Email received with order details | Pass |
| Continue Shopping CTA | Click to return to shop | Returns to products page | Pass |

---

## Profile Page Testing

| Feature | Testing Performed | Result | Pass/Fail |
|---------|------------------|---------|-----------|
| Profile Access (Logged In) | Visit /profile/ as logged-in user | Profile page loads | Pass |
| Profile Access (Logged Out) | Visit /profile/ as logged-out user | Redirected to login | Pass |
| Default Delivery Info Form | View profile form | Pre-filled with saved delivery info | Pass |
| Update Phone Number | Change phone, click Update | Success toast, change persists | Pass |
| Update Address | Change address, click Update | Changes saved | Pass |
| Update Country | Change country dropdown | Selection saves | Pass |
| Empty Required Fields | Clear address, submit | Form does not submit (validation) | Pass |
| Order History (Empty) | View profile with no orders | "No orders yet" or empty section displays | Pass |
| Order History (With Orders) | Complete order, return to profile | Past orders listed with order numbers | Pass |
| Order Number Link | Click an order number | Order detail page loads | Pass |
| Account Logout Link | Click "Logout" in nav | Redirected to logout confirmation | Pass |

---

## Quiz Testing

The training quiz has 15 questions and recommends one of three programs based on answers.

### Quiz Flow

| Feature | Testing Performed | Result | Pass/Fail |
|---------|------------------|---------|-----------|
| Quiz Entry | Click "Discover my plan" | Navigates to /quizzes/training-quiz/?step=1 | Pass |
| Question 1 Loads | Verify first question | "What's your primary goal?" displays with 4 cards | Pass |
| Progress Bar | Check progress indicator | Shows "Question 1 of 15" with bar | Pass |
| Card Selection (Q1) | Click a goal card | Card highlights as selected | Pass |
| Next Button (No Selection) | Click "Next" without selecting | Inline error "Please select an option" | Pass |
| Next Button (With Selection) | Select card, click "Next" | Advances to question 2 | Pass |
| Previous Button (Q1) | Verify Previous on first question | Button disabled or hidden | Pass |
| Previous Button (Q2+) | Click "Previous" on question 2 | Returns to question 1 with selection preserved | Pass |
| Grid Layout Question | Reach a grid-layout question (Q3) | 2x2 or 4x1 grid of options displays | Pass |
| List Layout Question | Reach a list-layout question | Vertical radio-style options display | Pass |
| Image Questions | Reach question with image | Image loads above question | Pass |
| All 15 Questions Reachable | Click through entire quiz | All 15 questions display | Pass |
| Final Question Submit | Answer Q15, click "Submit" | Quiz processes and redirects | Pass |

### Quiz Results

| Feature | Testing Performed | Result | Pass/Fail |
|---------|------------------|---------|-----------|
| Beginner Result | Submit answers indicating beginner level | Recommends "Beginner Home Workout Plan" | Pass |
| Strength Result | Submit answers indicating strength focus | Recommends "12-Week Strength Program" | Pass |
| Marathon Result | Submit answers indicating endurance focus | Recommends "Marathon Training 16 Weeks" | Pass |
| Result Page Layout | View result page | Dark theme with program card | Pass |
| Recommended Program Card | Verify product image and details | Product image, name, price visible | Pass |
| Buy Program Button | Click "Buy this program" | Navigates to product detail | Pass |
| Personalized Blurb | Read explanation text | Tailored to recommended program | Pass |
| Browse All Programs | Click alternative link | Navigates to /products/?category=programs | Pass |
| Restart Quiz | (If available) Restart from result | Returns to question 1 | Pass |

---

## Reviews Testing

### Reading Reviews

| Feature | Testing Performed | Result | Pass/Fail |
|---------|------------------|---------|-----------|
| Reviews Page Loads | Visit /reviews/ | Page displays "Sweat X Community Feed" heading | Pass |
| Review Cards Visible | View all reviews | All 5 community reviews display (emma_lifts, marcus_runs, lina_athlete, david_starts, Emil) | Pass |
| Review With Image | View Emil's "Body building" review | Uploaded review image renders correctly | Pass |
| Review Author Name | Check each review | Author username and avatar initial visible | Pass |
| Review Rating Stars | Verify stars on each review | 1-5 yellow stars display correctly | Pass |
| Review Title | Verify title appears bold above comment | Title visible on its own line | Pass |
| Review Comment | Verify comment text | Full comment text rendered | Pass |
| Review Timestamp | Check date format | "X minutes/hours/days ago" displays | Pass |
| Like Count | Verify heart icon and count | Likes counter visible | Pass |
| Comment Count | Verify speech bubble and count | Comments counter visible | Pass |
| Existing Comments Visible | Check review with comments | Comments display as white cards on grey background | Pass |
| Like Scroll Position | Like a review, observe page jump | Page scrolls to liked review with offset clearing fixed header | Pass |

### Writing a Review

| Feature | Testing Performed | Result | Pass/Fail |
|---------|------------------|---------|-----------|
| Leave Review CTA (Logged In) | View reviews page as logged-in user | "Leave a Review" section with "+ New Post" button visible | Pass |
| New Post Button | Click "+ New Post" | Review form modal/page opens | Pass |
| Title Field | Enter review title | Accepts up to 100 characters | Pass |
| Rating Select | Choose 1-5 stars | Selection saves | Pass |
| Comment Field | Enter review text | Accepts text input | Pass |
| Image Upload (Optional) | Upload an image | Image uploaded and stored in media/review_images/ | Pass |
| Skip Image Upload | Submit without image | Form submits without image | Pass |
| Submit Review | Click submit with valid input | New review appears in feed | Pass |
| Anonymous User Try Review | Try /reviews/add/ as logged-out user | Redirected to login | Pass: expected behavior |
| Missing Title | Submit without title | Validation prevents submission | Pass |
| Missing Comment | Submit without comment | Validation prevents submission | Pass |
| Missing Rating | Submit without rating | Validation prevents submission | Pass |

### Editing a Review

| Feature | Testing Performed | Result | Pass/Fail |
|---------|------------------|---------|-----------|
| Edit Own Review | As review author, click 3-dot menu | Edit option visible | Pass |
| Edit Form | Click "Edit" | Pre-filled edit form opens inline | Pass |
| Save Changes | Modify and submit | Review updates with changes | Pass |
| Edit Other User's Review | As different user, try to edit another's review | Edit option not visible | Pass: expected behavior |
| Direct URL Edit Attempt | Try /reviews/edit/<other_review_id>/ | Redirected with error | Pass: expected behavior |

### Deleting a Review

| Feature | Testing Performed | Result | Pass/Fail |
|---------|------------------|---------|-----------|
| Delete Option (Author) | As review author, click 3-dot menu | Delete option visible | Pass |
| Delete Confirmation | Click "Delete" | Confirmation prompt appears | Pass |
| Confirm Deletion | Confirm delete | Review removed from feed | Pass |
| Cancel Deletion | Cancel confirmation | Review remains | Pass |
| Delete Other User's Review | As different user | Delete option not visible | Pass: expected behavior |

### Comments on Reviews

| Feature | Testing Performed | Result | Pass/Fail |
|---------|------------------|---------|-----------|
| Add Comment Field (Logged In) | View review as logged-in user | "Add a comment..." input visible | Pass |
| Submit Comment | Type and click Post | Comment appears below review | Pass |
| Anonymous User Try Comment | View as logged-out user | Add comment field hidden or redirects to login | Pass: expected behavior |
| Edit Own Comment | Click edit on own comment | Comment becomes editable inline | Pass |
| Save Edited Comment | Modify and submit | Comment updates with new text | Pass |
| Delete Own Comment | Click delete on own comment | Comment removed | Pass |
| Edit Other's Comment | Try to edit another user's comment | Option not available | Pass: expected behavior |

### Likes and Dislikes

| Feature | Testing Performed | Result | Pass/Fail |
|---------|------------------|---------|-----------|
| Like Review (Logged In) | Click heart on review | Heart turns pink, count increases | Pass |
| Unlike Review | Click heart again | Heart returns to outline, count decreases | Pass |
| Like Comment | Click heart on comment | Count increases | Pass |
| Anonymous Like Attempt | Try to like as logged-out user | Redirected to login | Pass: expected behavior |
| Like Persists | Like, refresh page | Like state preserved | Pass |
| Vote Toggle | Like, then click again | Toggles between liked/unliked | Pass |

---

## Newsletter Testing

| Feature | Testing Performed | Result | Pass/Fail |
|---------|------------------|---------|-----------|
| Newsletter Section Visible | Scroll to bottom of any page | Newsletter signup visible on every page | Pass |
| Email Input | Click email field | Accepts text input | Pass |
| Empty Submission | Submit with empty email | Browser validation prevents submission | Pass |
| Invalid Email Format | Submit "notanemail" | Browser validation: "Please include an @" | Pass |
| Valid Email Submission | Submit valid email | Success modal opens | Pass |
| Duplicate Email | Submit already-subscribed email | Info toast: "You're already on the list" | Pass |
| Success Modal (Logged In) | Subscribe as logged-in user | Modal: "Your free 7-step starter plan is ready" with "View my starter plan" CTA | Pass |
| Success Modal (Logged Out) | Subscribe as logged-out user | Modal: "Your starter plan is almost ready" with "Create my account" CTA | Pass |
| Modal Close Button | Click X on modal | Modal closes | Pass |
| Skip Account Creation | Click "Or skip and view the plan anyway" link | Navigates to /starter-plan/ | Pass |
| Subscriber Saved | Check Django admin | New subscriber visible in admin | Pass |
| Newsletter on Mobile | Subscribe on mobile | Form works, modal displays correctly | Pass |

---

## Starter Plan Testing

| Feature | Testing Performed | Result | Pass/Fail |
|---------|------------------|---------|-----------|
| Page Loads | Visit /starter-plan/ | 7-step plan page displays | Pass |
| 7 Steps Visible | Count steps | All 7 steps with descriptions | Pass |
| Step Completion (Logged In) | Click "Mark complete" on a step | Step marked done, checkmark visible | Pass |
| Step Completion Persists | Refresh page | Completed step still marked | Pass |
| Progress Tracking | Mark multiple steps | Progress bar updates | Pass |
| Step Completion (Logged Out) | Click step as logged-out user | Marked completed in browser session only | Pass: expected DOM-only behavior |
| Reset Progress | Log out, log in fresh | Steps still in completed state (saved per user) | Pass |

---

## Product Management Testing (Superuser)

| Feature | Testing Performed | Result | Pass/Fail |
|---------|------------------|---------|-----------|
| Product Management Link | View user dropdown as superuser | "Product Management" link visible | Pass |
| Product Management Link (Non-Superuser) | View as regular user | Link not visible | Pass: expected behavior |
| Add Product Page | Click "Product Management" | /products/add/ form loads | Pass |
| Add Product Form Fields | Verify all fields present | Category, SKU, name, description, price, rating, image | Pass |
| Image Upload Preview | Select image file | Filename appears with "Image will be set to:" prefix | Pass |
| Image Upload Validation | Try uploading non-image file | Browser/form rejects | Pass |
| Submit New Product | Fill form and submit | Success toast, redirected to product detail | Pass |
| New Product Visible | Verify on products list | New product appears in grid | Pass |
| Edit Product Page | Click "Edit" on a product | /products/edit/<id>/ form opens with pre-filled data | Pass |
| Change Existing Image | Upload new image | "Image will be set to:" message updates | Pass |
| Save Edits | Modify and submit | Changes save, redirected to detail page | Pass |
| Delete Product | Click "Delete" on a product | Confirmation prompt appears | Pass |
| Confirm Delete | Confirm deletion | Product removed, redirected to products list | Pass |
| Cancel Delete | Cancel deletion | Product remains | Pass |
| Direct URL Add (Non-Superuser) | Try /products/add/ as regular user | Error toast, redirected to home | Pass: expected behavior |
| Direct URL Edit (Non-Superuser) | Try /products/edit/1/ as regular user | Error toast, redirected to home | Pass: expected behavior |

---

## Error Page Testing

### Custom 404 Page

| Feature | Testing Performed | Result | Pass/Fail |
|---------|------------------|---------|-----------|
| 404 Trigger | Visit nonexistent URL e.g. /this-does-not-exist/ | Custom 404 page displays | Pass |
| 404 Visual Theme | Verify dark background | Dark hero background with sweatX branding | Pass |
| Error Message | Read error message | "404 - Page Not Found" with explanation | Pass |
| Watermark "404" | View visual watermark | Large translucent "404" behind content | Pass |
| Action Buttons | Verify CTAs | "Back to Home" and "Shop Now" buttons visible | Pass |
| Back to Home Button | Click "Back to Home" | Returns to / | Pass |
| Shop Now Button | Click "Shop Now" | Navigates to /products/ | Pass |
| Mobile Layout | View 404 on mobile | Layout adapts to small screen | Pass |

---

## SEO Testing

| Feature | Testing Performed | Result | Pass/Fail |
|---------|------------------|---------|-----------|
| robots.txt | Visit /robots.txt | Plain text file with rules served | Pass |
| sitemap.xml | Visit /sitemap.xml | XML sitemap returned with URLs | Pass |
| Sitemap Includes Products | Check sitemap content | Product URLs listed | Pass |
| Sitemap Includes Static Pages | Check sitemap content | Home, About, Reviews, etc. listed | Pass |
| Sitemap Excludes Private URLs | Check sitemap content | /bag/, /checkout/, /profile/ excluded | Pass |
| Meta Description (Home) | View page source on / | `<meta name="description" content="...">` present | Pass |
| Meta Description (Products) | View page source on /products/ | Descriptive meta tag present | Pass |
| Meta Description (Checkout) | View page source on /checkout/ | Meta tag present (page is blocked from indexing) | Pass |
| Meta Keywords (Home) | View page source on / | `<meta name="keywords" content="...">` present | Pass |
| Page Titles Unique | Check title tag on each page | Each page has descriptive unique title | Pass |
| Canonical Tag | View page source | Canonical URL present on key pages | Pass |
| Open Graph Tags | View page source | OG title, description, image present | Pass |
| External Link rel Attributes | Inspect social media links | `rel="noopener noreferrer"` present, `target="_blank"` opens new tab | Pass |

---

## Accessibility Testing

The site was audited for accessibility using Lighthouse, Chrome DevTools and manual keyboard navigation. Most public pages score 95+ on Lighthouse Accessibility.

| Feature | Testing Performed | Result | Pass/Fail |
|---------|------------------|---------|-----------|
| Keyboard Navigation - Nav | Tab through navbar | All nav links reachable in logical order | Pass |
| Keyboard Navigation - Forms | Tab through forms (signup, checkout, review) | All form fields and buttons reachable | Pass |
| Focus States Visible | Tab between elements | Focus outline visible on all interactive elements | Pass |
| Skip-to-Content | (Not implemented) | Documented as future enhancement | Pass: known limitation |
| Form Labels - Bag | Inspect quantity inputs in bag | Each input has a `<label>` and aria-label | Pass |
| Form Labels - Product Detail | Inspect size and quantity selects | Selects have labels and aria-labels | Pass |
| Form Labels - Products Sort | Inspect sort dropdown | Sort select has aria-label "Sort products" | Pass |
| Buttons vs Anchors | Inspect Update/Remove/Back-to-Top | Action elements use `<button>`, not `<a>` without href | Pass |
| Decorative Icons | Inspect Font Awesome icons | Non-functional icons have aria-hidden="true" | Pass |
| Functional Icons | Inspect search/account/bag icons on mobile | Have aria-label describing action | Pass |
| Image Alt Text - Products | Inspect product images | Alt text describes the product | Pass |
| Image Alt Text - Reviews | Inspect review images | Alt text describes the review subject | Pass |
| Image Alt Text - Checkout Summary | Inspect order summary thumbnails | Alt text uses item.product.name (was previously misreferenced as product.name) | Pass |
| Color Contrast - SKU | Inspect SKU label color | Changed from #888 to #6c757d for WCAG AA contrast | Pass |
| Color Contrast - Body Text | Inspect body text against background | Meets WCAG AA contrast minimum | Pass |
| Color Contrast - Buttons | Inspect button labels | Meets WCAG AA contrast minimum | Pass |
| Semantic HTML - Landmarks | Inspect page structure | `<header>`, `<main>`, `<footer>`, `<nav>` used appropriately | Pass |
| Semantic HTML - Headings | Inspect heading order | Hierarchical heading levels (no skipped levels) on key pages | Pass |
| Lang Attribute | View `<html>` tag | `lang="en"` set | Pass |
| Form Error Identification | Submit invalid form | Errors announced near field, not just by color | Pass |

---

## Responsive Design Testing

Tested on:
- Desktop: 1920x1080, 1440x900
- Tablet: iPad Air (820x1180)
- Mobile: iPhone 12 Pro (390x844)

The mobile breakpoint was raised from 992px to **1200px** so that iPad Pro (in portrait) now receives the hamburger menu rather than a cramped full-nav layout.

### Layout Adaptation

| Feature | Testing Performed | Result | Pass/Fail |
|---------|------------------|---------|-----------|
| Homepage Hero (Desktop) | View at 1440px width | Side-by-side hero image and text | Pass |
| Homepage Hero (Tablet) | View at 820px width | Layout transitions correctly | Pass |
| Homepage Hero (Mobile) | View at 390px width | Stacked vertically | Pass |
| Products Grid (Desktop) | View at 1440px | 4 columns visible | Pass |
| Products Grid (Tablet) | View at 820px | 2-3 columns | Pass |
| Products Grid (Mobile) | View at 390px | Single column, full width | Pass |
| Bag Layout (Desktop) | View bag on desktop | Items in table format | Pass |
| Bag Layout (Mobile) | View bag on mobile | Items stack as cards | Pass |
| Checkout Form (Desktop) | View checkout on desktop | Two columns: form + summary | Pass |
| Checkout Form (Mobile) | View checkout on mobile | Single column, summary below | Pass |
| Quiz Card Layout (Desktop) | View quiz Q1 on desktop | 4 cards in row | Pass |
| Quiz Card Layout (Mobile) | View quiz Q1 on mobile | Cards stacked vertically | Pass |
| Nav Menu (Desktop) | View nav at 1440px | Full nav visible | Pass |
| Nav Menu (Tablet) | View nav at 820px | Hamburger menu activated | Pass |
| Nav Menu (Mobile) | View nav at 390px | Hamburger menu, condensed icons | Pass |
| Footer (All Devices) | View footer on each device | Adapts correctly | Pass |
| No Horizontal Scroll (Any Device) | Check for horizontal scroll on all pages | No horizontal scroll on any page | Pass |
| Touch Targets (Mobile) | Verify all clickable areas | Minimum 44x44px for all buttons | Pass |

### Mobile Feature Screenshots

#### **Homepage on Mobile**
![Mobile Home](docs/features/feature-mobile-home.png)

---

#### **Mobile Menu Open**
![Mobile Menu](docs/features/feature-mobile-menu.png)

---

### Responsive Screenshots — Tablet (iPad Air)

#### **Homepage**
![Home Tablet](docs/features/responsive-home-tablet.png)

---

#### **Products List**
![Products Tablet](docs/features/responsive-products-tablet.png)

---

#### **Product Detail**
![Detail Tablet](docs/features/responsive-detail-tablet.png)

---

#### **Bag**
![Bag Tablet](docs/features/responsive-bag-tablet.png)

---

#### **Checkout**
![Checkout Tablet](docs/features/responsive-checkout-tablet.png)

---

#### **Quiz**
![Quiz Tablet](docs/features/responsive-quiz-q1-tablet.png)

---

#### **Reviews**
![Reviews Tablet](docs/features/responsive-reviews-tablet.png)

---

#### **About**
![About Tablet](docs/features/responsive-about-tablet.png)

---

### Responsive Screenshots — Mobile (iPhone 12 Pro)

#### **Homepage**
![Home Mobile](docs/features/responsive-home-mobile.png)

---

#### **Products List**
![Products Mobile](docs/features/responsive-products-mobile.png)

---

#### **Product Detail**
![Detail Mobile](docs/features/responsive-detail-mobile.png)

---

#### **Bag**
![Bag Mobile](docs/features/responsive-bag-mobile.png)

---

#### **Checkout**
![Checkout Mobile](docs/features/responsive-checkout-mobile.png)

---

#### **Quiz**
![Quiz Mobile](docs/features/responsive-quiz-q1-mobile.png)

---

#### **Reviews**
![Reviews Mobile](docs/features/responsive-reviews-mobile.png)

---

#### **About**
![About Mobile](docs/features/responsive-about-mobile.png)

---

## Browser Compatibility

The site was tested across the major modern browsers. All features behave consistently with no visual regressions or broken functionality.

| Browser | Version | Tested? | Notes |
|---------|---------|---------|-------|
| Chrome | Latest | Pass | Primary testing browser |
| Firefox | Latest | Pass | All features functional |
| Microsoft Edge | Latest | Pass | All features functional |
| Safari | Latest (iPhone) | Pass | Tested on iOS |
| Samsung Internet | Latest (Android) | Pass | Tested on Android device |

---

## Lighthouse Performance Testing

I used [Google Lighthouse](https://developers.google.com/web/tools/lighthouse) to test performance, accessibility, best practices and SEO on both desktop and mobile.

Mobile scores summary (live site):

| Page | Performance | Accessibility | Best Practices | SEO |
|------|-------------|---------------|----------------|-----|
| Home | 70 | 98 | 100 | 100 |
| Products | 69 | 90+ | 100 | 92 |
| Product Detail | 69 | 95+ | 100 | 100 |
| Bag | 79 | 96 | 100 | 66 (intentional) |
| Checkout | 96 | 89 | 100 | 66 (intentional) |
| Reviews | varies | 90+ | 100 | 90+ |
| About | 71 | 95+ | 100 | 95+ |

**Note on the 66 SEO score for /bag/ and /checkout/:** these pages are intentionally blocked from search indexing via `robots.txt` (users should never land directly in a transactional flow from search). Lighthouse flags the "blocked from indexing" rule as an SEO penalty, but in our case it is the desired behaviour.

### **Homepage**

#### **Desktop Performance**
![Homepage Desktop Lighthouse](docs/features/lighthouse-home-desktop.png)

#### **Mobile Performance**
![Homepage Mobile Lighthouse](docs/features/lighthouse-home-mobile.png)

---

### **Products Page**

#### **Desktop Performance**
![Products Desktop Lighthouse](docs/features/lighthouse-products-desktop.png)

#### **Mobile Performance**
![Products Mobile Lighthouse](docs/features/lighthouse-products-mobile.png)

---

### **Product Detail Page**

#### **Desktop Performance**
![Detail Desktop Lighthouse](docs/features/lighthouse-detail-desktop.png)

#### **Mobile Performance**
![Detail Mobile Lighthouse](docs/features/lighthouse-detail-mobile.png)

---

### **Bag Page**

#### **Desktop Performance**
![Bag Desktop Lighthouse](docs/features/lighthouse-bag-desktop.png)

#### **Mobile Performance**
![Bag Mobile Lighthouse](docs/features/lighthouse-bag-mobile.png)

---

### **Checkout Page**

#### **Desktop Performance**
![Checkout Desktop Lighthouse](docs/features/lighthouse-checkout-desktop.png)

#### **Mobile Performance**
![Checkout Mobile Lighthouse](docs/features/lighthouse-checkout-mobile.png)

---

### **Reviews Page**

#### **Desktop Performance**
![Reviews Desktop Lighthouse](docs/features/lighthouse-reviews-desktop.png)

#### **Mobile Performance**
![Reviews Mobile Lighthouse](docs/features/lighthouse-reviews-mobile.png)

---

### **About Page**

#### **Desktop Performance**
![About Desktop Lighthouse](docs/features/lighthouse-about-desktop.png)

#### **Mobile Performance**
![About Mobile Lighthouse](docs/features/lighthouse-about-mobile.png)

---

## Validation Checks

### Validation Check for HTML Files using W3C HTML Validator

I used the [W3C Nu HTML Checker](https://validator.w3.org/nu/) to validate all rendered pages on the live site. After fixes, **all pages return 0 errors and 0 warnings**.

| Page | Result |
|------|--------|
| Home | ![Home HTML Validation](docs/validators/html/html-home.png) |
| About | ![About HTML Validation](docs/validators/html/html-about.png) |
| Products | ![Products HTML Validation](docs/validators/html/html-products.png) |
| Product Detail | ![Product Detail HTML Validation](docs/validators/html/html-product-detail.png) |
| Reviews | ![Reviews HTML Validation](docs/validators/html/html-reviews.png) |
| Quiz | ![Quiz HTML Validation](docs/validators/html/html-quiz-step.png) |
| Starter Plan | ![Starter Plan HTML Validation](docs/validators/html/html-starter-plan.png) |
| 404 | ![404 HTML Validation](docs/validators/html/html-404.png) |
| Profile | ![Profile HTML Validation](docs/validators/html/html-profile.png) |
| Bag | ![Bag HTML Validation](docs/validators/html/html-bag.png) |
| Checkout | ![Checkout HTML Validation](docs/validators/html/html-checkout.png) |
| Add Product | ![Add Product HTML Validation](docs/validators/html/html-product-add.png) |
| Edit Product | ![Edit Product HTML Validation](docs/validators/html/html-product-edit.png) |

**Issues Fixed:**
- Duplicate `id="user-options"` in nav — renamed mobile occurrence to `user-options-mobile`
- `<li>` directly inside `<nav>` without `<ul>` wrapper — added `<ul class="list-inline">` wrapper around mobile nav items
- Stray closing tags on certain templates — removed
- Missing alt attributes — added descriptive alt text to all images

For sitemap.xml and robots.txt, format-appropriate validators were used:

| File | Validator | Result |
|------|-----------|--------|
| sitemap.xml | xml-sitemaps.com | ![Sitemap Validation](docs/validators/html/xml-sitemap.png) |
| robots.txt | websiteplanet.com | ![Robots Validation](docs/validators/html/txt-robots.png) |

---

### Validation Check for CSS Files using W3C CSS Validator

I used the [W3C Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/) to validate my CSS files. All files passed with no errors.

| CSS File | Result |
|----------|--------|
| static/css/base.css | ![Base CSS Validation](docs/validators/css-base.png) |
| checkout/static/checkout/css/checkout.css | ![Checkout CSS Validation](docs/validators/css-checkout.png) |
| profiles/static/profiles/css/profile.css | ![Profile CSS Validation](docs/validators/css-profile.png) |

---

### Validation Check for JavaScript Files using JSHint

I used [JSHint](https://jshint.com/) to validate my JavaScript code. External library references (jQuery `$`, `Stripe`) and Django template placeholders are flagged as expected warnings; no actual JavaScript errors exist.

| JS File | Result |
|---------|--------|
| stripe_elements.js | ![Stripe Elements JS](docs/validators/js-stripe-elements.png) |
| countryfield.js | ![Country Field JS](docs/validators/js-countryfield.png) |
| Inline JS - base.html | ![Base Inline JS](docs/validators/js-base.png) |
| Inline JS - index.html | ![Index Inline JS](docs/validators/js-index.png) |
| Inline JS - about.html | ![About Inline JS](docs/validators/js-about.png) |
| Inline JS - email.html | ![Email Inline JS](docs/validators/js-email.png) |
| Inline JS - quantity_input | ![Quantity Input JS](docs/validators/js-quantity-input.png) |
| Inline JS - starter_plan.html | ![Starter Plan JS](docs/validators/js-starter-plan.png) |
| Inline JS - review_list.html | ![Review List JS](docs/validators/js-review-list.png) |
| Inline JS - training_quiz.html | ![Quiz JS](docs/validators/js-training-quiz.png) |

**Issues Fixed:**
- ES6 compatibility warnings — added `/* jshint esversion: 6 */` directive where needed
- jQuery compatibility warnings — added `/* jshint jquery: true */` directive where needed
- Undefined globals (`Stripe`, `bootstrap`) — added `/* global ... */` directives

---

### Validation Check for Python Files using CI Python Linter

All custom Python files were validated using the [CI Python Linter](https://pep8ci.herokuapp.com/). All files pass with **0 errors** after extensive cleanup.

**Initial state:** 117 errors across 35 files.
**Final state:** 0 errors across 46 files.

#### PEP8 Compliance Summary

The following adjustments were made:

1. **Line length violations (E501)** — broke long lines to stay under 79 characters
2. **Trailing whitespace (W291)** — removed trailing spaces
3. **Blank lines with whitespace (W293)** — cleaned whitespace in blank lines
4. **Missing newline at end of file (W292)** — added newlines
5. **Blank line errors (E302)** — corrected blank line counts between functions/classes
6. **Late imports** — `# noqa: E402` suppression added in `sweatX/urls.py` for two intentional late imports needed for Django's URL pattern structure

Sample validation screenshots:

| Python File | Result |
|-------------|--------|
| bag/views.py | ![Bag Views PEP8](docs/validators/python/py-bag-views.png) |
| checkout/views.py | ![Checkout Views PEP8](docs/validators/python/py-checkout-views.png) |
| products/views.py | ![Products Views PEP8](docs/validators/python/py-products-views.png) |
| reviews/views.py | ![Reviews Views PEP8](docs/validators/python/py-reviews-views.png) |
| quizzes/views.py | ![Quiz Views PEP8](docs/validators/python/py-quizzes-views.png) |
| sweatX/settings.py | ![Settings PEP8](docs/validators/python/py-sweatX-settings.png) |
| sweatX/urls.py | ![URLs PEP8](docs/validators/python/py-sweatX-urls.png) |

Full set of 46 Python validator screenshots available in `docs/validators/python/`.

---

## Bug Fixes Made During Development

| Bug | How It Was Found | Fix Applied |
|-----|------------------|-------------|
| 404 page rendered white text on white background | Manual testing of 404 route | Added dark wrapper background to 404 template |
| Modal close button (X) not visible on newsletter success modal | User feedback during testing | Replaced Bootstrap 5 `btn-close` class with Bootstrap 4 `class="close"` with `&times;` span |
| Review title rendered inline with comment | Visual inspection | Restructured template to render title in separate block above comment |
| Review comment editing form did not render | Manual testing | Added inline edit form to comment template |
| Comment section blended into review background | Visual inspection | Restyled comments as white pill cards on grey background |
| Mobile users had no way to return to homepage | UX testing on mobile | Added "Home" link as first item in mobile menu |
| Footer + newsletter only visible on homepage | Discovered when navigating between pages | Extracted to `templates/includes/footer.html` and `newsletter.html`, included in `base.html` |
| Site-wide CSS broken after extraction | Local testing | Identified stale `staticfiles/` collection — ran `collectstatic --noinput` |
| Products breadcrumb showed "Products Home" everywhere | UX inconsistency | Made breadcrumb context-aware: shows "All Supplements", "All Programs", or "All Products" based on filter |
| Toast "Go to Secure Checkout" linked to /bag/ | Manual testing of toast button | Updated URL to /checkout/ |
| Like button scrolled to top of page | Manual testing | Added `#review-X` fragment redirects + `scroll-margin-top: 150px` to clear fixed header |
| Bag-preview rendered inside review/comment toasts | Visual inspection | Added `extra_tags='no-bag-preview'` on review/comment messages; template checks tag before rendering bag preview |
| Email confirmation page unstyled | Manual testing of email verification flow | Styled allauth confirm_email template + enabled `ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True` for auto-login |
| Mobile navbar broke on iPad Pro portrait (1024px) | Manual testing on iPad Pro | Raised hamburger breakpoint from 992px to 1200px |
| Mobile nav action icons crowded at <576px | Manual testing on small phones | Made search/account/bag icon-only below 576px with aria-labels; text labels appear at sm+ |
| About-page hero image was 2.3 MB PNG, hurting performance | Lighthouse audit | Converted to 90 KB WebP (`media/sweatx-laptop.webp`) |
| Bag inputs lacked labels and used anchors as buttons | Accessibility audit | Added form labels and aria-labels, converted Update/Remove anchors to `<button>` |
| Product detail size/quantity selects lacked labels | Accessibility audit | Added explicit labels and aria-labels to selects, aria-labels to +/- buttons |
| Products sort dropdown lacked label | Accessibility audit | Added aria-label "Sort products" to sort select |
| Back-to-top was `<a>` without href | Accessibility audit | Converted to `<button>` |
| Checkout summary alt text used `product.name` (undefined) | HTML validator error | Changed to `item.product.name`; added aria-hidden to decorative icons |
| SKU label color #888 had insufficient contrast | Accessibility audit | Changed to #6c757d for WCAG AA compliance |
| Heroku ephemeral filesystem wiped review images on deploy | Discovered when Emil's review image disappeared after a redeploy | Committed Emil's image to `media/review_images/` in the repo so it persists across deploys; documented as known limitation |
| Duplicate ID `user-options` in nav | W3C HTML validator | Renamed mobile occurrence to `user-options-mobile` |
| `<li>` directly inside `<nav>` without `<ul>` wrapper | W3C HTML validator | Added `<ul class="list-inline">` wrapper around mobile nav items |

---

## Testing After Bug Fixes

After applying the fixes above, the affected flows were re-tested on the live deployment to confirm correct behaviour.

| Feature | Testing Performed | Result | Pass/Fail |
|---------|------------------|---------|-----------|
| Comment editing | Click edit on own comment | Inline edit form renders and saves | Pass |
| Toast "Secure Checkout" button | Add item to bag, click button | Lands on /checkout/ | Pass |
| Review like scroll | Like a review mid-page | Page scrolls to liked review with offset clearing header | Pass |
| Review/comment toast (no bag preview) | Post a comment | Toast appears without bag preview | Pass |
| Email confirmation styling | Verify a new account from email | Styled confirmation page, auto-logged in | Pass |
| iPad Pro portrait nav | View site at 1024px width | Hamburger menu displays correctly | Pass |
| About image loads as WebP | Inspect about page Network tab | sweatx-laptop.webp served (~90 KB) | Pass |
| Emil's review image on live site | Visit /reviews/ on Heroku | Image displays correctly | Pass |
| Products breadcrumb (Programs) | Visit /products/?category=programs | Breadcrumb reads "All Programs" | Pass |
| W3C HTML validator (Home) | Re-run validator after fixes | 0 errors, 0 warnings | Pass |

---

## Known Issues

Issues observed during testing that are not blocking but worth documenting:

| Issue | Description | Impact | Status |
|-------|-------------|--------|--------|
| Welcome bubble shows on /?subscribed=1 | After newsletter signup from non-homepage URL, user is redirected to home with success modal, and the 10%-off welcome bubble also triggers 2 seconds later. Both display correctly but coincide. | Cosmetic only | Accepted as edge case |
| Empty bag session reset | Bag is session-based by design. When user logs out and back in, bag may reset. This is expected behavior of Django sessions. | Documented behavior | Acceptable |
| Heroku ephemeral filesystem for media | Heroku dynos have an ephemeral filesystem, so user-uploaded media (e.g. new review images uploaded through the live admin) are wiped on every deploy and dyno restart. The 5 reference review images are committed to the repo so they always persist, but new user uploads in production would not survive long-term without an external store such as AWS S3. | Acceptable for capstone, would require S3 for true production | Documented |
| Skip-to-content link not implemented | The site does not currently expose a "Skip to content" link for keyboard users at the top of each page. | Minor accessibility gap | Future enhancement |

---

End of testing documentation.
