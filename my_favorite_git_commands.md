# Basic version control with git

## Standard flow 1

In this case you are working on a project and are writing a feature. A remote branch called `feature` was already created.

Copy changes from remote repo to local. No changes are done to local repo in this step.
```
git fetch
```

Switch to the new branch.
```
git checkout feature
```

Check if you are on the correct branch
```
git branch
git branch --show-current
```

Introduce your changes and check if they are correct.
```
git diff
```

Move your changes of `file.txt`to the staging area.
```
git add file.txt
```

Or move all of your changes to the staging area.
```
git add .
```

Check if your staged changes are correct.
```
git diff --staged
```

Create a commit from the changes in the staging area.
```
git commit
```

Check if the commit is correct.
```
git show
```

Check for changes that were introduced to the remote, and include them in the local `feature` branch. Replace `origin/master` with whatever the main branch is in the remote repo.
```
git fetch
git rebase origin/master
```

Push your local commit to the remote repo.
```
git push
```

Check the status of the repo
```
git status
```

## How to modify a commit

For example you receive some comments on a PR and need to update your commit. After making the changes, you should follow this flow to modify the commit instead of creating a new one.

```
git add .
git commit --amend
git push -f
```

## Creating a branch named `feature` locally and pushing it to a remote

```
git branch feature
git checkout feature
git add .
git commit
git push --set-upstream origin feature
```

## Create the `git tree` command which can show you a tree of the current repo

```
git config --global alias.tree "log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(bold yellow)%d%C(reset)' --all"
```
