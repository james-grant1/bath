---
layout: layout
title: "Upcoming Topics"
---

<section class="content">

Upcoming Topics
===============

**Summer 2018**

See below for upcoming meetings.

If you would like to volunteer as a speaker, please email Matthew Brett (m.brett@bham.ac.uk).

<ul class="listing">
  {% assign upcoming = site.posts | where: "category" , "upcoming" %}
  {% for post in upcoming reversed %}
  <li>
  <span>{{ post.date | date: "%B %e, %Y" }}</span> <a href="{{ site.url }}{{ post.url }}">{{ post.title }}</a>
  </li>
  {% endfor %}
</ul>
</section>
