Git History
====

As a git user, I want to see history graph of my commits so that I know which branch it was originated and when it has been merged into my current branch.

```
log --pretty=format:'%h %ad | %s%d [%an]' --graph --date=rfc
```

As a git user, I want to have `git hist` command to show git history so that I don't have to type the long command above everytime I want to see the history.

Add the command above into `$HOME/.gitconfig` as an `alias`.

```
[alias]
    hist = log --pretty=format:'%h %ad | %s%d [%an]' --graph --date=rfc
```

Credit: [boyone](https://plus.google.com/u/1/+ThawatchaiJong/about) for sharing.

