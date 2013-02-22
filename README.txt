========
Annotate
========

The world is changing ... again. Don't you wish it would stop doing that?

I would like to create a *distributed annotation infrastructure*

1. Javascript runs on a web page in a browser.

2. The user can comment on that page

3. The comment is stored on an arbitrary, user defined location, but that
   must be a viable HTTP aware store - ie PUT POST.
   For example the text of the comment is stored on their github repo "annotations".

4. Then the js client also posts a hash of the URL and the location of the comment to an indexing service

5. the indexing service is the infrastructure - and it is distributed over multiple domains.

6. the indexing service is relatively simple - for a given URL / URL hash it returns a json list of URLS where comments about that URL can be found.

7. there is a protocol to share and update (and even mark as down) between indexing services

8. the next time the page is opened and the "annotate" javscript is run, it will ask the indexing service for its results for the URL - and then fetch and display those annotations.

