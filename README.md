# The Hacker Within

This is the website that keeps the blog posts for each THW meeting at the
University of Birmingham, UK. The rendered website can be found
[here](http://thehackerwithin.github.io/UoB).

## How To Be The Speaker

One very common reason that folks want to contribute to this repository is
that they are planning to give the main skill sharing session for some week at
THW. To be the speaker, you'll need to sign up, set up, show up, and speak up.

### Sign Up

We try to decide the semester meeting topics at the beginning of the session. 
So, if you have a topic you'd like to talk about, please suggest it over the 
listhost before the semester starts or show up to the first meeting of the 
semester.

### Set Up

We love sessions that have example code! If you have example code, please
place it in an appropriately named directory in the master branch of this
GitHub repository. Make a [pull
request](https://help.github.com/articles/creating-a-pull-request/) or push
your branch to the
[thehackerwithin/UoB](http://github.com/thehackerwithin/UoB) fork. If you know
how to do that, please go right ahead. If you aren't sure about forks and pull
requests, here are some detailed instructions:

#### Getting ready to edit the Hacker Within pages

Use these instructions to get started editing the web pages, adding posts, or
adding other content to Hacker Within repository, such as example code.

Let's say that your Github username is `YOURUSERNAME`.

1.  Go to the UoB Hacker Within repository at:
    [https://github.com/thehackerwithin/UoB](https://github.com/thehackerwithin/UoB).
1.  Press the Fork button ([you'll need a github
    account](https://github.com/signup)).
3.  In your terminal, execute `git clone
    https://github.com/thehackerwithin/UoB.git`
4.  Enter the new directory with `cd UoB`
5.  Add a Git remote for your fork with `git remote add YOURUSERNAME
    https://github.com/YOURUSERNAME/UoB.git`
6.  Fetch information about your fork with `git fetch YOURUSERNAME`
7.  Start a new branch for your edits with `git branch --no-track
    name-of-thing-im-working-on origin/master`.  For example, if you are adding a tutorial
    on Python, you might do `git branch --no-track add-python-tutorial origin/master`.
8.  Check out your new branch with something like `git checkout
    add-python-tutorial` (where `add-python-tutorial` is the name you used in
    the `git branch` command).

Now you are ready to edit these pages.

#### Uploading Example Code

Let's say you have some code you'd like to share for a tutorial.  Say the code
file you want to share is called `my_program.py`.

Follow the instructions above to get the website code and start working in a
new branch.

7. Check what branch you're in `git branch`.  You should be in your new
   branch, that you made from the instructions above.
8. Move your code file to an appropriately named directory.
   Browse the root directory of the repository for directories other people
   have used to store code. Make a new directory if you prefer. Say you have
   chosen the directory `example_code`.  Move your code file to the directory
   you have chosen, e.g.: `mv my_program.py example_code`.
9. Add the files to the repo, e.g. `git add example_code/my_program.py`.
10. Commit the file(s). `git commit -am "I added files for the tutorial on my
    topic.."`
11. Git push to your remote with e.g. `git push YOURUSERNAME
    add-python-tutorial` where YOURUSERNAME is your Github user name, and
    `add-python-tutorial` is the name of your branch (see above).
12. Navigate in your browser to https://github.com/YOURUSERNAME/UoB and press
    the pull request button to ask us to merge your changes into the main website.

Now you're done adding code example files! You'll need to edit the post related
to your talk.

#### Add Your Tutorial to the Site

Rather than preparing a slideshow, please consider leading as interactive a
session as possible. This is often done by leading the audience through
whatever code examples you have merged to the master branch, using the
procedure above. Supportive text can be added to the markdown file holding the
blog post for your talk. To add text to that file and to edit your bio. You
may need to both create and modify the post.

First, if you haven't done so already, follow the instructions above in
"Getting ready to edit the Hacker Within pages".

Then, create and modify the post as in the sections below.

#### Creating a Post

In the directory that you just cloned (UoB), you'll notice a `_posts`
directory. The post related to the day and topic of your talk may already
exist. If so, skip ahead to "Modifying a Post."

If not, you'll need to create it. Thankfully, you'll also notice a `_drafts`
directory. In the drafts directory, you'll find an empty template for meeting
minutes `YYYY-MM-DD-subject.markdown`. If you're preparing for a special
holiday meeting on March 1, 2015, then the proper name for the file you're
creating should be something like 2015-03-01-katysbirthday.markdown.

You post is in [Github
Markdown](https://help.github.com/articles/basic-writing-and-formatting-syntax)
format - see that page for ways of marking up your text.

- In the UoB directory, execute `cp _drafts/YYYY-MM-DD-subject.markdown
  _posts/2015-03-01-katysbirthday.markdown`
- Then, edit that file as you see fit.
- Add that file to the repository `git add _posts/2015-03-01-katysbirthday.markdown`
- Commit it: `git commit -am "adds a post for march 1"`
- Push it to your fork as above with something like `git push YOURUSERNAME
  add-python-tutorial -u` where `YOURUSERNAME` is your Github user name, and
  `add-python-tutorial` is the branch name you chose above.
- Check how your new post looks by going to https://YOURUSERNAME.github.io/UoB
  in your browser.  Navigate to your new post.  Some of the page styling will
  be broken, because your fork is not directly attached to the main Hacker
  Within website, but check the content looks right for the post.
- Iterate on this until you are happy - edit, push, review.
- When you are ready, make a pull request to have your edits merged into the
  main website.  To do this, navigate in your browser to
  https://github.com/YOURUSERNAME/UoB and press the pull request button to ask
  us to merge your changes into the main website.

#### Modifying a Post

This is very similar to creating a post, for which, see the section above.
The only difference in the process is that, when you are editing a file, you
do not need to do the initial copy to create your new file.

#### Build the site locally

If you'd like to test the post before pushing or making a PR, you can build
the site locally:

- Install Jekyll: `gem install jekyll`
- Run the jekyll server: `jekyll --server`

You should have a server up and running locally at <http://localhost:4000>.

### Show Up

Please arrive 10-15 minutes before the start time so that you can set up your
computer and test out the projector. Please figure out how to zoom in on text
that might be too small from the back. Try command-plus-plus in the terminal
and other applications. If you're an emacs user on a mac, you may need
[accessibility zoom enabled.](https://www.apple.com/accessibility/osx/).

### Speak Up

The Hacker Within isn't a class and no one is required to attend. We show up
to have fun and to learn. Hopefully, your tutorial will teach something
**useful** in a way that is **enjoyable.** To do this, please consider
bringing your A-game. That is, find the enthusiastic tinkering problem-solver
inside yourself (The Hacker Within yourself) and bring that version of
yourself to share that enthusiasm with us. Enthusiasm is infectious!

## About this website.

It's all based on something @katyhuff forked. It's called Left.  It uses
[Jekyll](https://jekyllrb.com/).  It was extracted from
[zachholman.com](http://zachholman.com/). That is, we use Left to lay out this
Jekyll.

Left is a clean, whitespace-happy layout for
[Jekyll](https://github.com/mojombo/jekyll).

### Content Licensing

The content of this blog is liberally licensed to The Hacker Within and to the
individual authors of each blog post.  Additionally, you're welcome to reshare
the content with attribution, because it is [CC-BY-3.0
licensed](http://creativecommons.org/licenses/by/3.0/)

Except where otherwise noted, content on this site is licensed under a Creative
Commons Attribution 3.0 Unported License. Copyright 2013-2015 The Hacker
Within.

Please attribute any work with a link to its original appearance on this
domain (i.e., "from The Hacker Within's blog entry 'Segmentation Fault' at
[thehackerwithin.github.io/blog/posts/segmentation-fault](thehackerwithin.github.io/blog/posts/segmentation-fault)
").

### Left Licensing

The Left layout is [MIT](https://github.com/holman/left/blob/master/LICENSE) with no
added caveats. Left is the work of Zach Holman [@holman](https://twitter.com/holman).

![Left](http://cl.ly/image/3S2r1p2C0E2B/content)

