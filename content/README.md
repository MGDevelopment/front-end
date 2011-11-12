Content Generation for Tematika.com App
=======================================

Template Guide
--------------

To generate a page (text output) a template is rendered with a context and
parameters. The template will tipically inherit the basic structure from a
parent template and will also include fragments common to other templates.

The pages are PAGE entities. This entities must be generated separately.

### Basic Elements of Pages

### URLs in Templates

Template Data (Parameters)
--------------------------

The generator renders pages with the corresponding set of parameters. The
dasta query to obtain those parameters is closely related to the template.

### Example: Home Page


Templates
---------

### page.html (base)

    Description:   Basic structure for an HTML page
    Blocks:
        content_type:     basic content type defined
        page_css:         global stylesheets
        ie_fix:           Internet Explorer fix stylesheet
        head_extra:       placeholder for extra html head elements
        body_top:         start of body section
        canvas_top:       start of canvas section
        canvas_messages:  start of canvas section
        canvas_content:   start of canvas section
        canvas_bottom:    end of canvas section
        body_bottom:      end of body section (javascript)
    References:  page.css, cart.css, section.css, section_start.css,
                 gallery.css, last_visited.css
    Parameters:  section:(home|books|movies|music|games|quid|extra|*)

### Home

    Description: homepage for the site
    Extends:     page.html
    Includes:    index.css, home/bottom.html, home/showcase.js, home/bottom.js
    Fragments:   top.html, messages.html, product_gallery.html,
                 comments.html, last_visited.html, right_menu.html, extra.html
    Parameters:  section:home

### Section

    Description: sections and sub-sections
    Extends:     page.html
    References:  section.css
    Parameters:  

### static.html (base)

    Description: Base template for static content pages
    Extends:     page.html
    References:  site.css

### Static Help

    Description: help for the site
    Extends:     static.html
    References:  static.css

### script.js

    Description: help for the site
    Extends:     static.html

### home/showcase.js

    Description: gallery navigation data for dynamic scrolling
    Extends:     script.js
    Requires:    (jquery)

### comments.js

    Description: comments for a product, section or page
    Extends:     script.js
    Requires:    


Styles
------

The style definitions for pages.

### css/page.css

    Description:   styles common to all pages derived from base template

### css/cart.css

    Description:   styles for shopping cart fragment

### css/section.css

    Description:   styles for sections

### css/section_index.css

    Description:   styles homepage sections (?)

### css/gallery.css

    Description:   styles for product gallery

### css/last_visited.css

    Description:   styles for last visited products panel

### css/home/index.css

    Description:   styles for the home page

### css/section/section.css

    Description:   styles for section pages


Fragments
---------

Fragments are standalone parts of a page, usually components. These templates
do not extend from base page templates and should not reference external
resources directly (if possible).

### fragments/scripts.html

    Description:   basic scripts (base template)

### fragments/analytics.html

    Description:   Google analytics snippet

### fragments/product_gallery.html

    Description: gallery of products

### fragments/canvas_top.html

    Description:   common top (base template)
                   includes search, cart

### fragments/messages.html

    Description:   global messages to the user (base template)

### fragments/canvas_footer.html

    Description:   common page footer (base template)

### fragments/canvas_footer.html

    Description:   generic footer of the canvas

