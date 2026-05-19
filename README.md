# sweatX

![sweatX](docs/features/feature-home-hero.png)

**Live site:** [https://sweatx-5364775215dc.herokuapp.com/](https://sweatx-5364775215dc.herokuapp.com/)
**GitHub repository:** [https://github.com/Naida1710/sweatX](https://github.com/Naida1710/sweatX)
**GitHub project board:** [sweatX Development](https://github.com/users/Naida1710/projects/12)

sweatX is a full-stack e-commerce platform built for fitness consumers who want clean supplements and structured training programs in one place — without the noise of mass-market fitness sites. It pairs an 18-product catalogue (pre-workout, protein, creatine, recovery stacks, training programs) with a personalised 15-question training quiz that recommends the right program based on the user's actual goals, and a community feed where members can post reviews, comment, and motivate each other.

The project is my Code Institute Full Stack Diploma e-commerce capstone. It was built from scratch on top of the Boutique Ado walkthrough, with the apps, models, frontend and content fully customised for the fitness use case.

---

## CONTENTS

* [Project Goals](#project-goals)
* [Target Audience](#target-audience)
* [Business Model](#business-model)
* [Marketing Strategy](#marketing-strategy)
* [User Stories](#user-stories)
* [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Typography](#typography)
  * [Wireframes](#wireframes)
  * [Database Schema](#database-schema)
* [Features Overview](#features-overview)
* [Testing](#testing)
* [Technologies Used](#technologies-used)
* [Installation & Setup](#installation--setup)
* [Deployment](#deployment)
* [Known Limitations](#known-limitations)
* [Credits](#credits)
* [Acknowledgements](#acknowledgements)

---

## Project Goals

**sweatX** is built for people who actually train. The fitness e-commerce space is crowded with sites that either sell supplements without context, or sell programs without products, and rarely connect the two. As someone who has used both kinds of sites for years, I wanted to build something that does both — and that respects the user's time.

The site has three goals:

* ✅ **Make the right product easy to find.** Filter by category, sort by price, rating, or name. Programs and supplements live under clear, separate navigation.
* ✅ **Help the user pick a program with confidence.** The 15-question training quiz takes about two minutes and returns one of three structured programs (Beginner Home Workout, 12-Week Strength, Marathon Training 16 Weeks) based on actual answers — not a guess.
* ✅ **Build a community around honest feedback.** Logged-in members can post reviews with optional images, edit them, comment on each other's posts, and like both reviews and comments. The feed feels alive rather than transactional.

Beyond those, secondary goals include:

* ✅ Reward members with a 10% automatic discount and a 7-step starter plan unlocked through newsletter signup
* ✅ Keep checkout friction low — free delivery above $50, saved delivery info for logged-in users, and Stripe-powered card payments with proper webhook handling
* ✅ Meet professional standards on accessibility, SEO and code quality so the site holds up under real-world conditions

---

## Target Audience

The primary audience is fitness-engaged consumers aged roughly 20–45 who:

* Already train regularly but are unsure which supplements actually help their goals
* Want a structured training plan but don't know which one fits where they are now
* Read reviews before they buy and trust other users more than marketing copy
* Shop primarily on mobile

Secondary audiences include:

* Beginners just getting started, who need the quiz and the 7-step starter plan more than the product catalogue
* More advanced lifters and runners who come for specific stacks and pre-workouts and stay for the community feed

---

## Business Model

sweatX is a **B2C (business-to-consumer)** e-commerce platform. Customers buy supplements and training programs directly for personal use. There is no subscription tier in the current version — every order is a one-off transaction handled through Stripe.

### Revenue Streams

1. **Direct product sales** — supplements and training programs sold through the cart and Stripe checkout. This is the main revenue line.
2. **Member retention loop** — a 10% discount is automatically applied to logged-in users' bags. The discount is positioned as a sign-up incentive on the home page welcome bubble. The expected effect is higher account-creation rates, which gives sweatX better data about returning customers and creates an email channel that doesn't depend on paid acquisition.
3. **Newsletter funnel** — the 7-step starter plan is gated behind newsletter signup. New leads enter at the top of the funnel via free educational content and are nurtured into product purchases.

### Secondary B2B Opportunity

A natural future extension is **B2B sales to gyms and personal trainers** — bulk supplement orders, branded stacks for studios, and licensing of the training programs as digital content gym clients can follow at home. This is out of scope for the current build but the data model (Order, OrderLineItem, Product) supports it without rework — only the pricing tiers and an additional customer-type field would need adding.

### Core Business Intents

* Position sweatX as the **practical alternative** to noisy mass-market fitness retail — clean catalogue, real reviews, honest recommendations from the quiz
* Convert first-time visitors into **registered members** through the 10% discount and starter plan
* Convert members into **repeat customers** through the community feed (users who comment and like other reviews tend to come back more often than passive readers)

---

## Marketing Strategy

The marketing approach is built around organic discovery and member retention rather than paid ads.

### 1. Search Engine Optimisation (SEO)

A full SEO setup is implemented on the deployed site:

* **`robots.txt`** — served at `/robots.txt`, instructs crawlers to index public pages and block `/bag/`, `/checkout/`, `/profile/` and other transactional or private URLs that have no value in search results.
* **`sitemap.xml`** — generated dynamically with all public URLs (home, about, products, product detail, reviews, quiz, starter plan, 404), served at `/sitemap.xml`.
* **Descriptive meta tags** — every public page has a unique `<title>`, `<meta name="description">` and `<meta name="keywords">` aimed at long-tail keywords like "fitness training quiz", "pre-workout for beginners" and "marathon training program online".
* **`rel` attributes** — all external links (social media in the footer) use `rel="noopener noreferrer"` and `target="_blank"`.
* **Open Graph tags** — for previews when sweatX URLs are shared on Facebook, Instagram and other social platforms.
* **Custom 404 page** — keeps users on the site with clear "Back to Home" and "Shop Now" CTAs instead of bouncing.

### 2. Facebook Business Page (Mockup)

A bespoke Facebook business page mockup has been created for sweatX, showing the brand presence, cover image, bio, and a sample post. This is the channel where new program drops, community wins, and supplement guides would be published in a live launch.

![sweatX Facebook page mockup](docs/facebook/facebook-page.png)

### 3. Newsletter Signup

Every page on sweatX has a newsletter signup form in the footer ("Get your free 7-step starter plan"). The form is implemented as a custom Django model (`NewsletterSubscriber`), decoupled from the User model so guests can subscribe without creating an account first.

On submission:

* **Logged-in subscribers** see a modal: "Your free 7-step starter plan is ready" with a "View my starter plan" CTA
* **Guest subscribers** see a modal: "Your starter plan is almost ready" with a "Create my account" CTA, plus a softer "Or skip and view the plan anyway" link

This funnel turns SEO/social traffic into recurring email contact and gives sweatX a captured audience even if a visitor doesn't buy on the first visit.

### 4. Member Discount as a Retention Loop

The 10% member discount appears on the homepage in a delayed welcome bubble ("10% OFF EVERY ORDER" with a "Become a member" CTA), in the bag totals (clearly labelled as the member discount line), and as a soft prompt at checkout. The discount is automatic — there's no code to enter — which removes a known drop-off point at checkout.

### 5. Community Feed as Social Proof

The reviews page is a marketing asset in its own right. Five community reviews with names, ratings, comments, and one with an uploaded image are visible to any visitor — they don't have to log in to read social proof. Logged-in users can post their own, which keeps the feed fresh without sweatX having to manually seed content.

---

## User Stories

User stories are tracked as **GitHub Issues** and visualised on the project's **Kanban board**. Each story has its own issue with acceptance criteria, MoSCoW prioritisation (Must Have / Should Have / Could Have), and a Done state. All 15 stories were closed by the end of development.

* **Project board:** [sweatX Development on GitHub](https://github.com/users/Naida1710/projects/12)
* **Closed issues:** [GitHub Issues — closed](https://github.com/Naida1710/sweatX/issues?q=is%3Aissue+is%3Aclosed)

### Epics

User stories are grouped into the following epics:

| Epic | Description |
| :--- | :---------- |
| **E1: Navigation & Discovery** | Help users find products and programs quickly through clear navigation, search and category filtering |
| **E2: Authentication & Account** | Register, verify by email, log in, log out, reset password, manage profile |
| **E3: Product Catalogue** | Browse, filter, sort and search the 18-product catalogue across supplements and training programs |
| **E4: Shopping Bag & Checkout** | Add to bag, adjust quantities, apply member discount, pay with Stripe, receive confirmation email |
| **E5: Quiz & Personalisation** | Take the 15-question training quiz and receive a tailored program recommendation |
| **E6: Community & Reviews** | Read, write, edit, delete reviews; comment on and like reviews and comments |
| **E7: Marketing & Retention** | Newsletter signup, 7-step starter plan, 10% member discount, custom 404 |
| **E8: Superuser Product Management** | Front-end CRUD for products without using the Django admin |

### Core User Stories (sample)

| Story ID | As a/an | I want to be able to... | So that... |
| :--- | :--- | :--- | :--- |
| #1 | shopper | browse all products | I can discover what sweatX offers |
| #2 | shopper | view product details | I can decide whether to buy |
| #3 | shopper | add products to my bag | I can collect items before checkout |
| #4 | shopper | pay securely via Stripe | I receive my products |
| #5 | user | create an account and log in | I can save preferences and order history |
| #6 | user | take a training quiz | I can find the right program for my goals |
| #7 | community member | post a review with rating and image | I can share my honest experience |
| #8 | community member | comment on and like reviews | I can engage with other members |
| #9 | subscriber | sign up for the newsletter | I receive the free 7-step starter plan |
| #10 | logged-in user | get an automatic 10% discount | I'm rewarded for being a member |
| #11 | superuser | add, edit and delete products from the front end | I can manage the catalogue without the Django admin |
| #12 | visitor | land on a friendly 404 page if a URL is wrong | I can find my way back without bouncing |

Each story on the project board has a more detailed acceptance criteria list. The full set is visible on the [public project board](https://github.com/users/Naida1710/projects/12).

### Agile Methodology

Development followed an Agile, iterative approach:

* Every feature started as a GitHub Issue with acceptance criteria
* Issues were prioritised using MoSCoW labels (`must-have`, `should-have`, `could-have`)
* The Kanban board had four columns: Backlog → Todo → In Progress → Done
* Issues were moved across the board as work progressed and closed when the acceptance criteria were met
* Commit messages reference the work being done in plain language so the audit trail is easy to follow

---

## Design

### Colour Scheme

The sweatX palette is built around a bold pink-to-magenta gradient set against deep black backgrounds. The pink reads as energetic and modern without being childish, and the black gives the catalogue and program pages a premium, gym-floor feel.

![sweatX Colour Palette](docs/colour-palette.png)

| Colour | Hex | Use |
| :--- | :--- | :--- |
| Hot Pink | `#F527A9` | Primary brand colour, CTAs, gradients, link hover states |
| Light Pink | `#FF79C6` | Secondary brand colour, gradient endpoint, hover effects |
| Deep Black | `#000000` | Page backgrounds, hero sections, the quiz result page |
| Off-Black Navy | `#0D111A` | Footer gradient start, transitional sections |
| White | `#FFFFFF` | Body text on dark, card backgrounds, primary surface colour |

Supporting greys (`#6C757D` for secondary text, `#222` for dark surfaces) are used sparingly to maintain WCAG AA contrast.

### Typography

The site uses **Bootstrap's default font stack** combined with Font Awesome iconography. Headings use a heavier weight to anchor each section, body text uses a comfortable size for reading on mobile, and the brand wordmark "SWEATX" uses uppercase letter-spacing to feel sport-brand confident.

* **Body & UI** — system font stack via Bootstrap (`-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, ...`) for fast loading and native feel on every device
* **Icons** — Font Awesome 6 for navigation, social, action and feedback icons

### Wireframes

Wireframes were drawn in Balsamiq before any code was written, to lock in layout and information hierarchy before styling. The intention was always for the desktop and mobile experiences to feel like the same site rather than two different products — the wireframes show the shared structure.

* **Home**
  ![Home Wireframe](docs/wireframes/home-wireframe.png)

* **Products**
  ![Products Wireframe](docs/wireframes/products-wireframe.png)

* **Product Detail**
  ![Product Detail Wireframe](docs/wireframes/product-detail-wireframe.png)

* **Bag**
  ![Bag Wireframe](docs/wireframes/bag-wireframe.png)

* **Checkout**
  ![Checkout Wireframe](docs/wireframes/checkout-wireframe.png)

* **Quiz**
  ![Quiz Wireframe](docs/wireframes/quiz-wireframe.png)

* **Reviews**
  ![Reviews Wireframe](docs/wireframes/reviews-wireframe.png)

* **About**
  ![About Wireframe](docs/wireframes/about-wireframe.png)

* **Profile**
  ![Profile Wireframe](docs/wireframes/profile-wireframe.png)

### Database Schema

sweatX uses a relational database (PostgreSQL on Heroku, SQLite locally) with Django's built-in User model as the central authentication entity. The full ERD is below.

![sweatX ERD](docs/erd.png)

**Core Relationships:**

* **User ↔ UserProfile (1:1)** — each registered user has exactly one profile holding default delivery info and order history
* **User ↔ Order (1:Many)** — each user can place multiple orders over time
* **Order ↔ OrderLineItem (1:Many)** — each order contains one or more line items, each linking to a Product
* **User ↔ Review (1:Many)** — each user can post multiple reviews
* **Review ↔ Comment (1:Many)** — each review can have multiple comments
* **User ↔ Comment (1:Many)** — each user can post multiple comments across reviews
* **User ↔ QuizSubmission (1:Many)** — each user can take the quiz multiple times to update their recommendation
* **NewsletterSubscriber** — standalone, not linked to User (so guests can subscribe without an account)

**Custom Models (beyond Boutique Ado):**

To meet the "at least 3 custom models" requirement, sweatX adds the following on top of the walkthrough's Product / Category / Order baseline:

| Model | Purpose |
| :--- | :--- |
| **Review** | Community review with title, rating (1-5), comment, optional image, author FK, timestamps. Drives the entire reviews page and feed. |
| **Comment** | Threaded comment attached to a Review, with author FK and timestamp. Supports the community discussion feature. |
| **NewsletterSubscriber** | Email signup decoupled from User. Powers the newsletter funnel and gates the 7-step starter plan. |
| **QuizSubmission** | Stores quiz answers and the recommended program for each user, with timestamps. Drives personalised home headlines and the quiz result page. |
| **StarterPlanProgress** | Tracks which of the 7 starter plan steps a user has marked complete. Per-user persistence. |
| **UserProfile** | Extended Boutique Ado model — adds default delivery info fields and links to the user's order history. |

That is six custom or substantially-customised models, well above the three required.

---

## Features Overview

### Shared across every page

* **Responsive navbar** — full nav on desktop, hamburger menu on tablet and mobile (breakpoint 1200px so iPad Pro portrait also gets the hamburger). Includes search, user account dropdown, and bag total.
  ![Home Hero](docs/features/feature-home-hero.png)

* **Free delivery banner** — pink shimmer banner below the nav reminds users of the $50 free-delivery threshold on every page.

* **Footer with newsletter signup** — present on every page, captures email at the top of the funnel.
  ![Newsletter Footer](docs/features/feature-newsletter-footer.png)

* **Toast messages** — success, error and info toasts top-right with auto-hide and a manual close. Bag-success toasts include a mini bag preview; review/comment toasts opt out of the preview using a custom template tag.
  ![Toast Success — Bag](docs/features/feature-toast-success-bag.png)
  ![Toast Success — Comment](docs/features/feature-toast-success-comment.png)

* **Welcome bubble** — logged-out users see a 10% OFF bubble appear after two seconds on the homepage. Closes for the session when dismissed.

### Homepage

* **Hero section** with dual CTAs ("Discover my plan" → quiz, "Buy supplements" → catalogue) and a phone-mockup hero image
  ![Home Hero](docs/features/feature-home-hero.png)

* **Value section** — "Fuel your training" and "Train with intention" panels that explain the brand promise
  ![Home Values](docs/features/feature-home-values.png)

* **Dynamic personalised content** — if the user has completed the quiz, the homepage swaps in goal-specific copy on return visits

### About Page

* **Brand story** — who sweatX is for and why it exists
* **Performance-optimised hero image** — converted from 2.3 MB PNG to 90 KB WebP for fast mobile load
  ![About](docs/features/feature-about.png)

### Products

* **Catalogue grid** — all 18 products visible by default, filterable by category pill (Pre-Workout, Protein, Creatine, Recovery, Stacks, Deals, Programs)
  ![Products List](docs/features/feature-products-list.png)

* **Sortable** — by price (asc/desc), rating (asc/desc), name (A–Z) and category
  ![Products Sort](docs/features/feature-products-sort.png)

* **Context-aware breadcrumbs** — viewing `?category=PROTEIN` shows "All Supplements" as parent; viewing `?category=programs` shows "All Programs"

* **Search** — header search filters products by name/description and shows a count

* **Product detail page** — large image, full description, rating stars, price, quantity stepper (with min 1, max 99), size selector where applicable, and Add to Bag
  ![Product Detail](docs/features/feature-product-detail.png)

### Shopping Bag

* **Itemised bag** with editable quantities, remove buttons (proper `<button>` elements, not anchors), live subtotal, member discount line for logged-in users, delivery cost (or "$X more for free delivery" reminder), and a grand total
  ![Bag](docs/features/feature-bag.png)

* **Persistent across pages** — items stay in the bag as the user browses
* **Session-based** by Django design — documented in TESTING.md as expected behaviour

### Checkout

* **Two-column layout** — delivery form on the left, order summary on the right
  ![Checkout](docs/features/feature-checkout.png)

* **Pre-filled email** for logged-in users
* **Save delivery info** checkbox for logged-in users (writes to their profile)
* **Country dropdown** via `django-countries` with all countries alphabetised
* **Stripe card element** with real-time validation (invalid number, past expiry, declined card, insufficient funds — all handled)
* **Loading overlay** ("Processing payment...") while Stripe is being called
* **Webhook handler** confirms the order even if the user closes the browser before redirect

### Order Confirmation

* Success page with order number, itemised order, totals, and a confirmation email sent to the user

### Profile

* **Default delivery info form** — pre-filled, editable
* **Order history** — past orders listed with clickable order numbers that open the original order detail
  ![Profile](docs/features/feature-profile.png)

### Quiz

* **15-question training quiz** with three layouts (grid, list, image-question) and a progress bar
  ![Quiz Question 1](docs/features/feature-quiz-q1.png)

* **Previous/Next** with answer preservation between questions
* **Inline error** on Next-without-selection
* **Result page** recommends one of three programs (Beginner Home Workout Plan, 12-Week Strength Program, Marathon Training 16 Weeks) with a Buy CTA and a "Browse all programs" alternative

### Reviews / Community Feed

* **Public read** — anyone can read the 5 community reviews, ratings, comments and likes without logging in
  ![Reviews](docs/features/feature-reviews.png)

* **Logged-in members** can post, edit and delete their own reviews; image upload optional
* **Comment threads** under each review — comments display as white pill cards on a grey background for visual separation
* **Like reviews and comments** — toggle on/off, persists across sessions, with scroll offset so the page doesn't jump under the fixed header

### Newsletter & Starter Plan

* **Footer signup form** on every page; submission opens a success modal
* **7-step starter plan** at `/starter-plan/` — each step has a "Mark complete" toggle that persists per logged-in user
  ![Starter Plan](docs/features/feature-starter-plan.png)

### Authentication

* **django-allauth** with email verification required for new accounts
* **Auto-login** on email confirmation via `ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True`
* Password reset flow, remember-me, login redirect to homepage
  ![Login](docs/features/feature-login.png)
  ![Signup](docs/features/feature-signup.png)
  ![Logout](docs/features/feature-logout.png)

### Superuser Product Management (Front-End CRUD)

This is the front-end CRUD form required by the assignment — no Django admin needed.

* **Add Product** — superuser-only, full form with category, SKU, name, description, price, rating and image upload
  ![Add Product](docs/features/feature-product-add.png)

* **Edit Product** — pre-filled form, image-change preview
  ![Edit Product](docs/features/feature-product-edit.png)

* **Delete Product** — with confirmation prompt
* **Non-superuser protection** — direct URLs (`/products/add/`, `/products/edit/<id>/`, `/products/delete/<id>/`) all show an error toast and redirect to the home page

### Custom 404

* Dark hero with sweatX branding, large translucent "404" watermark, and Back to Home / Shop Now CTAs
  ![404](docs/features/feature-404.png)

### Defensive Design

Authentication and authorisation are enforced both at the view level and at the URL level:

* `@login_required` decorator on all user-only views (profile, post review, post comment, like, edit/delete own content)
* `@user_passes_test(lambda u: u.is_superuser)` on all product-management views
* User-scoped querysets (`Review.objects.filter(user=request.user)` for edit/delete) so users cannot operate on other users' content even by guessing URLs
* CSRF protection on every form via Django's built-in middleware
* All forms validate required fields on the client (browser validation) and on the server (Django form validation)
* Stripe handles all card data — sweatX never sees a full card number; PCI scope is minimised
* Secret keys, Stripe keys, database URL and email password are all in environment variables (`env.py` locally, Heroku Config Vars in production) and are never committed to the repo

---

## Testing

Manual testing was performed against the deployed application across desktop, tablet (iPad Air) and mobile (iPhone 12 Pro) viewports. Tests cover authentication, navigation, e-commerce flow, custom features, responsive design, accessibility, validation and performance.

For the **full test write-up**, see [TESTING.md](TESTING.md). It includes:

* Around 250 individual test cases across 20 sections, each with feature / steps / result / pass-fail
* W3C HTML validation screenshots for every public page (0 errors, 0 warnings)
* W3C CSS Jigsaw validator results for all CSS files
* JSHint results for all JavaScript files
* CI Python Linter results for all 46 Python files (0 errors, down from 117)
* Lighthouse desktop + mobile screenshots for Home, Products, Product Detail, Bag, Checkout, Reviews and About
* Accessibility testing section
* Bug fixes made during development with how each was found and fixed
* Known issues that are accepted edge cases

### Lighthouse Summary (Live, Mobile)

| Page | Performance | Accessibility | Best Practices | SEO |
|------|-------------|---------------|----------------|-----|
| Home | 70 | 98 | 100 | 100 |
| Products | 69 | 90+ | 100 | 92 |
| Product Detail | 69 | 95+ | 100 | 100 |
| Bag | 79 | 96 | 100 | 66 (intentional) |
| Checkout | 96 | 89 | 100 | 66 (intentional) |
| Reviews | varies | 90+ | 100 | 90+ |
| About | 71 | 95+ | 100 | 95+ |

The 66 SEO score on `/bag/` and `/checkout/` is intentional — those URLs are blocked from indexing via `robots.txt`.

---

## Technologies Used

### Backend

* **Python 3.12** — programming language
* **Django 6.0.2** — web framework
* **PostgreSQL** (Heroku-managed in production) and **SQLite** (local development) — relational databases
* **django-allauth 0.50.0** — authentication, email verification, password reset
* **django-crispy-forms 1.14.0** — form rendering
* **django-countries 7.6.1** — country dropdown on the checkout form
* **Stripe 14.1.0** — card payments and webhooks (test mode)
* **Gunicorn 25.3.0** — WSGI server in production
* **WhiteNoise 6.12.0** — static file serving
* **Pillow 11.0.0** — image handling for review and product image uploads

### Frontend

* **HTML5** — semantic markup
* **CSS3** — custom styles in `static/css/base.css` and per-app stylesheets
* **JavaScript (ES6)** — vanilla JS plus jQuery for legacy compatibility with Boutique Ado patterns
* **Bootstrap 4.6** — responsive grid, components, utilities
* **Font Awesome 6** — iconography

### External Services and Tools

* **Heroku** — production hosting
* **Stripe** — payments (test mode for capstone)
* **Gmail SMTP** — transactional email (allauth verification, password reset, order confirmation) via Gmail app password
* **GitHub** — version control, Issues, project board

### Development Tools

* **VS Code** — code editor
* **Git** — version control
* **CI Python Linter** ([pep8ci.herokuapp.com](https://pep8ci.herokuapp.com/)) — PEP8 compliance
* **JSHint** — JavaScript validation
* **W3C HTML Validator** and **W3C CSS Jigsaw** — markup and stylesheet validation
* **Google Lighthouse** — performance, accessibility, best practices and SEO audits
* **Balsamiq** — wireframing
* **Coolors** — colour palette generation

---

## Installation & Setup

### Prerequisites

* Python 3.12
* Git
* A GitHub account
* (Production only) A Heroku account, a Stripe account, and a Gmail account with an app password for SMTP

### Local Development Setup

1. **Fork and clone the repository**

   * Fork [https://github.com/Naida1710/sweatX](https://github.com/Naida1710/sweatX) on GitHub
   * Open VS Code, press `Ctrl+Shift+P`, type "Git: Clone" and paste your forked URL
   * Choose a local folder and let VS Code open the project

2. **Create and activate a virtual environment**

   * In the VS Code terminal: `python -m venv .venv`
   * Activate it:
     * Windows: `.venv\Scripts\activate`
     * macOS/Linux: `source .venv/bin/activate`
   * The terminal prompt should now start with `(.venv)`

3. **Install dependencies**

   ```
   pip install -r requirements.txt
   ```

4. **Create your environment variables**

   Create a file called `env.py` in the project root (it is already in `.gitignore`, so it will not be committed):

   ```python
   import os

   os.environ.setdefault("SECRET_KEY", "<your-django-secret-key>")
   os.environ.setdefault("DEBUG", "True")
   os.environ.setdefault("DATABASE_URL", "<your-database-url-or-leave-blank-for-sqlite>")
   os.environ.setdefault("STRIPE_PUBLIC_KEY", "<your-stripe-test-pk>")
   os.environ.setdefault("STRIPE_SECRET_KEY", "<your-stripe-test-sk>")
   os.environ.setdefault("STRIPE_WH_SECRET", "<your-stripe-webhook-secret>")
   os.environ.setdefault("EMAIL_HOST_USER", "<your-gmail-address>")
   os.environ.setdefault("EMAIL_HOST_PASS", "<your-gmail-app-password>")
   ```

5. **Run database migrations**

   ```
   python manage.py migrate
   ```

6. **Create a superuser** (for access to `/products/add/`, `/edit/`, `/delete/` and Django admin)

   ```
   python manage.py createsuperuser
   ```

7. **Collect static files**

   ```
   python manage.py collectstatic --noinput
   ```

8. **Run the development server**

   ```
   python manage.py runserver
   ```

   Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser. The site should load.

---

## Deployment

The live site is deployed on Heroku from the `feature/complete-project` branch.

### 1. Prepare for Deployment

* Confirm `requirements.txt` is up to date: `pip freeze > requirements.txt`
* Confirm `Procfile` exists in the project root and contains: `web: gunicorn sweatX.wsgi`
* Confirm `runtime.txt` exists and pins the Python version (currently `python-3.12.10`)
* In `sweatX/settings.py`:
  * `ALLOWED_HOSTS = ["sweatx-5364775215dc.herokuapp.com", "localhost", "127.0.0.1"]`
  * `CSRF_TRUSTED_ORIGINS = ["https://*.herokuapp.com"]`
  * `DEBUG = "DEVELOPMENT" in os.environ` (so it's False in production)

### 2. Heroku App Setup

* Create a Heroku account at [heroku.com](https://www.heroku.com/) and verify your email
* From the Heroku dashboard, click **New** → **Create new app**
* Give it a unique app name and choose Europe as the region
* Click **Create app**

### 3. Provision the Database

* In your new Heroku app, go to **Resources**
* Search for **Heroku Postgres** and provision the free tier (or paid Essentials)
* Heroku will automatically add a `DATABASE_URL` config var

### 4. Configure Environment Variables

In **Settings** → **Reveal Config Vars**, add:

| Key | Value |
| :--- | :--- |
| `SECRET_KEY` | Your Django secret key (generate a new one for production) |
| `STRIPE_PUBLIC_KEY` | Your Stripe public key (test or live) |
| `STRIPE_SECRET_KEY` | Your Stripe secret key |
| `STRIPE_WH_SECRET` | Your Stripe webhook signing secret |
| `EMAIL_HOST_USER` | Your Gmail address |
| `EMAIL_HOST_PASS` | Your Gmail app password (not your normal password) |
| `DISABLE_COLLECTSTATIC` | `1` for the first deploy only, then remove it |

`DATABASE_URL` is added automatically when you provision Postgres.

### 5. Connect GitHub and Deploy

* In **Deploy** → **Deployment method**, choose **GitHub** and connect your repo
* In **Manual deploy**, select the `feature/complete-project` branch and click **Deploy Branch**
* Heroku will build and release the app. The live URL is shown at the top of the app page.

### 6. Stripe Webhook

* In your Stripe dashboard, go to **Developers** → **Webhooks** → **Add endpoint**
* Endpoint URL: `https://<your-app-name>.herokuapp.com/checkout/wh/`
* Listen for events: `payment_intent.succeeded` and `payment_intent.payment_failed`
* Copy the signing secret into the `STRIPE_WH_SECRET` config var on Heroku

The live deployment for this submission is:
**[https://sweatx-5364775215dc.herokuapp.com/](https://sweatx-5364775215dc.herokuapp.com/)**

---

## Known Limitations

These are accepted limitations of the current build, called out so the assessor can see they're documented rather than missed.

* **Heroku ephemeral filesystem for user-uploaded media** — Heroku dynos have an ephemeral filesystem, so review images uploaded through the live site are wiped on each deploy and dyno restart. The five reference reviews on the live site have their images committed to the repo (`media/review_images/`) so they always persist. In a production launch, sweatX would move user-uploaded media to AWS S3 or Cloudinary.
* **Bag is session-based** — by Django design, logging out and back in resets the bag. This is expected behaviour and is documented in TESTING.md.
* **Welcome bubble overlaps with subscribe-success modal** in the rare case of subscribing from a non-homepage URL. Cosmetic only.
* **Skip-to-content link** is not implemented yet — a small accessibility gap noted for a future iteration.
* **Stripe is in test mode** — appropriate for a capstone submission; switching to live mode is a one-line config change.

---

## Credits

### Content & Inspiration

* Boutique Ado walkthrough by Code Institute — the architectural starting point for the catalogue, bag, checkout and Stripe integration. All apps were customised significantly on top of this base.
* Product copy, quiz questions and review content written from scratch for the sweatX brand.

### Design Resources

* [Coolors](https://coolors.co) — colour palette generation
* [Balsamiq](https://balsamiq.com) — wireframing
* [Canva](https://www.canva.com) — Facebook page mockup, logo concepts
* [Font Awesome](https://fontawesome.com) — iconography
* [Pexels](https://pexels.com) — placeholder product and lifestyle imagery

### Learning Resources

* [Django Documentation](https://www.djangoproject.com/) — official framework documentation
* [Code Institute LMS](https://learn.codeinstitute.net/) — Boutique Ado walkthrough and supporting modules
* [Stripe Documentation](https://stripe.com/docs) — payment integration and webhook handling
* [django-allauth Documentation](https://django-allauth.readthedocs.io/) — authentication setup
* [MDN Web Docs](https://developer.mozilla.org/) — HTML, CSS and JavaScript reference

### Code Validation Tools

* [W3C HTML Validator](https://validator.w3.org/) — HTML validation
* [W3C CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator/) — CSS validation
* [JSHint](https://jshint.com/) — JavaScript validation
* [CI Python Linter](https://pep8ci.herokuapp.com/) — PEP8 compliance
* [Google Lighthouse](https://developers.google.com/web/tools/lighthouse) — performance, accessibility, best practices and SEO

---

## Acknowledgements

* I want to thank my husband for his patience, support and steady encouragement throughout this project — especially during the long evenings near the deadline.
* A special thank-you to my mentor, **Dick Vlaanderen**, for his guidance, his patience with my questions, and for keeping me on track when the scope of this project felt overwhelming.
* Thank you to the Student Support team and tutors at Code Institute for their help on the trickier parts of the Boutique Ado integration and Stripe webhooks.
* And finally, thank you to the small community of fellow students who shared their own struggles and breakthroughs — knowing I wasn't the only one trying to make this work meant a lot.

[Back to Contents](#contents)
