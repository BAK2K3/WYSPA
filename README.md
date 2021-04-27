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

The project was developed using **HTML** , **CSS** , **JavaScript** , and **Python** , and utilises a NoSQL document-based database via **MongoDB**.

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
- Allow a user to comment on any **Wyspa** , and delete any comments they have made.
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
- When creating a **Wyspa** , the following information will be recorded, and for the following purposes:
  - **Author:** This will be pre-populated by the server, allowing backend verification of **Wyspa** ownership.
  - **Message:** This will be provided by the user, in free-text form. This will be the message the user would like to communicate, and therefore the message other users are able to read.
  - **Location:** This will be provided in a verbose manner by the user (i.e London), converted to Lat-Long (51.500153° N, -0.1262362° E), and scrambled (N/E +-0.1). This will be used to position the **Wyspa** on the **Map**.
  - **Mood:** This will be chosen by the user, out of choices presented to them. This will be used to colour the **Wyspa** marker on the **Map**.
  - **Expiry Date:** This will be set by the user. This will depict when the document removed from the database.
  - **Comments:** This is an entry which all logged in users will be able to contribute to; these comments will be displayed on the individual **Wyspa** page.
  - **Listens :** This is an entry which will log the users who have listened to a **Wyspa** ; this will be used to prevent any single user listening to a **Wyspa** more than once.
  - **Listen_Count:** This is an entry which counts the total amount of **Listens** contained within a whisper. This will be used for both sorting the database entries for the **Map** , depicting the size of the **Map** marker, and for displaying the amount of **Listens** a **Wyspa** has on the individual **Wyspa** page and profile page.

## Structure

## Skeleton

## Surface

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
