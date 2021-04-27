# WYSPA - Testing Documentation

The Main README documentation can be found under [README.md](README.md)

# Table of contents

> 1.  [User Story Testing](#user-story-testing)
> 2.  [Feature Testing](#feature-testing)
> 3.  [Browser Testing](#browser-testing)
> 4.  [Automated Testing](#automated-testing)
> 5.  [Significant Bugs](#significant-bugs)
> 6.  [Other Technical Difficulties](#other-technical-difficulties)

# User Story Testing

## As a visitor to the website, I want to know what the website does, so that I can decide whether I'm interested in engaging within it.

**Acceptance Criteria:** A user must be able to identify the website's name and understand its purpose on first visit.

**Summary:**

- When the user visits the website, they are presented with a **Logo** containing a self-descriptive name.
- The **Logo** is contained in a persistent **NavBar** across the site, which is positioned centrally at the top of the page, and is therefore familiar and easy to identify.
- When a user first visits the website, they are presented with a website overview, which contains:
  - A **call-to-action** which, while colloquial, is self-descriptive, understandable, and relatable: _"Penny for your thoughts?"_
  - Three **feature callouts**, which contain relevant and supporting imagery, and a description of each feature.
- It is therefore clear, from first visit, the name of the website, what its purpose is, and what the main features are.

**Outcome: Pass**

## As a potential user, I want the usage to be either self-descriptive or the instructions clearly communicated, so that I can interact with the site with ease.

**Acceptance Criteria**: A user should be able to understand how to both navigate and interact with the website and its features, either through design, implementation or through instructions.

**Summary:**

- When a user first visits the website, they are provided with a website overview. This overview explains the website's purpose, lists the primary features of by the website, and provides a succinct explanation of each feature.
  - Each feature's sub-title and supporting image contains a link to the relevant feature.
- The website's **Logo** contains a link which redirects the user to the home page at any given point.
- Each page contains a **help icon** in the upper right corner, which, when interacted with, presents the user with a **Modal** containing page specific guidance. As the content is generated per page, the information presented to the user is relevant to the page they're currently engaged with, so as to ensure only relevant information is provided at any given time.
- The **NavBar** contains links which aid with user navigation:
  - At the largest viewport, users can hover each navigational link with their mouse, producing a highlighting effect. This effect connotes interactivity, allowing users to intuitively understand how to navigate the website.
  - On smaller viewports, the **NavBar** is collapsed into a **SideNav** ; the icon to present the **SideNav** is a universal burger icon, thus identifiable and relatable.
  - On all viewports, a user's active location within website is depicted through alternative styling on the relevant link within the **NavBar**/**SideNav**, allowing a user to know their location at any given time.
- All interactive icons in the site are relevant to their action, so as to communicate intuitive instructions to the user.
  - On larger viewports, these icons are accompanied by tooltips which provide a verbal explanation of each action.
- All collapsible containers contain both a self-descriptive title and a relevant icon.
- All buttons are styled the same across the project, provide visual feedback when hovering and clicking, and contain text which appropriately explains their action.
- The **Map** feature uses **Google Maps**, and as such comes with intuitive navigational control. Users can scroll, click and drag, swipe, or pinch, to navigate the **Map**.
- **Toasts** appear accordingly to instruct, confirm, and inform the user of their interactions, providing feedback as they interact and provide content to the platform.
- The **Register**, **Login**, and **Logout** functionality are visible from all pages, and as they are presented in **Modals**, do not divert the user's attention away from the content. These forms are easy to interact with and provide appropriate feedback when completing.
- The **Wyspa Creation** form is self-explanatory, easy to complete, and provides appropriate feedback when completing.
- It is therefore easy for a user to navigate through the site, and to understand how to interact with its features.

**Outcome: Pass**

## As an unregistered user, I want to be able to view content on the site without having to register, so I can decide whether to make an account.

**Acceptance Criteria:** An unregistered user must be able to see all content posted by other logged in users without making an account.

**Summary:**

- Unregistered users have viewing access to all features across the website.
- Unregistered users can retrieve **Random Wyspas** from the **Wyspa** page. This is achieved by clicking directly on the **Wyspas** link, or by clicking on the **Random Wyspa** icon while on this page.
  - Unregistered users can view the message of a **Wyspa**, along with how many **Listens** it has, and is able to read the **Comments**, if applicable.
  - Unregistered users cannot add **Listens** or **Comments** to a Wyspa. The **Add Comment** field only appears to logged in users, and when attempting to **Listen** to a **Wyspa**, an unregistered user is informed via a **Toast** that they must be logged in to do so.
- Unregistered users can utilise all functionality of the **Map** feature; all features are available, including navigating the **Map**, and interacting with **Wyspas**.
- An unregistered user is therefore capable of viewing all user-contributed content on the site, without having to register or log in.

**Outcome: Pass**

## As an unregistered user, I want to be able to make an account and log in, so that I can benefit from the features of a registered user.

**Acceptance Criteria:** An unregistered user must be able to make an account, log in to their account, sign out of their account.

**Summary:**

- Users can **Register** with the website, **Log in** to access restricted features, **Log out** of their account, and **Delete** their account should they no longer want their details hosted in the database.
- The **Register**, **Login**, and **Logout** functionalities are visible, where applicable, from all pages, within the **NavBar/SideNav**.
- Interacting with the **Register** or **Login** feature presents the user with a slide-up modal; this produces the effect of maintaining a user's location within the site, and avoids navigating them away from content in order for them to access a particular restricted feature.
- The **Register** Modal requests a **username**, a **password**, and a **confirmation password** for registration.
  - Visual feedback is presented to the user when changing fields within the form, in the form of both colour and text; in the event the validation of any given input field is unsuccessful, the appropriate field is highlighted red, and instructional text is presented at the top of the form, clearly communicating which field needs attention.
  - Users cannot submit the form without all forms being validated, so as to present the best user experience when attempting to create an account.
  - If the **username** requested already exists, the user is informed via a **Toast** at the top of the page.
  - If **registration** is successful, the user is automatically logged into their account, and is redirected to their previous location. This provides a natural flow of navigation and interaction with the site.
- The **Log In** modal is of a similar design to the **Register** modal, but without the **password confirmation** field.
  - If **Log In** is unsuccessful, a user is returned to the page they were previously on, and is presented with a **Toast** informing them that the username or password was incorrect.
  - If **Log In** is successful, a welcome **Toast** appears, and the user is redirected to the page they were on, or the page they were trying to access.
- If a user attempts to visit a restricted aspect of the site, and immediately attempts to **register** or **log in**, they will be redirected to their initially requested page on successful **Log In**.
- When logged in, a user can click the **Log Out** button, and the user is logged out and redirected to the index page.
- If a user wishes to **delete** their account, they can access this feature from the **My Voice** section of the site. This feature removes their user account from the database, and all of their respective **Wyspas** from the messages database.
- As such, users can **Register** for an account, **Log in**, or **Log out** of their account from any page, and have the ability to **Delete** their account if they wish to do so.

**Outcome: Pass**

## As a logged in user, I want to be able to make posts anonymously, and engage with other posts anonymously, so that I can express myself or support others without exposing any personal details.

**Acceptance Criteria:** A logged in user must be able to create a Wyspa, comment on other Wyspas, and Listen to other Wyspas.

**Summary:**

- Upon successful **Log In**, users have access to the **My Voice** page. This page provides an overview of all active **Wyspas**, including each **Wyspa's** **message**, **listen** count, **expiry**, and the ability to **navigate** to the respective **Wyspa** Page.
- The **My Voice** section also provides the **Wyspa Creation** feature, which is available within a collapsible container.
- The **Wyspa Creation Form** allows a user to submit a **Wyspa** to the relevant database. All fields are required in order for the form to be submitted.
- Once the form has been submitted, a **Wyspa** is stored in the Database. In the event of the form being successfully submitted, but a with invalid content, the user is informed via a **Toast** which content was invalid and why. When the **Wyspa** submission is successful, a **Toast** is presented to the user to confirm this.
- When a **Wyspa** is submitted, it is accessible via three ways:
  - Via the **My Voice** feature, where a user accesses their own **Wyspas**.
  - Via the **Map** feature, where **Wyspas** are placed based on their specified **location**, in the colour specified by the **mood**, and its size based on how many **listens** it has.
  - Via the **Wyspa** section, if it is part of the **Random Generation** process, or if its respective marker is interacted with on the **Map** feature.
- When on the **Wyspa** page, logged in users can engage with **Wyspas** in the following ways:
  - **Listen** to the **Wyspa**, a form of interaction which directly affects the size of the **Wyspa's** marker on the **Map** feature. This is achieved by clicking on the relevant interactive icon. A user can only **listen** to a **Wyspa** once; any further attempts to do so will result in the user being informed of this via a **Toast**.
  - **Comment** on a **Wyspa**. This allows logged in users to stay in the conversation, support others, help others, or respond to other people's comments.
- All personal data (i.e information linking a **Wyspa** to a **User**) is handled and pre-processed server side. As a result of this, identifiable information cannot be found within any of the rendered HTML, such as **usernames** or **User IDs**.
  - When viewing **Wyspas** via the **Wyspa Page**, authors are not visible, nor are comment authors.
- All location data provided by a user is **scrambled** before being input into the database. Therefore, users cannot be located by the specific location of their **Wyspa** on the **Map**.
- As such, logged in users are capable of making **anonymous Wyspas**, and engage with other **Wyspas** anonymously, without exposing any identifiable information.

**Outcome: Pass**

## As a logged in user, I want to be able to edit or delete content, so that I have control over the content I have stored on the platform.

**Acceptance Criteria:** A logged in user must be able to edit their Wyspa, delete comments on their Wyspas, delete their comments on other users' Wyspas, and delete their account.

**Summary:**

- **Logged in** users can delete their **Wyspas** in one of three ways:
  - From the **My Voice** page, users can request to delete an active **Wyspa** by interacting with the **Delete** Icon within the relevant **Wyspa's** container. A confirmation message will appear which prevents users from accidentally removing content from the database.
  - A user can also **delete** their **account**, and all of their **Wyspas**, from the **My Voice** page. This option is hidden in a self-contained collapsible container at the bottom of the page. A user must expand this container, click the delete account button, and also confirm the account deletion in order to process this request, due to its permanent nature.
  - During **Wyspa Creation** or **Edit**, users must set an **expiry** date and time in the future. This allows a user to set a date in the future in which the **Wyspa** will be automatically be removed from the database; it also allows users to **extend** the life of their **Wyspa** should they wish for it to remain active for longer.
- **Logged in** users can edit their **Wyspas** from the relevant **Wyspa page**.
  - When the logged in user is presented with their own **Wyspa** on this page, an additional **edit** icon is presented to them which takes them to the **Edit Wyspa** page.
  - This page contains a similar form to the **Wyspa Creation** form, prepopulated with the chosen **Wyspa's** details. The only field not pre-populated is the **location** field, due to how the location is **scrambled** on submission.
  - All form validation is identical to that of the **Wyspa Creation** form. The only difference being that when a user successfully edits their **Wyspa**, the **Toast** notification text confirms that the **Wyspa** has been edited successfully.
- **Comments** can be deleted by either the owner of the **Comment** or by the owner of the **Wyspa** which the comment has been added to. If the user is either of these owners, a **delete** icon will appear within the relevant **comment**, allowing the user to **delete** the **comment**. Similar to deleting a **Wyspa**, a confirmation box appears when a user attempts to **delete** a comment.
- As such, logged in users are capable of editing their own **Wyspas**, deleting their **Wyspas** (individually or during account deletion), deleting their account, and removing comments (either their own, or comments on their own Wyspas).

**Outcome: Pass**

## As a user, I want to be able to see a Map of, and individually interact with, all Wyspas so that I can decide what content I see and interact with.

**Acceptance Criteria:** Any user must be able to view and utilise the Map feature, with the ability to navigate to any Wyspa by interacting with them on the Map.

**Summary:**

- All users have access to the **Map** functionality; this is accessed through the **NavBar**/**SideNav**.
- Users can interact with any **Wyspa** on the **Map**, regardless of size, or location.
- Where multiple **Wyspas** are overlayed on the **Map**, testing has been completed to ensure that both all **Wyspas** can be interacted with regardless of size or position.
- Clicking on any **Wyspa** on the **Map** takes the user directly to respective **Wyspa** page, where users can contribute to the post.
- Each **Wyspa's** position is determined by the location provided by the user, but multiple **Wyspas** submitted with the exact same location are placed different on the **Map** so as to ensure anonymity.
  - This allows users to decide where they want to look for Wyspas in the world.
- Each **Wyspa's** colour is determined by the **Mood** of the **Wyspa**, set during **Creation** or **Editing** of the **Wyspa**. The three moods available are `Sad`, `Neutral`, and `Happy`, which are coloured `Red`, `White`, and `Green` accordingly.
  - This allows users to decide what type of **Wyspa** they want to interact with.
- Each **Wyspa's** size is determined by the amount of **listens** it has.
  - This allows users to decide whether to look for the most or least popular **Wyspas** on the **Map**.
- As such, any user is able to utilise the **Map** function in order to choose what messages they want to interact with, based on their location, mood, and popularity.

**Outcome: Pass**

## As a mobile user, I want to be able to utilise all aspects of the site, so that I can interact with the website on the go.

**Acceptance Criteria:** A user should be able to benefit from all features on the website, regardless of viewport.

**Summary:**

- As the website uses **Materialize CSS**, most of the structure natively adapts to a user's viewport, allowing native compatibility on any screen size; all aspects of the site have been designed to be responsive, allowing the appropriate font sizing and spacing on all viewports.
- The **NavBar** collapses into a **SideNav** on medium viewports and down, preventing the **NavBar** from being overcrowded, with the burger icon being distinguishable and easy to interact with.
  - All elements in the **SideNav** are appropriately sized and respond appropriately to touch.
- All **interactive icons** work with touch screen devices, and are large enough to target using touch.
- All **text** is legible on all screen sizes.
- The **Map** functionality natively utilises a touch screen interface.
- All **forms** respond appropriately to on-screen keyboards.
- As such, all website functionality works innately on all screen devices, regardless of viewport.

**Outcome: Pass**

# Feature Testing

# Browser Testing

# Code Validation

# Significant Bugs

# Other Technical Difficulties

---

[Click here](README.md) to return to the main README.md.
