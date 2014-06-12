mcs-book
========

A User's Manual for MCServer

There is an automatically updated version of the manual at [mcs-book.nfshost.com](http://mcs-book.nfshost.com), which updates every time a commit is pushed to this repository.


Developers' Area
----------------

This book is structured as individual HTML snippets for each chapter. The filename describes the section number and also the name of the section, seperated by " - ".

A sample input directory structure would be:

    /
    |> 0 - Introduction/
    |   |> 1 - Intro.html
    |   |> 2 - Notes.html
    |> 1 - Setting Up/
    |   |> 1 - Downloading.html
    |   |> 2 - Running.html

The idea is that the generator, combines the files to form 2 outputs - one standalone HTML page with all sections integrated and internal links, and another with each file (or section?) being a seperate page. At the moment the generator only compiles to a single page, but multiple page is planned.

Here is a guide to writing:

Links to another section are automatically generated like so - `{{Section Number - Text of Link}}`.

Here is a list of semantically correct and styled HTML elements for specific purposes:

 * `<p>` For Paragraphs
 * `<h4>` For Headings
 * `<aside class="infobox">` For information tangentially related to the content.
 * `<aside class="warnbox">` For a warning related to the content.
 * `<figure class="codebox">` For a code sample, with nested `<pre>` and `<code>` tags. Optionally with a `<figcaption>` for a caption.
 * `<figure class="imgbox"` For an image/screenshot. Optionally with a `<figcaption>` for a caption.
