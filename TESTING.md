# WYSPA - Testing Documentation

The Main README documentation can be found under [README.md](README.md)

# Table of contents

> 1.  [User Story Testing](#user-story-testing)
> 2.  [Manual Feature Testing](#manual-feature-testing)
> 3.  [Automated Feature Testing](#automated-feature-testing)
> 4.  [Browser Testing](#browser-testing)
> 5.  [Code Validation](#code-validation)
> 6.  [Significant Bugs](#significant-bugs)

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
  - On smaller viewports, the **NavBar** is collapsed into a **SideNav**; the icon to present the **SideNav** is a universal burger icon, thus identifiable and relatable.
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

# Manual Feature Testing

The following features were tested manually, as described below.

## User Management

This aspect of the testing focuses on **User Management**:

- Front End and User Experience for Registering, Logging In, Logging Out, and Deleting an account.
- Server data handling and processing, focusing on the respective **User** class and views.
- **Creating, Reading**, and **Deleting** documents from the **Users** Collection in **MongoDB**.

### User: Registration

- Ensure that when a user is not logged in, they are able to access the **Register** link within the **NavBar/SideNav** from any location in the site.
- Ensure that when a user interacts with the **Register** link in the **NavBar/SideNav**, the **Register** modal appears as a slide-up **modal** from the bottom of the screen.
- Ensure that the following validation occurs appropriately, and that the form cannot be submitted if any of the validation is unsuccessful:
  - **Username Validation:**
    - Requirements: _Required/No Spaces_
    - On first interaction, if a user provides a **valid username**, when their focus navigates away from the field, the appearance of the field does not change.
    - If a user does not provide a **username**, the field should turn red when their focus navigates away from the field. When attempting to submit the form a standard browser validation message should confirm the field is required.
    - If a user provides a **username** containing whitespace, when their focus navigates away from the field or they attempt to submit the form, the following custom validation message appears: `Username cannot contain spaces!`, and the field turns red.
    - If the field is in an invalid state, and the user provides a valid **username**, when their focus navigates away from the field or they attempt to submit the form, the field reverts to its valid state.
  - **Password Validation**
    - Requirements: _Required/Between 6 and 20 characters, with one number or special character._
    - On first interaction, if a user provides a valid **password**, when their focus navigates away from the field, the appearance of the field does not change.
    - If a user does not provide a **password**, the field should turn red when their focus navigates away from the field. When attempting to submit the form a standard browser validation message should confirm the field is required.
    - If a user provides a **password** that does not comply with the validation requirements, when their focus navigates away from the field or they attempt to submit the form, the following custom validation message appears: `Password must contain 6-20 characters, and one number or special character`, and the field turns red.
    - If the field is in an invalid state, and the user provides a valid **password**, when their focus navigates away from the field or they attempt to submit the form, the field reverts to its valid state.
  - **Password Confirmation**
    - Requirements: _Required/Must match Password_
    - On first interaction, if a user provides a valid confirmation **password**, when their focus navigates away from the field, the appearance of the field does not change.
    - If a user does not provide a confirmation **password**, the field should turn red when their focus navigates away from the field. When attempting to submit the form, a standard browser validation message should confirm the field is required.
    - If a user provides a **password** that does not comply with the validation requirements, when their focus navigates away from the field or they attempt to submit the form, the following custom validation message appears: `Passwords do not match!`, and the field turns red.
    - If the field is in an invalid state, and the user provides a valid confirmation **password**, when their focus navigates away from the field or they attempt to submit the form, the field reverts to its valid state.
  - If the user is able to bypass the front-end verification, ensure the user is informed via **Toast** what aspect of the verification was unsuccessful, following server-side verification.
- Ensure that if a user attempts to submit the form without the fields being valid, a subsequent valid submission attempt is allowed.
- Ensure that when a user successfully registers, they are presented with a welcome **Toast**, and are automatically logged into their account.
- If a user has attempted to register an account with a username that already exists in the database, regardless of casing, ensure registration is unsuccessful, and the user is informed via **Toast** that the username already exists.
- Ensure that when the user clicks the **Cancel** button within the registration form, or clicks off the **modal**, the **modal** is dismissed.
- Ensure that when the user dismisses the **modal**, the form is cleared and all validation is removed.
- **Database Test:** Ensure that when a user successfully registers, a document is written to the **Users Database**, in the following format:
  - **\_id:** Unique object ID generated by MongoDB
  - **Username:** A lowercase version of the username provided by the user.
  - **Password:** A hashed version of the password provided by the user.
- **Stress Test:** Ensure that when a user that is not logged in types `/register` in the URL, they are redirected to the Home page, and instructed to use the **Register** link to register via **Toast**.
- **Stress Test:** Ensure that when a logged in user in types `/register` in the URL, they are redirected to the Home page, and informed they are already logged in via **Toast**.
- **Stress Test:** Ensure that if a user attempts to submit the form multiple times (clicking **Register** rapidly, for example), only a single **Post** request is made.
- **Database Test:** Ensure that, following rapid form submission testing, only a single document is written to the **Users** database.

### User: Login

- Ensure that when a user is not logged in, they are able to access the **Log In** link within the **NavBar/SideNav** from any location in the site.
- Ensure that when a user interacts with the **Login** link in the **NavBar/SideNav**, the **Login** modal appears as a slide-up modal from the bottom of the screen.
- Ensure that the following validation occurs appropriately, and that the form cannot be submitted if any of the validation is unsuccessful:
  - **Username Validation:**
    - Requirement: _Required_
    - On first interaction, if a user provides a **username**, when their focus navigates away from the field, the appearance of the field does not change.
    - If a user does not provide a **username**, the field should turn red when their focus navigates away from the field. When attempting to submit the form a standard browser validation message should confirm the field is required.
    - If the field is in an invalid state, and the user provides a **username**, when their focus navigates away from the field or they attempt to submit the form, the field reverts to its valid state.
  - **Password Validation:**
    - Requirement: _Required_
    - On first interaction, if a user provides a **password**, when their focus navigates away from the field, the appearance of the field does not change.
    - If a user does not provide a **password**, the field should turn red when their focus navigates away from the field. When attempting to submit the form a standard browser validation message should confirm the field is required.
    - If the field is in an invalid state, and the user provides a **password**, when their focus navigates away from the field or they attempt to submit the form, the field reverts to its valid state.
  - If the **username** cannot be found in the database, or the **password** provided does not match the **hashed password** stored in the database, the user must be redirected to the page they were on, and informed via **Toast** that either the **username** or **password** was incorrect; this message should be presented regardless of which of the two authentication errors occurred.
  - If **Log In** is successful, the user's **username** and **Time Zone** is stored in the session, and they are logged in.
  - If a user has attempted to access a **login restricted** page (such as **My Voice**), and immediately logs into the site successfully, they should be redirected to the page they initially requested.
  - If a user has **not** attempted to access a **login restricted** page (such as **My Voice)**, they must be redirected to the page they were on when logging in.
  - The above successful **log in** events must also apply to when users **register** for an account, due to the automatic **log in**.
  - When a user is **logged in**, they must be able to access the **My Voice** link in the **NavBar/SideNav**.
  - When a user is **logged in**, they must no longer be able to see or access the **Log In** or **Register** links.
  - When a user is **logged in**, they must be able to access the **Logout** link in the **NavBar/SideNav**.
  - Ensure that when the user dismisses the **modal**, the form is cleared and all validation is removed.
- **Stress Test:** Ensure that when a user that is not logged in types `/login` in the URL, they are redirected to the Home page, and instructed to use the **Log In** link via **Toast**.
- **Stress Test:** Ensure that when a logged in user types `/login` in the URL, they are redirected to the Home page, and informed they are already logged in via **Toast**.
- **Stress Test:** Ensure that if a user attempts to submit the form multiple times (clicking **Login** rapidly, for example), only a single **Post** request is made.

### User: Logout

- Ensure that when a user is logged in, they are able to access the **Log Out** link within the **NavBar/SideNav** from any location in the site.
- Ensure that when a user selects the **Log Out** link, they are **logged out** of the website. This includes:
  - Removing the **Username** from the session.
  - Removing the **Time Zone** from the session.
- Ensure that when a user has **logged out**, they are presented with the **Log In** and **Register** links in the **NavBar** / **SideNav**
- Ensure that when a user has **logged out**, they are only have viewing access to the site's contents (as per User Story 3).
- Ensure that when a user **Logs out**, they are redirected to the **Home** page.
- Ensure that when a user **Logs out**, they are presented with a confirmation **Toast**.
- **Stress Test:** Ensure that when a user that is not logged in types `/logout` in the URL, they are redirected to the Home page, and instructed they are not logged in via **Toast**.
- **Stress Test:** Ensure that when a logged in user types `/logout` in the URL, they are logged out, redirected to the Home page, and informed log out has been successful via **Toast**.

### User: Deletion

- Ensure that a user must do the following to **delete** their account:
  - **Log In**
  - Navigate to **My Voice**
  - Open the collapsible labelled **Delete Account**
  - Click the button stating **Permanently Delete**
  - Press **Confirm** in the confirmation box that appears.
- A user must not be able to **delete** their account without following these steps.
- A user must be **logged out** of their account during the **deletion** process.
- A user must not be able to **log in** with their previous credentials once the account **deletion** has occurred.
- Ensure a user's **Wyspas** are also be deleted, after successful account **deletion**.
- **Database Test:** On successful account deletion, ensure the user's entry within the **Users** collection has been removed, and no **Wyspas** exist in the **Messages** collection with the deleted accounts **username** as the **author**.
- **Stress Test:** Ensure that when a user that is not logged in types `/delete_user` in the URL, they are redirected to the **Home** page, and instructed to log in to access this page via **Toast**.
- **Stress Test:** Ensure that when a logged in user in types `/delete_user` in the URL, they are redirected to the **My Voice** page, and informed they must interact with the deletion process, via **Toast**.
- **Stress Test:** Ensure that if a user attempts to submit the form multiple times (clicking **Login** rapidly, for example), only a single **Post** request is made.

## Wyspa Management

This aspect of the testing focuses on **Wyspa Management**:

- Front End and User Experience for **Creating**, **Editing**, **Deleting**, and **Interacting** with **Wyspas**.
- Server data handling and processing, focusing on the respective **Wyspa** class and views.
- **Creating, Reading, Updating**, and **Deleting** documents from the **messages** collection in **MongoDB**.

### Wyspa: Creation

- Ensure that only a logged in user can access the **Wyspa Creation** form in **My Voice**.
- Ensure that when the **Create a Wyspa** form is collapsed, when a user interacts with the heading, the title text changes to "The world is listening…" and the **Wyspa Creation** form appears underneath.
- Ensure that when the **Create a Wyspa** form is revealed, when a user interacts with the **The world is listening…** heading, the title text reverts back to **Create a Wyspa**, and the form collapses.
- Within the **Wyspa Creation** form, ensure that the following validation occurs appropriately:
  - **Your Wyspa**
    - Requirement: _Required/Must not only contain Whitespace_
    - If a user attempts to submit the form without an entry in this field, form submission should be prevented, and a standard browser validation message should confirm the field is required.
    - If the user submits the form with this field containing only whitespace, submission should be successful, but the **Wyspa** should not be written to the **Messages** collection; instead, a **Toast** should inform the user that a **Wyspa** cannot contain only whitespace.
  - **Location**
    - Requirement: _Required/Valid Location_
    - If a user attempts to submit the form without an entry in this field, form submission should be prevented, and a standard browser validation message should confirm the field is required.
    - If the user submits the form with this field containing an unknown address or location, submission should be successful, but the **Wyspa** should not be written to the **Messages** collection; instead, a **Toast** should inform the user that the address was not located.
  - **Mood**
    - Default Value: _Neutral_
    - This field will always contain a value; therefore, a default value of `Neutral` is set, depicted by the **sub-label** with a corresponding **white** colour, and this will be the value submitted within the document if the value is not adjusted by the user. If the **Wyspa** is submitted without the user interacting with this aspect of the form, the value **1** should be stored in the **mood** field of the document written to the database.
    - Dragging the slider to the left should change the field's **sub-label** to `Sad`, with the **sub-label** being coloured **red**. The value **0** should be stored in the **mood** field of the document written to the database.
    - Dragging the slider to the right should change the field's **sub-label** to `Happy`, with the **sub-label** being coloured **green**. The value **2** should be stored in the **mood** field of the document written to the database
    - Dragging the slider back to the central position should revert the field's **sub-label** to `Neutral`, with the **sub-label** being coloured **white**. The value **1** should be stored in the **mood** field of the document written to the database.
  - **Expiry Date**
    - Requirement: _Required/Current or future date_
    - If a user attempts to submit the form without an entry in this field, form submission should be prevented, and a standard browser validation message should confirm the field is required.
    - Ensure that a user cannot type in this field.
    - Ensure that a user cannot copy and paste text into this field.
    - Ensure that when a user interacts with this field, a **date picker** modal appears.
      - Ensure that a user can click off the modal to dismiss it.
      - Ensure that a user can click **cancel** to dismiss the modal.
      - Ensure that a user can navigate through the **date picker**.
      - Ensure that a user can interact with the **year** and **month** dropdowns within the **date picker**.
      - Ensure that a user can select a date, and that when selected, the date populates the field without the user having to click **OK**.
      - Ensure that if a value is in this field, and the user clicks **clear** within the **date picker**, the field is emptied.
    - Ensure that when a date is selected, it appears in the format: `%dd-%mm-%yy`
    - Combined with the **Expiry Time**, if a date and time is selected that is not in the future, form submission will be successful, but the **Wyspa** should not be written to the **Messages** collection; instead, a **Toast** should inform the user that the expiry date must be in the future.
  - **Expiry Time**
    - Requirement: _Required/A time in the future_
    - If a user attempts to submit the form without an entry in this field, form submission should be prevented, and a standard browser validation message should confirm the field is required.
    - Ensure that a user cannot type in this field.
    - Ensure that a user cannot copy and paste text into this field.
    - Ensure that when a user interacts with this field, a **time picker** modal appears.
      - Ensure that a user can click off the modal to dismiss it.
      - Ensure that a user can click **cancel** to dismiss the modal.
      - Ensure the user can first select an **hour**, then select **minutes**.
      - Ensure that when the **minutes** has been chosen, the full **time** populates the field without the user having to click **OK**.
      - Ensure that if a value is in this field, and the user clicks **clear** within the **date picker**, the field is emptied.
    - Ensure that when a time is selected, it appears in the format: `%hh:%mm` in 24hr formatting.
    - Combined with the **Expiry Date**, if a date and time is selected that is not in the future, form submission will be successful, but the **Wyspa** should not be written to the **Messages** collection; instead, a **Toast** should inform the user that the expiry date must be in the future.
- Ensure that on successful **Wyspa** submission, the user is presented with a **toast** confirming it was successful.
- Ensure that on successful **Wyspa** submission, **My Voice** is updated to include the new **Wyspa** (all of a user's active **Wyspas** should be displayed here).
- **Database Test:** Ensure that when a user successfully submits a **Wyspa**, a document is written to the **Messages Database**, in the following format:
  - **\_id:** Unique object ID generated by MongoDB.
  - **author:** The username of the user who submitted the Wyspa.
  - **message:** The text entered into "Your Wyspa".
  - **mood:** A numerical value between 0-2 depicted by slider position.
  - **location:** A Lat/Long dictionary, calculated as per **Wyspa: Location**.
  - **expiry:** A UTC date time stamp, converted as per **Wyspa: Expiry**.
  - **comments:** An empty list.
  - **listens:** An empty list.
  - **listen_count:** An integer representing the length of the listens list (initialised at 0).
- **Stress Test:** Ensure that if a user attempts to submit the form multiple times (clicking **Wyspa** rapidly, for example), only a single **Post** request is made.
- **Database Test:** Ensure that, following rapid form submission testing, only a single document is written to the **Messages** database.

### Wyspa: Edit

- Ensure that if a **logged in** user is viewing a **Wyspa** on the **Wyspa page**, in which they are the **author**, they are presented with an interactive **Edit** icon (next to the **listen** and **random** icons).
  - A user should be able to directly access one of their own **Wyspas** by navigating to it via the **My Voice** page. Alternatively, when randomly viewing **Wyspas** through the **Wyspa: Random Generation** feature, they may be presented with a **Wyspa** they submitted.
- Ensure that if a user clicks on the interactive **Edit** icon, they are taken to the **Edit** page.
- Ensure that when a user is presented with the **Edit** page for a specific **Wyspa**, the respective form input fields are pre-populated with the contents of the **Wyspa**, other than **Location**.
- Ensure that all form validation is identical to that discussed in **Wyspa: Creation**.
- Ensure that on successful **edit**, the user is redirected to **My Voice**, and is informed via **Toast** that the edit was successful.
- **Stress Test:** Ensure that if a user hard codes a URL to force edit a **Wyspa** that is not theirs, they are redirected to their own **My Voice** page, and informed via **Toast** that they are unable to edit a **Wyspa** that does not belong to them.
- **Database Test:** Ensure that on successful **edit**, the correct document in the **messages** collection in MongoDB has been updated, and that the updated information is correct.
- **Stress Test:** Ensure that if a user attempts to submit the form multiple times (clicking **Edit** rapidly, for example), only a single **Post** request is made.
- **Database Test:** Ensure that, following rapid form submission testing, only a single document is updating in the **Messages** database.

### Wyspa: Location

It must be noted that as the **Location** feature heavily relies on the external package **GeoPy**, most of the pure **Lat** and **Long** conversion testing has been completed on the basis of what the expected outcome would be.

- Ensure that each degree of location specificity is translated into the appropriate location:
  - **Europe**: Places a marker in Germany.
  - **Pacific Ocean**: Places a marker in the Pacific Ocean.
  - **UK**: Places a marker in the north of the England.
  - **London**: Places a marker in London.
  - **Buckingham Palace, London**: Places a marker near Buckingham Palace in London.
  - **SW1A 1AA:** Places a marker near Buckingham Palace in London.
  - **Warsaw, Poland**: Places a marker in Warsaw, Poland.
  - **1 Main Street, Leicester**: Places a Marker near Main Street, Leicester.
  - **LE5 1AE**: Places a marker near Main Street, Leicester.
  - **KS, United States**: Places a marker in Kansas, United States.
- Ensure that the geolocation scrambling works as intended.
  - Ensure that when two **Wyspas** are created with the same **Location** specified, they are positioned close to each other on the **Map**, but not in the same position.
  - Ensure that when a user updates their **Wyspa** and provides the same location as the original **Wyspa**, it is in a different position than when first created, but in the same general area.
- **Database Test:** Ensure that on successful **Wyspa Creation** or **Edit**, the relevant document in the **messages** collection in MongoDB contains a **lat**/**long** dictionary in the **Location** field.
- **Stress Test:** Ensure that when a user provides an incorrect location (tested by providing a random string of letters and numbers), the submission is unsuccessful and the user is informed via **Toast** that the location could not be found.

### Wyspa: Mood

The testing for **Wyspa: Mood** was largely completed within the **Wyspa: Creation** section above. As such, the following testing has been condensed.

- Ensure three **Moods** are available for the user to choose when **creating** or **updating** a **Wyspa**:
  - **Neutral**
    - Ensure this is the default value of the slider within the **Wyspa Creation** form when creating a **Wyspa**.
    - Ensure a user can revert to this value when **editing** a Wyspa where the value was previously not `Neutral`.
    - Ensure the value **1** is stored within the **Mood** field of the relevant document within the **messages** collection when writing to or updating the database, when the **mood** has been set to `Neutral`.
    - When completing the **Wyspa** form (for either **creation** or **edit**), ensure the **sub-label** reads `Neutral`, and is **white**.
    - Ensure a Wyspa's corresponding **Marker** on the **Map** is **white**, when the **mood** is set to `Neutral`.
  - **Sad**
    - Ensure the user can select this value on the slider (by dragging the slider left) within the **Wyspa Creation** form when creating a **Wyspa**, or during **editing**.
    - Ensure the value **0** is stored within the **Mood** field of the relevant document within the **messages** collection when writing to or updating the database, when the **mood** has been set to `Sad`.
    - When completing the **Wyspa** form (for either **creation** or **edit**), ensure the **sub-label** reads `Sad`, and is **red**.
    - Ensure a Wyspa's corresponding **Marker** on the **Map** is **red**, when the **mood** is set to `Sad `.
  - **Happy**
    - Ensure the user can select this value on the slider (by dragging the slider right) within the **Wyspa Creation** form when creating a **Wyspa**, or during **editing**.
    - Ensure the value **2** is stored within the **Mood** field of the relevant document within the **messages** collection when writing to or updating the database, when the **mood** has been set to `Happy`.
    - When completing the **Wyspa** form (for either **creation** or **edit**), ensure the **sub-label** reads `Happy`, and is **green**.
    - Ensure a Wyspa's corresponding **Marker** on the **Map** is **green**, when the **mood** is set to `Happy `.

### Wyspa: Listens

- Ensure new **Wyspas** are initialised with an empty list in the **listens** field of the document stored in the database.
- Ensure new **Wyspas** are initialised with **0** in the **listen_count** field of the document stored in the database.
- Ensure users who are not logged in are unable to add **listens** to a **Wyspa**.
  - Although capable of interacting with the **listen icon** in the **Wyspa** page, a logged-out user should be redirected to the same message, with a **toast** confirming they need to log in to add a **listen**.
  - Ensure, when this happens, the **listen** and **listen_field** fields within the relevant **Wyspa's** document in the database have not been modified.
  - Ensure the **listen** count on the **Wyspa** page does not change when this happens.
- Ensure users who are logged in are able to add **listens** to a **Wyspa**.
  - Logged in users who interact with the **listen** icon should be redirected to the same **Wyspa** page, with a **toast** thanking the user for listening.
  - Ensure, following a successful **listen**, that the **listen** field has been updated with the username of the listener being appended to the list within the field.
  - Ensure, following a successful **listen**, that the **listen_count** field has been incremented. The value of the listen count should be the same length as the list within the **listen** field.
- Ensure logged in users can only listen to a single **Wyspa** once.
  - If a user has already **listened** to a **Wyspa**, and attempts to listen to the same **Wyspa** for a second time, they should be redirected to the same message, with a **toast** confirming they can only listen to each **Wyspa** once.
  - Ensure, when this happens, the **listen** and **listen_field** fields within the relevant **Wyspa's** document in the database have not been modified.
  - Ensure the **listen** count on the **Wyspa** page does not change when this happens.
- Ensure that the size of a **Wyspa's Map Marker** increases with the size of the **listen_count** variable.
- **Stress Test:** Ensure that if a user attempts to perform their first **listen** to a single **Wyspa** in quick succession (clicking the **Listen** icon rapidly, for example), only a single valid **listen** is recorded, and any subsequent requests through the route are handled appropriately.
- **Stress Test:** Ensure that if a user hard codes a URL to force **Listen** to a **Wyspa**, the request is handled the same as if the user interacts with the **Listen** icon.

### Wyspa: Comments

- Ensure that when any user visits a **Wyspa**, the comments are collapsed under the **Comments** header.
- Ensure that when a user clicks the **Comments** header, when the comments are collapsed, the **Wyspa's** comments are revealed.
- Ensure that when a user clicks the **Comments** header, when the comments are revealed, the **Wyspa's** comments are collapsed.
- Ensure that **Comments** are displayed sequentially, alternating between left and right speech bubble styling and layout.
- Ensure that **Logged in** users are presented with a **Comment** form at the end of the **comment** trail, contained within the collapsible element.
  - Ensure this element follows the sequential left and right sequencing as existing **comments**.
- Ensure that an empty **comment** cannot be submitted.
  - Ensure a browser standard validation box appears when submitting an empty comment confirming that the text field is required.
- Ensure that a **comment** containing explicitly whitespace cannot be submitted.
  - While the submission will be processed, ensure a **Toast** appears stating that a message must not contain purely whitespace, and ensure the **comment** is not added to the **Wyspa**.
- Ensure that on successful **comment** submission, the user is redirected the same **Wyspa** page, and the **comment** appears appended to the list of existing **comments**.
- Ensure that logged in users with the appropriate access (see below) have the ability to delete a comment. When applicable, a **delete** icon appears underneath the body of the comment.
  - Ensure that **Comment** authors are capable of deleting their comments on a given **Wyspa**.
  - Ensure that **Wyspa** authors are capable of deleting any comment on their own **Wyspa**.
  - Ensure that when a user attempts to **delete** a **Comment**, they are presented with the appropriate confirmation dialogue confirming their request to delete.
  - Ensure that when a user successfully **deletes** a **Comment**, the correct comment is removed from the **Wyspa**, and the order of all other comments remains intact.
- Ensure that when a user is not logged in, and a **Wyspa** has no **Comments**, the **Comment** section contains a text box advising the user that there are no comments on the **Wyspa**, and that they can log in to add a comment.
  - Logged in users should not be presented with this box; instead, the **comment form** replaces this text box.
- **Database Test:** Ensure that when a comment containing pure whitespace is submitted, that the **comments** field within the existing **Wyspa's** document in MongoDB is unchanged.
- **Database Test:** Ensure that when a comment is successfully submitted, that the **comments** field within the existing **Wyspa's** document in MongoDB has the following formatted dictionary appended to the list: `{<Author>; : <Comment>}`
- **Database Test:** Ensure that when a comment is successfully **deleted**, that the **comments** field within the existing **Wyspa's** document in MongoDB no longer holds the deleted comment's dictionary, and that all other elements in the list remain in order.
- **Stress Test:** Ensure that if a user hard codes a URL to force delete a **Comment**, they are redirected to the relevant **Wyspa** page, and instructed to use the icons provided, via **Toast**.
- **Stress Test:** Ensure the confirmation dialogue prevents multiple rapid attempts to delete a comment.
- **Stress Test:** Ensure that if a user attempts to submit a **comment** multiple times (clicking **Add** rapidly, for example), only a single **Post** request is made.
- **Database Test:** Ensure that, following rapid form submission testing, only a single entry is added to the **comment** field of the appropriate document in the **Messages** database.

### Wyspa: Expiry

- Ensure the **Expiry Date and Time** provided by a user during either **Wyspa Creation** or **Edit** is correctly converted to UTC, before being saved to the database.
- Ensure the **Expiry Date and Time** is appropriately converted back to a user's local **Time Zone** when **Wyspas** are displayed to a user in the **My Voice** page.
- Though extensively tested through various means, this is ultimately best described through the following test:
  - Creating a Wyspa while in the UK (British Summer Time: GMT+1)
    - Time of Expiry set, and displayed in **My Voice**: `30th April – 10AM`
  - Passing the account credentials to a user who lives in Spain (Central European Summer Time: GMT+2), and ensuring the **Expiry** was presented to the user as 1 hour ahead of the time initially set.
    - Time of Expiry displayed to Spanish user in **My Voice**: `30th April – 11AM`
  - Checking the **Wyspa** document within the **messages** collection in MongoDB to ensure the time displayed as UTC (GMT).
    - Time of Expiry saved to DB: `30th April – 9AM`
  - This confirms that the **expiry** is being correctly converted from a user's **Time Zone** to UTC for storing in the database, and is correctly being converted from UTC to the user's **Time Zone** when retrieving the **Wyspa** from the database.
- Given the above testing proved the conversion was functioning correctly; when **creating** or **editing** a **Wyspa**, ensure that when a user provides an **Expiry** in the past (after conversion), the submission is not successful, and a **toast** appears confirming the **Expiry** date must be in the future.
- **Database Test:** Ensure that a **Wyspa** document is removed from the **messages** collection in MongoDB when the respective **Expiry Date and Time** is met.
- **Database Test:** Ensure that when a user successfully **edits** a **Wyspa**, the relevant **Wyspa's Expiry** field is updated accordingly with a UTC datetime.

### Wyspa: Deletion

- Ensure a logged in user can interact with the **delete** icon for each individual **Wyspa** in **My Voice**.
- Ensure when a user interacts with the **delete** icon, a confirmation dialogue appears, requesting a user to confirm their decision to delete the respective **Wyspa**.
- Ensure a user can click off the dialogue, or click **back**, to dismiss the dialogue, cancelling the request.
- Ensure that when a user clicks **confirm** within the dialogue, the correct **Wyspa** deleted.
- Ensure that following successful **Wyspa deletion**, the user is redirected to **My Voice**, a deletion confirmation message is presented as a **Toast**, and the deleted **Wyspa** is no longer listed in the user's active **Wyspas**.
- Ensure that when a user has **deleted** all of their **Wyspas** (or have yet to create one), their **My Voice** page states the user has no active **Wyspas**.
- **Database Test:** Ensure that when a Wyspa is successfully deleted, it is removed from the **messages** collection in MongoDB.
- **Stress Test:** Ensure that if a user hard codes a URL to force **delete** a **Wyspa**, the user is redirected to the **My Voice** page and informed via **Toast** to use the **delete** icon to perform this action.

### Wyspa: Random Generation

Considering the nature of pseudo-random generation, capabilities were limited for testing the random **Wyspa** generation. I believe the following is sufficient to deem the feature functions as intended.

- Ensure that a user can be presented with a **random** Wyspa via two methods:
  - Via interacting with the **Wyspa** link in the **NavBar/SideNav**.
  - Via interacting with the **Random** icon on the **Wyspa** page.
- Ensure that interacting with either of these two features presents the user with a perceived **random Wyspa** from the database.
- If no **Wyspas** are available in the Database, the user should be presented with a message (in place of where the **Wyspa message** usually is) stating there are currently no **Wyspas**, and encouraging the user to **Log In** to submit their own.
- **Stress Test:** Ensure that if a user hard codes a URL to force **Random Wyspa generation**, the request is handled the same as if the user initiates this feature via either of the two methods above.

## Map

- Ensure that all users are able to access and interact with the **Map** feature.
- Ensure users can navigate the **Map**, and can zoom in and out.
- Ensure all **Wyspas** in the database are shown on the **Map**.
- Ensure each **Map Marker**'s location correlates with the **Lat/Long** co-ordinates stored in the relevant document's **Location** field within the database.
- Ensure each **Map Marker**'s colour correlates with the following colour **Map**, from the value stored in the relevant document's **Mood** field within the database:
  - 0 : `Red`
  - 1 : `White`
  - 2 : `Green`
- Ensure each **Map Marker**'s radius correlates with the size of the **listen_count** value of the relevant document within the database.
- Ensure each **Map Marker** can be interacted with, regardless of size, location, or overlap.
- Ensure interacting with a **Map Marker** directs the user to the correct **Wyspa Page**.
- Ensure **Map Markers** are placed in order of their radius, so smaller radius **markers** sit on top of the larger radius **markers**.
  - Ensure interacting with a smaller **marker**, which overlaps a larger **marker**, takes the user to the correct **Wyspa Page**.
- **Stress Test**: Ensure that when a user interacts with a **Marker** which relates to a **Wyspa** that no longer exists in the database, the user is redirected to a random **Wyspa** page and the user is informed via **Toast** that the **Wyspa** they are looking for does not exist. _Stress tested by deleting an entry in the database before interacting with the relevant Marker._
- **Stress Test:** Ensure that if the Google Maps API throws an authentication error, the **Map** is replaced with the standard static background, and an error message is presented informing the user to try again. _Stress tested by removing the API key from the script._
- **Stress Test:** Ensure no errors appear when there are no **Wyspas** in the **messages** collection in MongoDB, and the **Map** functions as intended.
- **Stress Test:** Over-ride the **listen_count** value of two documents in the database to 100 and 150 respectively, and ensure they both appear the same size on the **Map** (due to the 100 listen_count value reaching the imposed radius limit within the script).

## Responsive Layout and Design

The features detailed above were re-tested for use on all viewports, including the user interface for responsive layout and design.

### Browser Based Testing

Using Chrome Development tools, either via the pre-set mobile device resolutions or via the manual responsive tool (using `Toggle Device Toolbar`), the following was completed:

- Manual responsive testing via Chrome Development Tools, selecting `Toggle Device Toolbar`.
- Cycling through each available device, and performing the tests as detailed above:
  - Moto G4
  - Galaxy S5
  - Pixel 2
  - Pixel 2XL
  - iPhone 5/SE
  - iPhone 6/7/8 (and plus)
  - iPhone X
  - iPad
  - iPad Pro
  - Surface Duo
  - Galaxy Fold
- Ensure all Features function and appear correctly from at least 320px wide.
- Ensure Modals are presented appropriately on all viewports:
  - Interaction is enabled.
  - The Modal fits on device's screen.
  - The content is legible.
  - The user can dismiss the modal.
- Ensure all **Toasts** appear, are visible and legible, and can be dismissed.

### Mobile and Tablet Testing

The website was physically tested on a Samsung Tab S4, and a Samsung Note 10+ 5G. The following tests were completing:

- Ensure all interactive **icons** are distinguishable, identifiable, and are correctly sized and placed to allow users to interact with each of them via touchscreen individually.
- Ensure all inputs within the **Wyspa Creation** form respond appropriately to touchscreen devices.
- Ensure all text input fields respond appropriately to on-screen keyboards.
- Ensure on-screen keyboards do not obfuscate the users view of the site or the corresponding inputs.
- Ensure the **SideNav** can be swiped to collapse or reveal.
- Ensure the **Map** feature responds appropriately to touchscreen devices (swipe, pinch, touch, etc), and that all **Wyspas** can be interacted with regardless of location or size.

## Additional Testing

### Error Handling

- Ensure that 404 HTTP errors are appropriately routed to 404.html.
  - **Stress Test:** Input an unfamiliar route in the URL
- Ensure **that** 500 HTTP errors are appropriately routed to 500.html.
  - **Stress Test:** Set debug to disabled, and intentionally break a route before attempting to access it.

### Links

- Ensure the link in the footer is visible across all pages, and that a user can interact with it via touch or via mouse click.
- Ensure the link opens up in a new tab.

### Help

- Ensure the **Help** icon is visible and accessible from all pages.
- Ensure that interacting with the **Help** icon brings up a **modal**, with page specific content.
- Ensure the modal's content is legible, and can be scrolled where applicable.
- Ensure the **modal** can be dismissed by interacting with the area outside of the modal, or via clicking the **close** button.
- Ensure each page (including error pages) include page specific content.

# Automated Feature Testing

Due to time constraints, limited unit testing was performed on the project. Below is a demonstration of unit testing, performed with [unittest](https://docs.python.org/3/library/unittest.html) and [Flask-Testing](https://pythonhosted.org/Flask-Testing/); with more time and resources, all of the above features would have been unit tested.

For the full testing file, please see tests.py

## Basic Routing

Test 1: **test_home**

- **Overview** : Test the response from a **get** request to the `/` URL.
- **Expected Result** : 200 response code, index.html template returned, and "Penny for your thoughts" contained within HTML file.
- **Outcome** : Pass

Test 2 **: test_message_overview**

- **Overview** : Test the response from a **get** request to the `/view_message` URL.
- **Expected Result** : 200 response code, and mesages.html template returned.
- **Outcome** : Pass

Test 3 **: test_map**

- **Overview** : Test the response from a **get** request to the `Map_overview` URL.
- **Expected Result** : 200 response code, and **Map** s.html template returned.
- **Outcome** : Pass

Test 4 **: test_my_voice**

- **Overview** : Test the response from a **get** request to the `/my_voice` URL.
- **Expected Result** : 302 response code, with a redirect next parameter of "My Voice" due to login required
- **Outcome** : Pass

## Database CRUD

**Note** : These methods were named in alphabetic sequence to ensure correct compile order.

Test 5: **test_a_register**

- **Overview** : Submit a **post** request to `/register`, and check a user has been added to the **users** collection within MongoDB.
- **Expected Result** : User added to the database, and username verified against that provided during the Post request for registration.
- **Outcome** : Pass

Test 6: **test_b_create**

- **Overview** : Submit a **post** request to `/create_wyspa`, and check a Wyspa has been added to the **messages** collection within MongoDB.
- **Expected Result** : Wyspa is successfully written to the database, and subsequently retrieved from the database for verification.
- **Outcome** : Pass

Test 7: **test_c_create**

- **Overview** : Log in to Wyspa via previously created account, retrieve the previously submitted Wyspa from the DB, submit a **post** request to `/edit_wyspa`, and verify the two Wyspas for full contents and ID comparison.
- **Expected Result** : Log in is successful, Wyspa is successfully retrieved from the database, Wyspa is successfully edited and updated within the database, both Wyspas do not match as a whole, but both contain the same ID.
- **Outcome** : Pass

Test 8: **test_d_create**

- **Overview** : Log in to Wyspa via previously created account, delete the user account, delete all Wyspa's created by test account, and query both the Users and Messages collections for deleted user and Wyspa.
- **Expected Result** : Log in is successful, account is successfully deleted, Wyspa is successfully delete, and query on database produces no results for deleted user and no results for user's Wyspas.
- **Outcome** : Pass

## Wyspa

Test 9: **test_random_wyspa**

- **Overview** : Test the random Wyspa generation.
- **Expected Result** : The method produces a random Wyspa from the Database.
- **Outcome** : Pass

Test 10: **test_location_to_latlong**

- **Overview** : Test whether the location scrambling is working.
- **Expected Result** : Search for "London" via the `location_to_latlong` method, and compare the scrambled results against the true geo-coordinates for London.
- **Outcome** : Pass

## Summary

All tests were successful and performed as expected. Please note that `Flask-testing` is not included in the requirements.txt file as it is not a requirement of the deployed application.

![Unit Test Results](https://res.cloudinary.com/bak2k3/image/upload/v1619531109/WYSPA/unit-test-outcome_rm38ev.jpg)

# Browser Testing

Cross-Browser compatibility was tested via applying the methodology described above within each browser detailed below.

## Chrome/Firefox/Edge/Safari (iOS)

All functionality worked as intended.

## Internet Explorer 11

As WYSPA uses JavaScript ES6, support for Internet Explorer 11 has not been considered or tested.

# Code Validation

## HTML

- The project's HTML was validated using the automated [W3 Markup Validator](https://validator.w3.org/) at intervals throughout the development process.
- At no point were errors or warnings presented, and all HTML files were assessed:
  - Index.html
  - My_voice.html
  - Messages.html
  - Maps.html
  - Edit_wyspa.html
  - 404.html
  - 500.html

## CSS

- The project's CSS was validated using the automated [W3 Jigsaw Validator](https://jigsaw.w3.org/css-validator/) at intervals throughout the development process.
- At no point were errors presented.
- At time of deployment, there are 40 warnings:
  - 1: ` Imported style sheets are not checked in direct input and file upload modes`.
    - Satisfied this is informational to confirm imported style sheet is not being validated.
  - 39: `<extension> is an unknown vendor extension`.
    - Satisfied these can be dismissed.

## JavaScript

- The project's JavaScript was validated using the open source automated service, [JSHint](https://jshint.com/), at intervals throughout the development process.
- Warnings are currently present; however, these are regarding ES6 Compatibility; I'm aware of these and am satisfied these can be dismissed.
- One error was presented, in **maps.js**, when using a `for (const x in y)` statement:
  - `The body of a for in should be wrapped in an if statement to filter unwanted properties from the prototype.`
  - This was easily fixed after reviewing a similar error on [StackOverflow.](https://stackoverflow.com/questions/4166551/javascript-jslint-error-the-body-of-a-for-in-should-be-wrapped-in-an-if-statem)
- At the time of deployment, no errors are present.

## Python

- The project's Python was validated for PEP8 compliance using [Pylint](https://pypi.org/project/pylint/), via the terminal, at intervals throughout the development process.
- The following warnings were presented:
  - [app.py:15:4](https://github.com/BAK2K3/WYSPA/blob/86dec8a923916d6afebb6d12a7ed1ab462443b77/app.py#L14): `W0611: Unused import env (unused-import)`
  - [wyspa/factory/initialisation.py:18:4](https://github.com/BAK2K3/WYSPA/blob/86dec8a923916d6afebb6d12a7ed1ab462443b77/wyspa/factory/initialisation.py#L18): `W0611: Unused import env (unused-import)`
    - These warnings have been considered, however they appear to be incorrectly reporting `env.py` as being unused, due to how env.py works. Once deployed, this will not be imported anyway, and therefore this has been added to the ignore rule within these particular python modules.
    - `# pylint: disable=unused-import`
  - [wyspa/messages/classes.py:26:0](https://github.com/BAK2K3/WYSPA/blob/86dec8a923916d6afebb6d12a7ed1ab462443b77/wyspa/messages/classes.py#L29): `R0902: Too many instance attributes (9/7) (too-many-instance-attributes)`
  - [wyspa/messages/classes.py:127:4](https://github.com/BAK2K3/WYSPA/blob/86dec8a923916d6afebb6d12a7ed1ab462443b77/wyspa/messages/classes.py#L130): `R0913: Too many arguments (10/5) (too-many-arguments)`
    - The root cause of both of these warnings are related; as the Wyspa class has 9 attributes, with the `__init__` method using 10 arguments (including self), PyLint is warning that the class may be overly complicated and hard to read.
    - I have considered the warnings, and ways in which the Class could be refactored further, but believe that the current functioning Class appropriately encapsulates the Wyspa object, and whilst it contains a large amount of attributes, believe this is necessary in this instance and is not overly complicated.
    - As such, ignore rules have been added to the top of messages/classes.py.
    - `# pylint: disable=too-many-arguments, too-many-instance-attributes`
  - [wyspa/messages/views.py:315:0](https://github.com/BAK2K3/WYSPA/blob/86dec8a923916d6afebb6d12a7ed1ab462443b77/wyspa/messages/views.py#L317): `R0911: Too many return statements (7/6) (too-many-return-statements)`
    - This warning relates to the `edit_wyspa` route, as it has 7 return statements within the logic of both the Get/Post routes combined.
    - I have considered this warning, and looked at possibly refactoring the logic within this route. One possibility was to create an additional method within the Wyspa class that verifies each field of a Wyspa (create or edit) following user submission, returning specific error message to present to the user. However, I believe the logic for this validation belongs within this particular route. I also don't believe this warning was designed for analysing Flask routes. Regardless, I do not believe this particular route is overly complicated or difficult to navigate. As such, an ignore rule has been added to the top of messages/views.py.
    - `# pylint: disable=too-many-return-statements`
- Having individually reviewed each python file, and considered the warnings above, there are currently no other PEP8 warnings.

![pylint](https://res.cloudinary.com/bak2k3/image/upload/v1619531108/WYSPA/pylint_xk5fid.jpg)

## Accessibility, Performance, and Best Practice

- The project's Accessibility, Performance, and Best Practices audit was undertaken with [Google Lighthouse](https://developers.google.com/web/tools/lighthouse).
- Please note any **Login Required** routes, such as **My Voice**, were not capable of being audited due to how the audit is completed. However, the results of the successful tests provide a good indication as to how these particular routes might have performed given they share a base template.

### Desktop

#### Home

![lighthouse home desktop](https://res.cloudinary.com/bak2k3/image/upload/v1619531107/WYSPA/lighthouse_home_desktop_vwu65f.jpg)

#### Map

![lighthouse Map desktop](https://res.cloudinary.com/bak2k3/image/upload/v1619531107/WYSPA/lighthouse_map_desktop_tsuagi.jpg)

#### Message

![lighthouse message desktop](https://res.cloudinary.com/bak2k3/image/upload/v1619531107/WYSPA/lighthouse_wyspa_desktop_yplzam.jpg)

### Mobile

#### Home

![lighthouse home mobile](https://res.cloudinary.com/bak2k3/image/upload/v1619531107/WYSPA/lighthouse_home_mobile_jkg8zg.jpg)

#### Map

![lighthouse Map mobile](https://res.cloudinary.com/bak2k3/image/upload/v1619531107/WYSPA/lighthouse_maps_mobile_dkkvzn.jpg)

#### Mobile

![lighthouse message mobile](https://res.cloudinary.com/bak2k3/image/upload/v1619531107/WYSPA/lighthouse_wyspa_mobile_owsy9o.jpg)

- It appears the Mobile Performance was reduced due to the throttling imposed on the mobile testing for the Lighthouse assessment.
- The static background image could have been compressed for slightly better performance under throttling, however this was tested and resulted in a substantial difference in quality; the distinct outline was missing from the **Map**, which reduced the impact the image had.

# Significant Bugs

## Time Zone Conversion

**Fixed: Yes**

When initially implementing an Expiry Date/Time for MongoDB to index TTL from, Time Zones were not considered. As my Time Zone matched UTC (the standard time format [MongoDB uses](https://docs.mongodb.com/manual/tutorial/model-time-data/)), at the time of initial implementation, I did not encounter any issues. However, following the change to Daylight Savings, I realised that the Expiry Date/Time a user was inputting into the database was being stored as pure UTC. As such, when storing an expiry of 15:00 (as a GMT+1 user), this was being stored directly into the Database as 15:00 (UTC), and was therefore not expiring until 16:00 (the GMT+1 representation of 15:00 UTC).

Many solutions were explored to try and implement Time Zone conversion, and consideration was given as to **how** a Time Zone could be obtained from the user, given the user, server, and database could all potentially be in different Time Zones at any given time.

Given any logic within python would be calculating a DateTime depending on the Time Zone of the server it was being hosted on, the first step was to obtain the user's Time Zone via the browser, before attempting to handle and process this data in the server. The following JavaScript code snippet taken from [StackOverflow](https://stackoverflow.com/a/34602679/13810970) obtains a user's [IANA](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) Time Zone.

```javascript
Intl.DateTimeFormat().resolvedOptions().timeZone;
```

With a user's Time Zone now accessible, a decision had to be made as to how to store this information. The following solution was considered:

- Storing the user's Time Zone in an additional parameter in the **expiry** field within a document in the **messages** collection.
  - Considering the PEP8 warnings regarding the complexity of the existing **Wyspa** class, it was decided not to proceed with adding additional attributes to the class.

Ultimately, the decision was made to create hidden form fields within the Login and Register forms, which are automatically populated with the user's Time Zone (using the aforementioned code snippet). This is then passed to the server when a user Registers/Logs In, and is stored in the Session, under the **timezone** key. This results in the user's Time Zone being accessible at any time within Python.

When a user **Creates** or **Edits** a **Wyspa,** the time is converted to a DateTime object, and assigned the Time Zone of the current user before being submitted to MongoDB. A helpful discussion on this topic was found on [StackOverflow](https://stackoverflow.com/a/4771733/13810970). As this DateTime object is now Time Zone aware, when submitted to MongoDB it is automatically converted to UTC based on this information.

The next step was to decide how to convert this UTC Date Time back to a User's Time Zone whenever it was to be displayed back to the user. The following solution was considered:

- Utilising MongoDB's aggregate functions such as [toDate](https://docs.mongodb.com/manual/reference/operator/aggregation/toDate/) or [dateToString](https://docs.mongodb.com/manual/reference/operator/aggregation/dateToString/), combined with a [Time Zone Offset](https://docs.mongodb.com/manual/reference/operator/aggregation/hour/).
  - Unfortunately, these features are only available for paid databases.

The decision was made to make a standard query from the database, and replace the Expiry attribute of each returned Wyspa object with a Time Zone converted version of the UTC time object retrieved from the database. Once this is complete, it can then be converted to the appropriate string value to be presented to a user.

In order to test this fully, a user in Spain (UTC+2) created a Wyspa, and shared their **My Voice** page (which displays Wyspas' expiry dates), for me to compare against the relative document stored in the MongoDB collection:

![spain_my_voice](https://res.cloudinary.com/bak2k3/image/upload/v1619531109/WYSPA/Spain_Wyspa_Page_f354d8.png)

![spain_mongoDB](https://res.cloudinary.com/bak2k3/image/upload/v1619531108/WYSPA/Spain_DB_Entry_mjrfx0.png)

This solution means a user can submit a Wyspa whilst in one Time Zone, and be presented with its relative Expiry date if viewing the website in a country with a different Time Zone.

**Assigning Expiry Date the user's Time Zone**

```python
user_timezone = tz.gettz(session["timezone"])
formatted_expiry = formatted_expiry.replace(tzinfo=user_timezone)
```

**Converting Expiry Date from UTC to user's Time Zone**

```python
user_timezone = tz.gettz(session["timezone"])
formatted_expiry = formatted_expiry.astimezone(user_timezone)
```

## Double Form Submission

**Fixed: Yes**

When initially implementing and testing the **Wyspa: Comment** feature, I accidentally clicked the **Add** button within the comment form after inputting a comment. This resulted in two identical comments being added to the **Wyspa**. This brought to light the fact that forms were capable of rapidly being submitted.

![Double Comment](https://res.cloudinary.com/bak2k3/image/upload/v1619531106/WYSPA/empty_comment_oqhsru.jpg)

After researching a [potential workaround](https://www.bram.us/2020/11/04/preventing-double-form-submissions/) to this, I implemented an **is-submitting** class, which is attached to forms (via a custom JavaScript function) following submission, and all forms are prevented from being submitted if they contain this class. As such, after a form has been submitted, it will be blocked from being submitted on subsequent attempts.

However, this had an unintended effect on the Registration Form. If a user attempted to register with an invalid Username, Password, or Confirmation Password, they were prevented from subsequent attempts to register until the browser had been refreshed or the user navigated to a different page.

In order to rectify this, the registration form was excluded from the global form function discussed above, which applied **is-submitting** to all forms on submission. Instead, the addition of the **is-submitting** class was added to custom form-validation script, as part of the final checks when all other fields are valid. As a result of this, the registration form is still subject to the **is-submitting** submission exclusion, but the class is only added when all fields within the form are valid.

## Login and Register Modals

**Fixed: Yes**

When implementing the Login and Register Modals, I was keen to ensure that a user was never redirected away from any content in order to perform these actions. However, due to the size of the on-screen keyboard on physical mobile devices, and due to the implementation of modals in Materialize CSS, I identified that when attempting to log in or register on physical devices, the on screen keyboard would cause the respective modal to shrink, causing a user to have to scroll through the respective interface to log in or register. As you can see from the examples below, this resulted in validation errors or buttons being hidden from the user.

![Old login mobile](https://res.cloudinary.com/bak2k3/image/upload/c_scale,h_765/v1619531061/WYSPA/LoginMobile2_lx9gdj.jpg)

![Old Register](https://res.cloudinary.com/bak2k3/image/upload/c_scale,h_765/v1619531062/WYSPA/RegisterMobile2_qjdq6p.jpg)

The solution to this was to replace these modals with **slide-up** modals. I found that these inherently utilised space on the device more efficiently and effectively, and obfuscated less of the user's view when initially interacted with. The **help** modal still uses normal modals, as the variation of interfaces produces a much more dynamic website as a whole.

![New Mobile Login](https://res.cloudinary.com/bak2k3/image/upload/c_scale,h_765/v1619531061/WYSPA/loginnewmobile_pkd5vh.jpg)

![New Mobile Register](https://res.cloudinary.com/bak2k3/image/upload/c_scale,h_765/v1619531061/WYSPA/registernewmobile_tzetti.jpg)

## Unexpected Date Picker Behaviour

**Fixed: Yes**

When initially implementing the **Date and Time Pickers** for **Wyspa: Create** and **Wyspa: Edit**, the features were tested on a physical mobile device. While these features appeared to work fine on Chrome Developer Tools, when using a mobile browser (tested on Chrome and Firefox), the **Year** and **Month** drop-downs within the **Date Picker** was automatically disappearing on the first interaction every time. This provided a very poor user experience, so I attempted to research what was causing it.

After reaching a dead end with the specific nature of this particular issue, I looked into the Materialize CSS [issues](https://github.com/Dogfalo/materialize/issues) to find 616 open issues, with the last commit being in June 2020. A discussion on one of the issues stated the repository was [no longer being supported](https://github.com/Dogfalo/materialize/issues/6615), and that a group of contributors had forked the project and have been producing nightly builds of a _"community enhanced"_ [Materialize CSS](https://github.com/materializecss/materialize).

I created a new branch within my project (called nightly-css), and attempted to integrate a [nightly build](https://nightly.link/materializecss/materialize/workflows/nightly/v1-dev/build) of the community enhanced Materialize CSS on the off chance that this would resolve the Date Picker behaviour. After hosting the source code locally, and removing the CDN links to the old Materialize, I tested all features of the website thoroughly, and while there did not appear to be any substantial differences to the framework (other than a [deprecated component](https://github.com/materializecss/materialize/pull/49) of the Toast that I needed to update), everything worked as intended, and the Date Picker dropdowns no longer dismissed on first interaction; this is the reason the project uses the open sourced, community driven, version of Materialize CSS.

The deployed version of this project uses the first full [Alpha](https://github.com/materializecss/materialize/releases) release of the community enhanced Materialize CSS.

## Changing Layout in Chrome Dev Tools Breaks Page Layout

**Fixed: No**

When using Chrome Development Tools, when switching between a Responsive Layout and a Mobile-Specific layout, the page's structure will **sometimes** not update to the new screen size. While the background of the website remains full screen, all other components, whilst appearing to maintain the correct aspect ratio for the given device, do not fill the screen.

![Chrome Mobile Dev Tools](https://res.cloudinary.com/bak2k3/image/upload/v1619531062/WYSPA/chrome-dev-mobile_jbkgaa.jpg)

I have been unable to pinpoint the reason why this happens, and it doesn't appear to happen every time, however I am aware this is a development bug only, and would never have an impact on user experience. The website has been tested extensively on physical devices, and while using browsers (without inspector/development tools open) and this bug cannot be recreated in these instances.

## Korea Uses Default Map Style

**Fixed: N/A**

While testing the **Map** feature, I identified that when zooming into South Korea, all **Map** styles are reverted to default.

![Korea Google Maps](https://res.cloudinary.com/bak2k3/image/upload/v1619531106/WYSPA/Korea_Google_Maps_stumu2.jpg)

However, having [researched this issue](https://support.google.com/maps/forum/AAAABJRTXHEAI_0FslsAs4/?hl=ko&gpf=%23!topic%2Fmaps-ko%2FAI_0FslsAs4), it appears that South Korea has restrictions on the ability to export **Map** data to overseas data centres, and as such some **Map** stylings do not apply. Accordingly, there is no fix for this bug, and the issue remains.

---

[Click here](README.md) to return to the main README.md.
