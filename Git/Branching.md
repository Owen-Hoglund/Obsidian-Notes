# Git branching

[documentation](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)

E.g. there's a parent branch `main`

`git checkout -b mynewbranch`

this is shorthand for:
creates: `git branch mynewbranch`
switches: `git checkout mynewbranch`

Once some new features on `mynewbranch` are finished, go to the GitHub.com interface and create a new pull request. Pull the changes from `mynewbranch` into `main`. GitHub will help determine whether the changes can be automatically merged, or whether there are some conflicts that need attending to. 

If there are conflicts, GitHub will point to where exactly in the code it wants you to select the changes to be saved in `main`, and it will present you with code block options to select from where it detects a conflict. I haven't had to do this that many times but you'll know it when you see it.
