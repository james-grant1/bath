---
layout: post
title: Testing and continuous integration
comments: true
category: posts
tags: meeting <+ tags +>
---

* when: Monday 20 July, 1-2.30pm.
* where: Muirhead 112
* what: Testing and continuous integration

## Stream of talk

Try [this
link](https://bham.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=7ee182bc-003d-4394-9b6b-a94200c81d6b)

## Getting set up

Make sure you have these two things on your computer:

*   A Python distribution.  If you haven't got one already, and particularly if
    you are on Windows, I recommend [the Anaconda distribution
    installer](https://www.anaconda.com/distribution/).  Choose the Python 3.6
    version, not the Python 2.7 version.  You do not need to install VSCode,
    when that option comes up.
*   [Git version control
    software](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
    I suggest you choose the option to use the Nano editor by default, instead
    of Vim (I use Vim, but if you are not used to it, it's a terrible choice
    for getting started as quickly as possible).

## Improving as a programmer

*   Does an academic need to be a good programmer?
*   What is a good programmer?

    * [Teach yourself programming in 10
      years](https://www.norvig.com/21-days.html).
    * [Winning a programming competition is not what you
      need](https://youtu.be/DdmyUZCl75s).

## Preparing to use Github

*   Go to [https://github.com](https://github.com)
*   If you haven't got an account, make one now.  Use your `.bham.ac.uk`
    address, it gives you access to some education features (if you ask for
    them).
*   Navigate to
    [https://github.com/matthew-brett/play-poker](https://github.com/matthew-brett/play-poker)
*   Click on the "Fork" button just below the top right of the screen.  Wait
    for a bit.  You should now be looking at your own *fork* of my
    `play-poker` repository.
*   Select the URL of your new forked repository from the URL bar, and copy
    it.  The URL will be of form
    ``https://github.com/your-user-name/play-poker``.
*   Open the terminal (Cmd-spacebar "Terminal" on Mac, Start key "git bash"
    on Windows)
*   Change directory to the Desktop:

    ```
    cd Desktop
    ```

*   Clone your new repository with the following at the terminal:

    ```
    git clone https://github.com/your-user-name/play-poker
    ```

    where `your-user-name` is your Github username.

*   Change directory to the repository directory.

    ```
    cd play-poker
    ```

## Ready for poker

*   If you're on Windows - press the "Start key" then type "Spyder" (no
    quotes).  Press return.  The Spyder editor should start.  Click on File,
    select Open, navigate to the Desktop `play-poker` folder, and select
    `poker.py`. Click the green run (play) icon to run the file.
*   On Mac, in Terminal.app, check you are in the `Desktop/play-poker`
    directory with:

    ```
    pwd
    ```

    Now run your `poker.py` script with:

    ```
    python poker.py
    ```

*   You should see the printout of "Running tests", and "Finished".
    Congratulations, you are all set for some test-driven development.

## Getting more interactive

When we are writing tests, we often want to experiment with code, and look at
variables.  The best tool to do this is the [IPython](https://ipython.org)
interactive Python prompt.

*    Windows: if you are using Spyder, you already have this - it's the bottom
     right pane in your Spyder window arrangement.
*    Mac: first check you have IPython installed by typing:

     ```
     python -m IPython --version
     ```

     If this gives an error, type:

     ```
     pip install --user ipython
     ```

     Now type:

     ```
     python -m IPython
     ```

Now you will have a prompt of form `In [1]: `.  Type `2 + 3` and press return.
This should execute and return 5.

## Start with a failing test

This is the key element of test first developement - write a failing test,
then fix it.

*   Edit `poker.py`.  In Windows, you probably already have Spyder open.  On
    Mac, start a new tab in Terminal, with the Shell menu, New Tab option.  In
    this new tab, type `nano poker.py`.
*   We are going to start by generating a new desk of cards.  To do this, we
    imagine a `make_new_deck` function, that returns a fresh unshuffled deck
    of cards.  We start by imagining what that should return.  It should
    probably be something that has 52 cards in it, at least.   Imagining
    further, replace `test_new_deck` like this

    ```python
    def test_new_deck():
        # We will test the `make_new_deck` function
        deck = make_new_deck()
        assert len(deck) == 52
    ```

    Note the four space indentation for the stuff inside the function.

    Now run the file - Windws: click Run / Play in Spyder; Mac: switch back to
    the original tab, running IPython and run `run poker.py`.

    It fails, because we haven't written `make_new_deck` yet.

*   Put a new function called `make_new_deck` into `poker.py`.  It returns 52
    None values.

    ```python
    def make_new_deck():
        return [None] * 52
    ```

    Run the tests again.  They pass.

## Working out the design by testing

Now we have 52 "cards", but the cards are Python's special `None` value.  We
have to decide what a card should be.

Let's say one card is a string, of form "7 of Spades" or "Jack of Hearts".

Let's also say that a new deck will be not-shuffled, so the first card will be
the 2 of Hearts.  Expand your test function like this:

```python
def test_new_deck():
    # We will test the `make_new_deck` function
    deck = make_new_deck()
    assert len(deck) == 52
    first_card = deck[0]
    assert first_card == "2 of Hearts"
```

Run the file.  It fails because the first card is currently `None`.

## Experimenting as you go

Now we will write a proper function to generate the new deck of cards.

To do this, we would like to try various things at the interactive IPython
prompt.

Try typing this at the IPython prompt:

```python
'2 3 4 5 6 7 8 9 10 Jack Queen King Ace'.split()
```

You should see a length 13 list with the card values.

Try this:

```python
'Hearts Diamonds Clubs Spades'.split()
```

This should be a four element list of suit names.

We can put these at the top of our `poker.py` file, like this:

```python
VALUES = '2 3 4 5 6 7 8 9 10 Jack Queen King Ace'.split()
SUITS = 'Hearts Diamonds Clubs Spades'.split()
```

Run the file from IPython with:

```
run poker.py
```

Now check the variables look right by showing their contents.  At the IPython
prompt:


```python
VALUES
```

and

```python
SUITS
```

Let's try making the first card in IPython.

```python
VALUES[0] + ' of ' + SUITS[0]
```

To make the full deck of cards, we cycle through all the suits, then all the
values, and combine the value with the suit, to make 52 cards:

```python
def make_new_deck():
    cards = []
    for suit in SUITS:
        for value in VALUES:
            card = value + ' of ' + suit
            cards.append(card)
    return cards
```

Run the tests.  Do they pass?

## Extend the tests

We just did a lot of code, and our tests only test the first card.  We should
add some more tests to check our `make_new_deck` function is doing the right
thing.

Add these lines to your `test_new_deck` function.  Be careful to keep the same
indentation as the lines above:

```python
    assert deck[12] == "Ace of Hearts"
    assert deck[13] == "2 of Diamonds"
    assert deck[26] == "2 of Clubs"
    assert deck[51] == "Ace of Spades"
```

## Making a poker hand

To make a poker hand, we shuffle the cards, and then give out five cards from
the shuffled deck.  What would a shuffled deck look like?

First we write a failing test.

A shuffled deck will virtually never have the same order as a fresh deck.
Let's put that in as a test, expecting it to fail one time in 52 x 51 x 50 x
49 etc, and that is basically never.

```python
def test_shuffled():
    ordered_deck = make_new_deck()
    to_shuffle = make_new_deck()
    shuffled_deck = shuffled(to_shuffle)
    assert shuffled_deck != ordered_deck
```

You'll also need to add this function call to your `if __name__` block:

```python
if __name__ == "__main__":
    print("Running tests")
    test_new_deck()
    test_shuffled()
    print("Finished")
```

Run the file.  It fails.  We are going to fix it.

First consider this really bad shuffle function:

```python
def shuffled(deck):
    # A really bad shuffle function
    re_ordered = deck.copy()
    # Reverse the order
    re_ordered.reverse()
    return re_ordered
```

That would always return a deck with the 'Ace of Spades' first and the '2 of
Hearts' last.  But our test would still pass.  Put that function into
`poker.py`.

Run the tests - they pass.  Oops.  We need to test more.

`shuffled` needs to do more than return something different from an ordered
deck.  It needs to return something different each time.

We add some new lines to `test_shuffled` that will do 1000 shuffles, and makes
sure each one is different.  We take the opportunity to fold in the check that
the deck is not ordered.

```python
def test_shuffled():
    decks = []
    # Put an ordered deck into the list of decks
    decks.append(make_new_deck())
    for i in range(1000):
        deck = make_new_deck()
        shuffled_deck = shuffled(deck)
        # Compare this deck to all previous ones.  Do any match?
        assert shuffled_deck not in decks
        decks.append(shuffled_deck)
```

Run the tests.  They should fail.

How to make this work correctly?  Let's experiment in IPython:

```python
import random
```

Use tab completion to explore the `random` module, by typing `random.` (notice
appended period) and then pressing tab.  We find `random.shuffle`.  Here is a
not-shuffled deck:

```python
deck = make_new_deck()
# First 10 cards
deck[:10]
```

Now shuffle:

```python
random.shuffle(deck)
# New order shows in first 10 cards
deck[:10]
```

We will use `random.shuffle` for our `shuffled` function.


Type `import random` at the top of `poker.py`.  Replace the bad version of
`shuffled` with this version:

```python
def shuffled(deck):
    # A proper shuffle function
    re_ordered = deck.copy()
    random.shuffle(re_ordered)
    return re_ordered
```

Run the tests.  They should pass.

## A better way to run the tests

[pytest](https://pytest.readthedocs.io) is a Python package that makes it
easier to write tests and run them.

So far we've been running the tests by running our Python module `poker.py`.
We had to add a call to our test functions in the `if __name__` block.

Pytest finds tests in `.py` files automatically, and then runs the tests.

If you installed Anaconda, you have Pytest installed already.

If not, open a terminal window, and type:

```
python -m pytest --version
```

If you get `No module named pytest`, then:

```
pip install --user pytest
```

Now check you can run the tests with:

```
python -m pytest poker.py
```

This is an efficient way to find tests and run them.

## Commit your changes

Open Git (go back to git bash in Windows; open a new Terminal tab on Mac).

First check that Git knows your name and email.  Type:

```
git config user.name
```

It should show your name.  If it doesn't show anything, type:

```
git config user.name "Your Name"
```

Now check:

```
git config user.email
```

If that shows nothing:

```
git config user.email "my.name@bham.ac.uk"
```

Now you are ready to prepare and make a new commit.  Type:

```
git status
```

You should see that `poker.py` has been modified.

Put it in Git's *staging area* ready for the next commit:

```
git add poker.py
```

Use `git status` to show that the changes in `poker.py` are now in the
"Changes to be committed".

Do the commit with:

```
git commit
```

Your text editor should open for you to type a commit message.  Save the
message to finish the commit.

## Continuous integration

Notice the
[.travis.yml](https://github.com/matthew-brett/play-poker/blob/master/.travis.yml)
file in the repository.  This is a configuration file for the free
[Travis-CI](https://www.travis-ci.com) continuous integration service.

Now we ask Travis-CI to run our tests each time we do a new commit to the
repository.

Go to the [https://www.travis-ci.com](https://www.travis-ci.com) front page.
Click on the green button "Sign up with Github".  Click on the green button at
the bottom of the page: "Authorize travis-pro". Select the `play-poker`
repository.

All done.  The next time you send a commit to the `play-poker` repository,
Travis-CI will run the tests for you.

Let's do that:

```
git push origin master --set-upstream
```

Now go to the [https://travis-ci.com](https://travis-ci.com) site. You should
see that Travis-CI is running or has run your tests for you.
