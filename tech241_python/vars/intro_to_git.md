# Intro to Git

The Definition of Git is:

![Definition of Git](C:\Users\ashle\OneDrive\Pictures\Git_def.PNG)

### But in Software Development terms:
Git is a modern Version control tool.

#### Before Git,
a common technique used for version control was to just
make a new copy of a project whenever any changes were made.  
The problem with this, is that if only a small numbers of files
in a project were altered between versions,
you'd be potentially wasting large amounts of storage with
identical copies of the unchanged files.

![Diagram of Classic Version Control](C:\Users\ashle\OneDrive\Pictures\Classic_VC.png)

#### With Git,
version control is achieved by only saving new copies of files
that have actually been updated,
as we'll still have access to the other files as long as
we have access to the older versions,
which is the whole point of version control anyway.

![Diagram of Git Version Control](C:\Users\ashle\OneDrive\Pictures\Git_VC.png)

#### Git Commands:
* `git init`
  * initialises git version control for the current directory.
* `git status`
  * informs of the current state of the files in the directory
  in relation to the current version.
* `git add [file_name(s)]`
  * adds the named/selected files to git staging,
  ready to by committed.
* `git commit -m "commit message"`
  * commits the currently staged files to the current version.