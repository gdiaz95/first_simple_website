# first_simple_website

# Dasmoto's Arts & Crafts

This is an educational project that serves as an introduction to building websites using HTML and CSS. The website represents a fictional arts and crafts store called **Dasmoto's Arts & Crafts**. It showcases basic product information for brushes, frames, and paint, along with images and custom styling.

## Features

- **Simple Structure:** Basic HTML layout with a header and multiple product sections.
- **External Styling:** Uses an external CSS file to style the text, images, and background.
- **Product Showcase:** Three product categories are featured:
  - **Brushes:** Hacksaw Brushes made of high-quality oak.
  - **Frames:** Assorted art frames made from different materials.
  - **Paint:** Clean Finnish Paint available in a variety of colors.
- **Custom Fonts & Colors:** Unique typography and color schemes enhance the design.


## How to View the Website

1. **Clone or Download the Repository:**  
   Get a copy of the project files on your local machine.

2. **Open the HTML File:**  
   Open `index.html` in your preferred web browser to see the website.

## Code Overview

### HTML Overview

- **Header:**  
  The `<div id="header">` contains the main title of the site.  
  _Note: There is an HTML typo in the closing tag (`</hheader>` instead of `</h1>`), which should be fixed for valid HTML._

- **Products:**  
  Each product is wrapped in a `<div class="product">` and includes:
  - A product category heading (`<h2>`).
  - An image representing the product.
  - A subheading (`<h3>`) and description (`<p>`).
  - Price information wrapped in a `<div class="price">`.  
  _Note: Nesting a `<div>` inside a `<p>` is invalid HTML. Consider restructuring the markup for better semantic correctness._


## CSS Overview

The external CSS file (`style.css`) is used to control the overall look and feel of the website. Here's a general overview of the CSS structure:

- **Global Styles:**  
  Sets foundational styles such as fonts, colors, and sizes that are applied consistently across the site.

- **Header and Title Styling:**  
  Special rules target the header and title elements to create a strong, visually appealing introduction. For example, the title is styled with a large, bold font and a custom background image.

- **Section-Specific Styles:**  
  Each product section (Brushes, Frames, Paint) is given a distinct background color and style to differentiate the content areas and enhance visual hierarchy.

- **Element Targeting:**  
  The stylesheet uses IDs and classes to apply tailored styles to specific elements, making the design modular and easier to maintain.

- **Scalability and Flexibility:**  
  The CSS is organized to allow for future enhancements, such as responsive design adjustments or additional styling rules, ensuring that the website can evolve as needed.


This project is for educational purposes only. Feel free to modify, expand, and use it as a starting point for your own web development projects.
