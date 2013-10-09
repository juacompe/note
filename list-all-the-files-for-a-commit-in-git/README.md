List all the files for a commit in Git
----

```
git diff-tree --no-commit-id --name-only -r bd61ad98
```

or

```
git show --pretty="format:" --name-only bd61ad98
```

ref: <http://stackoverflow.com/questions/424071/list-all-the-files-for-a-commit-in-git>
