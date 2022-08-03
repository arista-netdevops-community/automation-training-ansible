# Pushing your work

This should be your easiest lab of the day.
In this lab, you're going to experience commiting the files you've written to your local git repo, and then pushing those commits to a remote git repo on Github.

## Commit your local changes
Change directory to the day1 repo (`cd /home/coder/project/labfiles/day1`).

Run `git status` and look at the list of files git reports as changed, created, or deleted.

Run `git commit -a` to stage and commit all files you have changed.
Write a commit message and save it, and then git will commit your code.
Alternatively, try using the `git add` and `git commit` commands separately, to explore working with git staging.

## Setup a Github account

If you don't already have a Github account, go make one at [Github's signup page](https://github.com/signup)
If you already have an account, login

## Add your ATD SSH key to your Github profile

We're going to use SSH keys for pushing code here, so you'll need to add the publickey from your ATD VSCode instance to your Github profile so that Github will accept commit pushes from your instance.
To do this, run `cat ~/.ssh/id_rsa.pub` from your VSCode terminal, and copy this value to your clipboard.
Go to your profile settings page on Github, and click on the "SSH and GPG keys" tab on the sidebar, then click "New SSH key".
Paste your key data in here, and hit save.
You can remove this key from your profile after the ATD topology has been decommissioned if you wish.

## Create a new Github repo

Click the "+" symbol in the top right of the Github page, and select "New repository".
From here, give your new repository a name (doesn't matter, make it something significant to you) and set the privacy to Private.
Click the green "Create repository" button.

On the next page, look for the section header "push an existing repository".
Paste those commands into your VSCode terminal, and you should see git push your commits to Github.
Refresh the page and confirm you now see your files in the new repository.