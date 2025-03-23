Title: Guide for designing better mobile apps typography | by Andrii Zhulidin | UX Collective

Description: Thanks to the rapid development of the Internet over the past decades, typography in interfaces has gone through the main stages of transformation into the digital world. But the design of mobile…


Guide for designing better mobile apps typography
=================================================

Andrii Zhulidin

Thanks to the rapid development of the Internet over the past decades, typography in interfaces has gone through the main stages of transformation into the digital world. But the design of mobile apps is still a new wave.

In this article, I won’t talk about the general concepts of typography, which can be used both in print and in a digital environment. Instead, I will focus on nuances and hacks that can be used in the typography in mobile apps design.

Because app development is very closely related to operating system features, I will often refer to individual recommendations from Material Design for Android and Human Interface Guidelines for iOs.

So, let’s start.

Minimum Font size
=================

It’s no secret that mobile apps are often used on the go. Add to these limitations associated with the screen size, glare from the sun, various visual impairments among users, not always the best screen quality of smartphones and you will get the first ground rule governing the minimum size for body text.

Apple in its Human Interface Guidelines recommends setting the minimum size for Body text to be 17pt.

Google in Material Design guidelines recommends setting the minimum size for Body text to be 16sp (equal to 16pt in iOs)

It’s necessary to take into account that recommendations from systems are given relative to their default fonts. This is currently the Roboto font for Android and San Francisco and New York fonts for iOs. Minimum font size for other typefaces may vary depending on their characteristics. For example, fonts that have very thin strokes require a larger size for body text.

Also, WCAG 2.0 standards recommend following the minimum font size of 18pt and 14pt for Bold text.

The exception may be the various smaller Captions. But keep in mind that if the user cannot read them, it should not greatly affect the user’s interface comprehensibility.

Recommendations
---------------

Don’t use a font size less than 16pt for the Body text in your app design. A good size for the body text will be in the range from 16pt to 18pt

🤓 Pro-Tip
----------

To make the typography of your app more accessible in iOs, you can apply Dynamic Type Sizes. Using this technology inside your app will allow users who set an increased or decreased font size in the system settings to see the interface of your app according to these settings.

Typography — Visual Design — iOS — Human Interface Guidelines — Apple Developer
-------------------------------------------------------------------------------

### San Francisco (SF) is the system typeface in iOS. The fonts of this typeface are optimized to give your text unmatched…

developer.apple.com

Headline size
=============

In recent years, it has become very popular to use large headings in digital typography. They look contrasted with the main text and become anchor elements on the page.

But you need to be very careful when using large headers in the mobile apps. Often the use of a large size for headings in mobile apps results in the fact that a headline is stretched to 3–4 lines while contains 1 or 2 words per line. Such headers look messy and are hard to read.

Recommendations
---------------

Choose a headline size both contrasting with the body text and fitting on average 2–3 lines.

🤓 Pro-Tip
----------

In some cases, you can use an eyebrow headline to shorten your header.

How You Can Aid User Scanning by Using Eyebrow Headlines
--------------------------------------------------------

### Are you writing your marketing headlines the way users read online? An eye-tracking study found that most users don’t…

uxmovement.com

Contrast
========

Also of the peculiarities of using mobile apps, your background and text contrast ratio is a very important parameter.

Recommendations
---------------

*   Follow WCAG 2.0 Contrast Standards
*   Make sure that the text you place over images has a sufficient contrast
*   Provide two options for placing text on a light and a dark background

🤓 Pro-Tip
----------

Use the Stark plugin (or other same plugins) for Sketch, Adobe XD and Figma or online contrast testing tools to check your text contrast.

System Fonts
============

Currently, for iOs, you can use two system fonts: San Francisco and New York. And the Roboto font is a system font for Android these days.

System fonts will make the design of your app more consistent with the operating system. But using system fonts only will prevent you from getting a unique look for your app.

Recommendations
---------------

The easiest and most common way to add accents and a unique look for the typography of your mobile app is using a system font for the body text and various controls and a non-default font for headings. This combination will always look interesting and fresh.

You can use one of these services below to choose interesting fonts pairs.

Generate font pairing using neural nets
---------------------------------------

### Fontjoy helps designers choose the best font combinations. Mix and match different fonts for the perfect pairing.

fontjoy.com

FontPair helps you pair Google Fonts together.
----------------------------------------------

### Font Pair helps designers pair Google Fonts together. Beautiful Google Font combinations and pairs.

fontpair.co

Fonts In Use — Type at work in the real world.
----------------------------------------------

### A searchable archive of typographic design, indexed by typeface, format, and topic.

fontsinuse.com

🤓 Pro-Tip
----------

Note that the Apple system fonts can only be used in Apple ecosystem products (iOs, macOS, etc). While Google’s Roboto font can be used in any operating system. Keep it in mind when designing one app for both platforms.

Commercial Fonts
================

Sooner or later, many designers find that system or free fonts cannot satisfy their needs for a particular project. And then they face the task of choosing a commercial font. Usually, it is the choice of commercial font that is associated with all the major difficulties.

The price difference between a font for the app use and a desktop or web license will be an unpleasant surprise for you (especially if you didn’t buy this license before). For example, a license for one font style FF DIN for desktop or web costs $ 95, and $ 950 for an app 😱 (price from myfonts.com)

Recommendations
---------------

If you decide to integrate a custom font into the design of your app, you need to consider the following:

*   Learn all the nuances of a license. Font distribution conditions may vary greatly
*   Learn all the technical nuances of a font, such as its readability in small sizes
*   Think about how your product will scale in the future. For example, it may turn out that a selected font doesn’t support Cyrillic
*   Learn whether typeface has a sufficient number of weights or styles.

🤓 Pro-Tip
----------

Search Type Foundries sites directly for fonts for your app. So you can save a large amount on a license and find more interesting styles.

Below, as an example, I give some links of my favorite Type Foundries

Swiss Typefaces
---------------

### We take a look beyond our own work & honor type made by others Read the story 29lt.com sangbleu.com

www.swisstypefaces.com

Commercial Type
---------------

### Trademarks and trade names shown are the property of their respective owners and no endorsement or derogation is…

commercialtype.com

TypeTogether | High quality fonts and custom type design
--------------------------------------------------------

### Unique, high-quality retail typefaces and custom fonts. Our international team of professionals specializes in…

www.type-together.com

Klim Type Foundry · Home
------------------------

### Klim Type Foundry is an independent typeface design studio led by Kris Sowersby and is based in Wellington, New…

klim.co.nz

Colophon Foundry
----------------

### Colophon is an international, award-winning type foundry based in London (UK) and Los Angeles (US). We create, publish…

www.colophon-foundry.org

Pangram Pangram Foundry — Free to Try Quality Fonts and Typefaces
-----------------------------------------------------------------

### Welcome to thePangram Pangram Foundry We provide trend-conscious quality, free to try fonts for designers.Each…

pangrampangram.com

Free fonts
==========

Nowadays, there are more and more good free fonts that are as good as commercial ones. If you are selective in your choice of the free font you might save the project from unnecessary expenses without sacrificing quality or uniqueness in design.

Recommendations
---------------

When choosing a free font, you need to take into account the same nuances as when buying a commercial one. 👆

Below, as an example, I give some links of my favorite free fonts sites and typefaces

Google Fonts
------------

### Making the web more beautiful, fast, and open through great typography

fonts.google.com

Inter font family
-----------------

### Inter started out in late 2016 as an experiment to build a perfectly pixel-fitting font at a specific small size…

rsms.me

Fonts — Fontfabric™
-------------------

### Fontfabric a digital type foundry crafting retail fonts and custom typography for various brands.

www.fontfabric.com

IBM Plex
--------

### IBM Plex™ is our new typeface. It’s global, it’s versatile, and it’s distinctly IBM.

www.ibm.com

Baseline
========

We can often observe a typical situation. Due to the difference in text rendering inside design tools and mobile operating systems, the margins between text blocks and other interface elements may differ visually.

To prevent this from happening, you can consider all margins relative to baseline. This approach will maximize the fit between your layouts and implementation in the app.

\*Android currently doesn’t have full support methods for baseline spacings

Recommendations
---------------

Most likely, using the baseline for all text elements of your interface will be difficult and costly to develop. Therefore, I recommend using this approach for elements where precise accuracy is especially important.

Whitespace and margins
======================

Mobile devices have a very limited screen size, so you will want to fit as much text as possible within a single visible screen.

You don’t have to sacrifice whitespace to do this by reducing margins between text blocks. This will break the hierarchy between different text styles and blocks and will make the text harder to read.

Recommendations
---------------

Compose the layout so that part of the content was above the fold, thereby showing the user that there is more content and encouraging them to scroll.

And don’t forget:

> «Learn the rules like a pro, so you can break them like an artist» Pablo Picasso

Thank you for reading!
