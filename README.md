![WYSPA Logo](https://res.cloudinary.com/bak2k3/image/upload/v1614792358/WYSPA/WYSPA-logo_asepp4.jpg)

# **WYSPA**: Wyspa Your Secrets, Publicly and Anonymously

WYSPA is an anonymous social media network, allowing users to post, comment on, and listen to messages anonymously.

View deployed site on [Heroku](https://w-y-s-p-a.herokuapp.com/).

# Table of contents

> 1.  [Overview](#overview)
> 2.  [UX](#ux)
>     1.  [Strategy](#strategy)
>     2.  [Scope](#scope)
>     3.  [Structure](#structure)
>     4.  [Skeleton](#skeleton)
>     5.  [Surface](#surface)
> 3.  [Features](#features)
>     1.  [Existing Features](#existing-features)
>     2.  [Future Feature Considerations](#future-feature-considerations)
> 4.  [Technologies Used](#technologies-used)
> 5.  [Testing](#testing)
> 6.  [Deployment](#deployment)
> 7.  [Credits](#credits)
>     1.  [Content](#content)
>     2.  [Media](#media)
>     3.  [Code](#code)
> 8.  [Acknowledgements](#acknowledgements)
> 9.  [Disclaimer](#disclaimer)

# Overview

> _**Wyspa**_  
> ˈwɪspə | NOUN  
> 1: **WYSPA** (Acronym): Whisper Your Secrets Publicly and Anonymously – The Anonymous Social Media Network. _”Are you on WYSPA?”_  
> 2: **Wyspa** : An anonymous message. _”Have you listened to any Wyspas today?”_

**Wyspa** is an anonymous social media network, designed to inspire self-expression; it encourages the acknowledgement of, and engagement with, other posts to increase their visibility. All posts have user-determined expiry dates, and can be viewed on a global map, based on their scrambled geolocation.

The project was developed using **HTML**, **CSS**, **JavaScript**, and **Python**, and utilises a NoSQL document-based database via **MongoDB**.

---

# UX

## Strategy

### Stakeholder Interview

**What would your ideal social media network look like?**

“_I don’t want to need to have a large following/network in order to get the most out of the platform.”_

“_I don’t want to be judged by my friends and family for how I’m feeling.”_

“_I want to be able to support those who need it.”_

“_I want to feel like my contribution makes a difference.”_

“_I want a more creative interface, and various degrees of interaction, in comparison to modern social media networks.”_

### Similar Project Review

**Whisper:** [http://whisper.sh/](http://whisper.sh/)

Whisper is a Social Media Network which allows users to make anonymous posts, which are called “Whispers”, and as of 2015 had 250 million monthly users. The platform has a dedicated app (for Android and IOS), however users can access and utilise the service via a browser (desktop/mobile). Whispers are created by providing a short extract of text, which are then overlayed onto either a user-provided or database generated image. Users can engage with each other through either post comments, or private pseudonymous chats. In terms of user experience, when first visiting the site its intention and purpose is unclear, as it appears to have become heavily influenced by brand advertising and blog posts; in order to find the “Whispers”, a user must first engage with a blog post, which in turn displays a random selection of relevant Whispers underneath. In its current state, without any prior knowledge of the site or its concept, it may not be clear how to use the site, or what its purpose is.

**Facebook:** [https://www.facebook.com/](https://www.facebook.com/)

Facebook is currently the most popular social media network, with approximately 2.5 billion monthly active users. The concept of Facebook is primarily focused on a user’s “network”; insomuch as that the content they are shown is depicted by the size of their network. Users who have a much more diverse and growing network will be shown a wealth of content, as opposed to newer users (who have fewer “Friends”), who will have generic (if not limited) content being provided. Facebook is not an anonymous network, and all content, including personal data, is stored indefinitely unless requested otherwise by the user. The site’s intention and user interface is extremely effective; the implementation of the _”endless scroll”_ effectively engages users, to the extent the platform has been criticized for being [addictive](https://www.sciencedirect.com/science/article/abs/pii/S0165178117311678).

### User Stories

1. `”As a visitor to the website, I want to know what the website does, so that I can decide whether I’m interested in engaging within it.”`
2. `”As a potential user, I want the usage to be either self-descriptive or the instructions clearly communicated, so that I can interact with the site with ease.”`
3. `”As an unregistered user, I want to be able to view content on the site without having to register, so I can decide whether to make an account.”`
4. `”As an unregistered user, I want to be able to make an account and log in, so that I can benefit from the features of a registered user.”`
5. `”As a logged in user, I want to be able to make posts anonymously, and engage with other posts anonymously, so that I can express myself or support others without exposing any personal details.”`
6. `”As a logged in user, I want to be able to edit or delete content, so that I have control over the content I have stored on the platform.”`
7. `”As a user, I want to be able to see a Map of, and individually interact with, all Wyspas so that I can decide what content I see and interact with.”`
8. `”As a mobile user, I want to be able to utilise all aspects of the site, so that I can interact with the website on the go.”`

### Project Strategy Summary

**Ideal User:** An individual who wants to express themselves anonymously, or support and communicate with others anonymously.

**Project Goal:** Provide a platform on which users can express themselves anonymously, allowing them control over their contributions, and giving them a sense of “involvement” in how the platform works.

**User Needs:**

- To be able to navigate the site with ease.
- To be able to create an account and log in.
- To be able to create, edit, and delete a Wyspa.
- To remain anonymous at all times.
- To be able to view a world Map of Wyspas.

**Project Objectives** :

- To create a social media network that allows anonymity.
- To give users a sense of involvement and contribution to how the platform works.
- To engage the user through unique features.
- To allow the user to navigate and control the application with ease on all platforms and devices.

## Scope

### Functional Requirements

#### Simple, Intuitive, and Engaging Interface

- Allow a user to navigate, and interact with, the site with ease.
- Take a minimalistic approach to layout, content, and structure, whilst always presenting sufficient and relevant information.
- Ensure the layout and design is responsive to all media sizes.

#### User Management

- Allow a user to create an account, log in, log out, and delete their account.

#### Anonymous Wyspa Management and Interaction

- Allow a user to create **Wyspas** anonymously.
- Allow a user to edit and delete their own **Wyspa**.
- Allow a user to comment on any **Wyspa**, and delete any comments they have made.
- Allow a user to remove any comments left on their own **Wyspa**.
- Allow a user to engage with other **Wyspas** through “**Listens**”.

#### Random Wyspa Generation

- Allow a user to request a random **Wyspa** to view, comment on, and listen to.

#### Interactive Wyspa Map

- Allow a user to navigate a world **Map** presenting all **Wyspas** available, positioned according to their geolocation.
- Allow a user to interact with each **Wyspa** individually.
- Allow a user to identify the Mood of the **Wyspa** through colour.
- Allow a user to identify how many **Listens** the **Wyspa** has had through size of its marker.

### Content Requirements

#### User created Wyspas

- The website’s primary content is entirely user generated; the creation and editing of **Wyspas** within in the database.
- When creating a **Wyspa**, the following information will be recorded, and for the following purposes:
  - **Author:** This will be pre-populated by the server, allowing backend verification of **Wyspa** ownership.
  - **Message:** This will be provided by the user, in free-text form. This will be the message the user would like to communicate, and therefore the message other users are able to read.
  - **Location:** This will be provided in a verbose manner by the user (i.e London), converted to Lat-Long (51.500153° N, -0.1262362° E), and scrambled (N/E +-0.1). This will be used to position the **Wyspa** on the **Map**.
  - **Mood:** This will be chosen by the user, out of choices presented to them. This will be used to colour the **Wyspa** marker on the **Map**.
  - **Expiry Date:** This will be set by the user. This will depict when the document removed from the database.
  - **Comments:** This is an entry which all logged in users will be able to contribute to; these comments will be displayed on the individual **Wyspa** page.
  - **Listens :** This is an entry which will log the users who have listened to a **Wyspa** ; this will be used to prevent any single user listening to a **Wyspa** more than once.
  - **Listen_Count:** This is an entry which counts the total amount of **Listens** contained within a whisper. This will be used for both sorting the database entries for the **Map**, depicting the size of the **Map** marker, and for displaying the amount of **Listens** a **Wyspa** has on the individual **Wyspa** page and profile page.

## Structure

### Informational Architecture

**Wyspa** has been designed to combine persistent elements, which a user may want to access at any given location, with unique elements, which a user may want to visit with a specific intention. This allows the content to be condensed and minimalistic, yet intuitive and user friendly.

#### Persistent

##### Header

The header of the page contains the **NavBar**, the **Logo**, and the **Help** function. It is a static element, and is affixed to the top of the page at all times. Where the page body content exceeds the viewport of the screen, the **NavBar** has been designed **not** be a “sticky” element, so as to utilise the full viewport when required.

##### Navigation

On larger viewports, the navigational elements are separated into separate links within the **NavBar**. On medium viewports and lower, the navigational elements are collapsed into a **SideNav**, which can be activated with a toggler in the upper-left corner.

##### Logo

The **Logo** is centrally placed within the Header element, regardless of viewport.

##### Help

The **Help** functionality is embedded into every page, with the interactive icon placed in the top right of the header, regardless of viewport.

##### Login / Register / Logout

The **Login** / **Register** functionality is embedded into every page; this allows a user to **log in** or **register**, via a slide-up **Modal**, or **log out**, regardless of their location on the site.

##### Footer

The footer is statically positioned at the bottom of the page. Similar to the header, this is not a sticky element, and when content exceeds the viewport of the device, the footer is pushed out of the viewport. The footer contains a link to the project’s GitHub repository; however, its primary intention is to enclose the webpage to produce a letterbox style aesthetic.

#### Unique

##### Index

The Index page contains an overview of the website, describing and linking the main three features, along with a call to action.

##### My Voice

The **My Voice** page offers a profile section, where users can view and manage their existing **Wyspas**, create new **Wyspas**, or delete their account.

##### Wyspa

The **Wyspa** page provides users with a randomly selected **Wyspa**. From here, users can read, listen to, comment on, and edit **Wyspas**.

##### Map

The **Map** page provides a **Map** of the world, with the existing **Wyspa’s** markers placed depending on their geolocation, their size depending on how many **Listens** they have, and their colour depending on the mood of the **Wyspa**.

### Interaction Design

##### NavBar

The **NavBar** contains the four unique page locations, along with the log in, register, and log out functionality, where applicable. When a user is located on one of the four unique locations, the active position is represented with alternative shading and styling on the relevant link within the **NavBar**. This allows a user to know where they are at any given time. This feature is applied to all viewports, with the styling varying slightly depending on whether a full **NavBar** or **SideNav** is in use.

##### Login/Register/Logout

If a user is not logged in, the **NavBar/SideNav** provides the relevant **Log In/Register** links. When a user interacts with the **Log In/Register** link within the **NavBar**, a **slide-up Modal** appears which presents them with the required functionality. When a user is logged in, the **Logout** link replaces the **Log In/Register** links.

##### Help

Interacting with the **Help** icon initialises a **centrally positioned Modal** which presents the user with additional information relevant to the page they’re currently engaged with. While the functionality of the help feature is baked into the persistent HTML across the site, the content is dynamically generated depending on a user’s location. While the interface for each aspect of the site is designed to be intuitive and self-explanatory, this feature provides additional information if a user requires it.

##### Wyspa

Each time the user visits the **Wyspa** page, a **Wyspa** from the database is selected at random and presented to the user.

The content of the **Wyspa** is the primary aspect of this page, and is therefore placed in central view of the user and cannot be hidden. Underneath the content of the **Wyspa** is “Listen” counter, displaying how many users have “Listened” to the **Wyspa**, along with an interactive icon which allows a user to “Listen” to the **Wyspa**. Next to this icon lies a **Random Wyspa** icon, which randomly selects a new **Wyspa** from the database. If the author of the **Wyspa** is currently logged in, an **edit** icon is also provided here, navigating the user to a dedicated edit page.

The comments for the selected **Wyspa** are hidden in a collapsible interactive element. This gives the user interactive control over how different aspects of the content are displayed. When this element is shown, the comments are displayed vertically, alternating left and right to produce a **conversational** aesthetic. For each comment, an interactive **delete** icon is presented to both the owner of the **Wyspa**, and the owner of the **comment.** This icon is displayed directly underneath the relevant comment, within its container.

##### My Voice

**My Voice** shows a list of all active **Wyspas** the user has within the database. Each **Wyspa’s** message is displayed, along with a counter displaying how many **Listens** the **Wyspa** has, an interactive icon allowing the user to directly access the **Wyspa,** and an interactive **delete** icon. Consideration was given to add the **edit** icon within this contextual menu, however this resulted in a cluttered screen space, and prevented the tooltips from displaying as intended due content overflowing.

Underneath the existing **Wyspas** is a collapsible element in which contains a **Wyspa Creation** form. The form contained within this element is self-descriptive with a user-friendly design, and is easy to complete and navigate. When the user interacts with the collapsible element, the heading text changes from “Create a **Wyspa**” to “The world is listening…”. This is reverted when this element is collapsed.

Underneath the **Wyspa Creation** form is a **Delete Account** container. A user must interact with this element to reveal a button which states **Permanently Delete.** This button will also produce a confirmation modal.

##### Map

The **Map** feature takes the user directly to an interactive **World Map**, whereby all currently active **Wyspas** are displayed. A user can interact with a **Wyspa** by clicking on it, taking them directly to its **Wyspa page**. A **Wyspa’s** colour, size, and placement are all influenced by how users interact with and contribute to it. The **Map** itself is easy to navigate on all viewports, with intuitive zoom and drag functionality.

##### Tooltips

All interactive icons throughout **Wyspa** contain **tooltips**; on Desktop, these appear when the user highlights the icon with a cursor. While the icons are self-descriptive, the tooltips provide an extra depth of engagement and interactivity. However, in its current state, a Mobile friendly tooltip has yet to be implemented, due to the nature in which they are interacted with and displayed. As such, Tooltips are disabled for Mobile users; however, the help functionality contains all additional and relevant information for each page and each interaction if required.

##### Toasts

**Toasts** are used across **Wyspa** to communicate short snippets of important information without obfuscating the viewport, and without overloading the user with information. These can be dismissed via a “Dismiss” button within the **Toast**, or can be swiped away on mobile. These have been implemented to re-affirm a user’s action, or to draw a user’s attention to an error, providing an effective means of feedback to the user.

## Skeleton

### Wireframes

**Due to the resolution of the wireframe documents, it is recommended that these PDFs are downloaded to be viewed in the browser, rather than using GitHub’s native PDF viewer.**

Header and Footer Wireframe: [Link](./wyspa/static/wireframes/header-footer-wireframe.pdf)

Index Wireframe: [Link](./wyspa/static/wireframes/index-wireframe.pdf)

My Voice Wireframe: [Link](./wyspa/static/wireframes/my-voice-wireframe.pdf)

Wyspa Wireframe: [Link](./wyspa/static/wireframes/wyspa-wireframe.pdf)

Map Wireframe: [Link](./wyspa/static/wireframes/map-wireframe.pdf)

Edit Wireframe: [Link](./wyspa/static/wireframes/edit-wireframe.pdf)

### Database

**WYSPA** utilises a NoSQL document-based Database via MongoDB for storing **User** credentials and **Wyspas**. The project uses two Collections: **Users**, and **Messages**. The format and structure of these collections are illustrated below:

![Database Design](https://res.cloudinary.com/bak2k3/image/upload/v1619531106/WYSPA/DB_Diagram_qxcjqm.png)

## Surface

The project encompasses the **Dark Mode** aesthetic, aligning with the secretive yet personal and sensitive nature of the project. Its intention is to be engaging, alluring, and cohesive.

### Colour Scheme

#### Primary Colour Scheme

The primary colour scheme implemented across the project is a blue monochromatic scheme. The colours complement each other, yet are distinguishable when side-by-side.

![Primary Colour Scheme](https://res.cloudinary.com/bak2k3/image/upload/v1619532900/WYSPA/Wyspa_Palette_b0yvvu.jpg)

#### Text Colour Scheme

Text against a dark body is pure white, while text against a white body is pure black. Whilst the chosen text colour scheme may seem basic, it complements the overall monochromatic blue colour scheme very well, and produces excellent contrast between the types of content being displayed.

**White Text on Black Background**

![White Text on Black Background](https://res.cloudinary.com/bak2k3/image/upload/v1619532900/WYSPA/White_Text_uwmv3j.jpg)

![White on Black accessability](https://res.cloudinary.com/bak2k3/image/upload/v1619531061/WYSPA/white_on_black_dqlzuc.jpg)

**Blck Text on White Background**

![Black Text On White Background](https://res.cloudinary.com/bak2k3/image/upload/v1619532900/WYSPA/Black_Textr_agnfyk.jpg)

![Black on White accessability](https://res.cloudinary.com/bak2k3/image/upload/v1619531061/WYSPA/black_on_white_uix0ff.jpg)

### Typography

#### Logo Font

[Cinzel Decorative](https://fonts.google.com/specimen/Cinzel+Decorative?preview.text=WYSPA&preview.text_type=custom) was chosen for the **Logo**. This font is flamboyant, loud, and it stands out. The Logo is the only item within the project that uses this font, due to its iconicity, intending to make the logo, brand, and name recognisable.

#### Body Font

[Roboto](https://fonts.google.com/specimen/Roboto?preview.text=Penny%20for%20your%20thoughts%3F&preview.text_type=custom&query=roboto) was chosen for the **Body** text of the project. This font is simple, legible, and due to it being the default font for Android devices, is recognisable and relatable.

### Visual Effects

#### Google Maps and Static Background Image

The **Map** Feature uses [Google Maps](https://developers.google.com/maps/) as its interactive **Map**, with a custom style designed through [SnazzyMaps](https://snazzymaps.com/editor/customize). The colour scheme utilises the full scale of the blue monochromatic colour scheme, with all major labels and icons removed. This results in a simple **Map**, leaving only country border lines, country names, and city names when zoomed in.

The Static Background Image used throughout the rest of the site is a static customised version of the interactive **Map**, edited in [Gimp](https://www.gimp.org/), and provides a basic world map outline with the same colour scheme, but with less identifiers.

As the background image and **Map** are based on the same design, this provides a sense of repetition and flow as a user navigates through the website. Transitioning between any page and the **Map** feature produces the effect of the static background coming to life.

![Static Map](https://res.cloudinary.com/bak2k3/image/upload/v1619532793/WYSPA/Static_Map_gpq52b.jpg)
![Interactive Map](https://res.cloudinary.com/bak2k3/image/upload/v1619532793/WYSPA/Dynamic_Map_eyc4tt.jpg)

#### Opacity

The project heavily relies on opacity in order to create a blended and cohesive aesthetic. These are either to draw the user’s attention to certain features, or to create a dynamic background colour on which to overlay text. Opacity is utilised in the following elements:

- Header/Footer
- Card Panels (Including Speech Bubbles/Wyspa Content/Wyspa Creation)
- Modals (Opacity is applied to background overlay)
- Sidebar (On medium and below viewports)
- Toasts
- Tooltips

For the Card Panels, border shadows are also used to lift the content off the static background image, providing the content depth.

#### Speech Bubble

Within the **Wyspa** section, comments on individual **Wyspas** are formatted in a similar manner to Card Panels, with the addition of small triangular elements to create the illusion of a **Speech Bubble**. These alternate left and right, depending on the order in which the comments are generated, producing a conversational aesthetic.

![Speech Bubble Example](https://res.cloudinary.com/bak2k3/image/upload/v1619533104/WYSPA/Speech_Bubble_zftk9e.jpg)

#### Z-Axis Control

The layering of content is crucial in **Wyspa**; Z-axis control is implemented on every page in order to appropriately layer content depending on its priority and interactivity. The order of Z-Axis control is as follows, from lowest priority to highest priority:

- Background Image / Google Maps
- Main body element
- Footer
- Header
- Tooltips
- Modals / SideNav
- Toasts

As a result of this, the Header and Footer can always be interacted with when interaction is intended. While the **SideNav** or a **Modal** is active, these take priority and the background content is made unavailable via an overlay. The **Toast** Container is always at the front most layer, yet does not disrupt interactivity with content visible to the user.

---

# Features

## Existing Features

## Future Feature Considerations

---

# Technologies Used

---

# Testing

---

# Deployment

---

# Credits

## Content

## Media

## Code

---

# Acknowledgements

---

# Disclaimer

---
