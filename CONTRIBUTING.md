# Contributing to odd-even-game
Thanks for taking the time to contribute!
because we need volunteer developers to help this project come to fruition.

### Did you find a bug?
Ensure the bug was not already reported by searching on GitHub under Issues.</br>
If you're unable to find an open issue addressing the problem, open a new one.
be sure to follow according to issue template

### Did you write a patch that fixes a bug?

Open a new GitHub pull request with the patch.
Ensure the PR description clearly describes the problem and solution. 
Include the relevant issue number if applicable and it follows the template

### Do you intend to add a new feature or change an existing one?

Submitting changes
Please send a GitHub Pull Request to DIC with a clear list of what you've done (read more about pull requests). When you send a pull request. We can always use more test coverage. Please follow our Coding Guidelines (below) and make sure all of your commits are atomic (one feature per commit).</br></br>

Always write a clear log message for your commits. One-line messages are fine for small changes, but bigger changes should look like this:

```git
$ git commit -m "A brief summary of the commit"
```
# Coding Guidelines

All new code **must** follow the following coding guidelines. \
If you make changes in a file that still uses another coding style, make sure that you follow these guidelines for your changes. \
For programming languages other than C++ (e.g. JavaScript) used in this repository and submodules, unless otherwise specified, coding guidelines listed here applies as much as possible.

**Note:** I will not take your head if you forget and use another style. However, most probably the request will be delayed until you fix your coding style. \
**Note 2:** You can use the `Astyle` program/tool to clean up any source file.

## Table Of Contents

* [1. New lines &amp; curly braces](#1-new-lines--curly-braces)
  * [a. Function blocks, class/struct definitions, namespaces](#a-function-blocks-classstruct-definitions-namespaces)
  * [b. If-else statements](#c-if-else-statements)
* [2. Indentation](#2-indentation)
* [3. File encoding and line endings](#3-file-encoding-and-line-endings)
* [4. Names](#4-names)
  * [b. Variable names](#b-variable-names)
* [5. Git commit message](#8-git-commit-message)
* [6. Not covered above](#9-not-covered-above)

---

## 1. New lines & curly braces

### a. Function blocks, class/struct definitions, namespaces

```python
def myFunction(a):
	// code


def myFunction() // empty body
```

### b. Other code blocks

```python
if condition:
    // code

for i in list:
    // code

```

### c. If-else statements

```python
if condition:
    // code
elif condition:
    // code
else:
    // code
```

## 2. Indentation

2 spaces.

## 3. File encoding and line endings

UTF-8 and Unix-like line ending (LF). Unless some platform specific files need other encodings/line endings.

## 4. Names

use an Underscore (_) for long names
it is optional to start with Upper case letter
eg- Expection_handling, manly_name

### a. Variable names

it is optional to start Variable names with upper case letter.
but it is a must to use an underscore when naming more than one word

```python
whichShape = 1;
errorMessage = "This is an error;
```
## 5. Git commit message

1. Limit the subject line to 50 characters. Subject should contain only the very essence of the changes (you should avoid extra details and internals)
2. Separate subject from body with a blank line
3. Capitalize the subject line
4. Do not end the subject line with a period
5. Use the imperative mood in the subject line (it's like you're ordering the program to do something (e.g. "Don't create temporary substrings")
6. Use the body to explain what and why vs. how
7. If commit fixes a reported issue, mention it in the message body (e.g. `Closes #4.`)

## 6. Not covered above

If something isn't covered above, just follow the same style the file you are editing has.
*This guide is not exhaustive and the style for a particular piece of code not specified here will be determined by project members on code review.*
Credits to qbit_torrent's code guildlines https://github.com/qbittorrent/qBittorrent