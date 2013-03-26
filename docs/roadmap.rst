=======
Roadmap
=======

Overview
--------

Annotate is a *distributed database of comments and annotations to any web page anywhere*.

We intend to build a system that will capture user comments on a page,
store them where ever the user defines, and enable any visitors to the page 
later on to recover and view the comments.  Optionally we want to place limitations on who can retrieve comments.

Goals
-----

We think that the annotation of web pages without needing permission
from the owner of the server hosting the page *may* be of social
benefit and it *will* be of interest and a learning opportinity for
the developers to take on some web-scale and web technology issues


What major functions will we need to do
=======================================

Bookmarklets
   http://en.wikipedia.org/wiki/Bookmarklet
   We shall develop a bookmarklet (probably quite large!)
   which shall allow a user to click on the bookmark, make a comment 
   on the page and have that stored.
   The bookmarklet will be the prime client side code.



1.a. Capture a comment or other annotation from the web browser user and associate ti with the unique_snippet_reference

2. To connect via JS based RESTful connection, to a given server

3. To retrieve from the server all snippets related to that web page and version.

4. TO ise a distributed index of annotations that will eventually ecome consistent 



Glossary and ideas
==================   

Unique Snippet Reference
   The globally unique location on a particular version of a partiucular
   web page (think wikipedia).  
   I think a URN might work
   usr:http://en.wikipedia.org/wiki/Mars#Search_for_life#This%20most%20often

   We should read  RFC 3986 and http://www.w3.org/Addressing/URL/uri-spec.html​
   carefully.
   http://en.wikipedia.org/wiki/Fragment_identifier - 
   https://developers.google.com/webmasters/ajax-crawling/
  
   so URL + first id before highlighted text + identifer of highlighted text

Annotation
  A combination of USR plus plain text Unicode that is the comment.



Bookmarklet spec
================

* Needs to be a working bookmarklet
* Needs to check if it itself needs updating
* Needs to be able to calculate md5 hashes or similar
* Needs to be able to take some user configuration settings.
* Needs to capture a highlighted area from a user
* Needs to AJAx that highlighted areas Unique SNippet Reference (USR)
   to a annotation storeage server and an annotation index server

* Other stuff



Annotation store
----------------

Initially this will just be a key-value pair of USR and the comment
made.  Its probably all we need.  Any access control should be the
responsbaility of the web server serving the annotation

The annotation-store-reference will be the URL of the storing server plus the
USR plus the md5 of the comment.

It should be feasible to make an annotation on an annotation.


Annotation index
----------------

This is both simple and complex.
The simple part is *non-distributed* - it will be a USR key with a list of
annotation-store-references - that is ::

   xxx: [http://myserver/annotate/12345, http://yourserver/annotate/12345,]


Next steps
----------

Obvfiouslyt expand on this note.

I suggest we create a bookmarklet and get it to fire off snippets of
text to our wsgi server and store them.  the rest is gravy.
