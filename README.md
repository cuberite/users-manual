mcs-book
========

A User's Manual for MCServer


Developers' Area
----------------

This book is structured as individual HTML snippets with metadata header.

A sample input directory structure would be:

    /
    |-0/
    |  |-1 (intro).html
    |  |-2 (notes).html
    |-1/
    |  |-1 (downloading).html
    |  |-2 (running).html

The idea is that a generator (to be written, perhaps Lua?), combines the files to form 2 outputs - one standalone HTML page with all sections integrated and internal links, and another with each file (or section?) being a seperate page.

This generator would have to include the following features:

 * Link generation is different for the different outputs (example.html and #example).
 * Inclusion of header and footer for each page and using metadata (different for standalone).
 * Integration of JS and CSS assets into the source for the standalone file so it can be run offline.
 * Generation of table of contents.

The metadata is proposed to be a simple YAML document at the head of each HTMl file, and is seperated from the body by a seperator (`~~~~` maybe?). The YAML document would look something like this:

    section: 1.1
    title: Downloading MCServer
    description: How to download MCServer.