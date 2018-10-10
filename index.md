---
layout: layout
title: "About"
---

<!-- You can edit this whole page, remove it, or use it as basis for any non-post pages you have. -->
<section class="content">

# The {{ site.title }}, {{ site.chapter }}

To keep up to date - join the mailing list.  To subscribe, email
[Majordomo@lists.bham.ac.uk](Majordomo@lists.bham.ac.uk) with a "plain text"
(not HTML) email, having the following text as the body of the email:
`subscribe hacker-within`

Please make sure there is a new line at the end.

If you have any problems subscribing then just email
[bear-software@contacts.bham.ac.uk](bear-software@contacts.bham.ac.uk) and we
can subscribe you.

After following those instructions, you should be able to [mail the
list](mailto:hacker-within@lists.bham.ac.uk).

<b>Summer 2018 is here!</b>

<ul class="listing">
<li>
<span>Summer 2018</span><a href="{{ site.url }}/upcoming.html">Upcoming Topics</a>
</li>
  {% assign upcoming = site.posts | where: "category" , "upcoming" %}
  {% for post in upcoming reversed %}
    {% if forloop.first %}
	<li style="text-indent: 2em;">
		<span>{{ post.date | date: "%B %e, %Y" }}</span> Next topic: <a href="{{ site.url }}{{ post.url }}">{{ post.title }}</a>
	</li>
    {% endif %}
  {% endfor %}
<li>
<span>Previous</span><a href="{{ site.url }}/previous.html">Previous Topics</a>
</li>
</ul>

Most work in academia makes use of computing to analyze data.   Over the last decade there has been an explosion in the number, range and flexibility of software for data analysis.   With so much choice, how do we choose the right tools?  In the face of such complexity, how do we learn to work efficiently and simply, so we can share our work, and properly report our analyses?   We need to find - The Hacker Within.

## What:

The Hacker Within is a monthly peer learning group for sharing skills and best practices for research computing and data science. In these friendly sessions, peers at all levels of experience share topics useful in our data analysis and software development workflows.

This meeting would be a great venue for introducing new libraries, showing off useful features of a data processing/analysis/visualisation library or programming language you’re using, or bringing up a computational problem you’re having.

We plan to have regular talks where we present to each other on useful and important tools and practices for effective computing.  We aim to build a community to support the spread of these tools and practices across the University and beyond.

## Why:

We started this group because we know that using the right tools reduces error and makes us more productive and better at collaborating.  Technology changes fast, and finding the right tool or process for a particular task can be difficult; by presenting the tools that we use and sharing our expertise, we can all learn new ways of working more effectively.


## Who:

Anyone interested in how to learn and do things by programming computers is welcome to come to our meetings. You don’t need to be affiliated with the University of Birmingham and you don’t need to come to every meeting. There is no set of prerequisites, although we frequently use the command line, Python, R, version control and Jupyter notebooks.

We decide the topics by negotiation in the meeting and on our mailing list, but the main staff contacts are:

* Matthew Brett [m.brett@bham.ac.uk](m.brett@bham.ac.uk) (College of Life and
  Environmental Sciences);
* Research Software Group [bear-software@contacts.bham.ac.uk](bear-software@contacts.bham.ac.uk) (IT Services);
* Debbie Carter [d.j.carter@bham.ac.uk](d.j.carter@bham.ac.uk) (IT Services).

## Where:

The meetings move around quite a bit.  Please see the [upcoming meetings
page]({{ site.baseurl }}{% link upcoming.md %}) for the location of the next
meeting.

## When:

We will meet on the third Monday of each month, to start off with, at a time /
venue that may shift from meeting to meeting (see above).

<a href="http://twitter.com/share" class="twitter-share-button" data-count="none" data-via="{{ site.twitter }}">Tweet</a>
<a href="http://twitter.com/{{ site.twitter }}" class="twitter-follow-button" data-show-count="false">Follow @{{ site.twitter }}</a>
<script src="http://platform.twitter.com/widgets.js" type="text/javascript"></script>
</section>

## Talk videos

Have a look at the [Hacker Within Canvas
course](https://canvas.bham.ac.uk/courses/33864) for links to talk videos, if
they are available.
