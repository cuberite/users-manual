mcs-book
========

A User's Manual for MCServer


Developers' Area
----------------

This book is structured as individual HTML snippets with metadata header.

A sample input directory structure would be:

    /
    |> 0/
    |   |> 0.1 - Intro.html
    |   |> 0.2 - Notes.html
    |> 1/
    |   |> 1.1 - Downloading.html
    |   |> 1.2 - Running.html

The idea is that the generator, combines the files to form 2 outputs - one standalone HTML page with all sections integrated and internal links, and another with each file (or section?) being a seperate page. At the moment the generator only compiles to a single page, but multiple page is planned.

Here is a small indication of features:

Links to another section are automatically generated like so - `{{Section Number - Text of Link}}`.
