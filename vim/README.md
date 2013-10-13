Vim default
----

edit `$HOME/.vimrc`

```
set expandtab
set shiftwidth=4
set softtabstop=4
set tabstop=4
set nu
set autoindent
```

Description

- the first 4 lines would insert 4 spaces instead of \t when you press tab in insert mode
- set nu shows number

Concatenate string lines
----

```
:%s/$\n^//g
```

Scenario:
I have output of base64 command as below.

```
iVBORw0KGgoAAAANSUhEUgAAAf8AAAE7CAYAAADTiIgcAAAgAElEQVR4Xu2dCZQVxfWHr+PCDiIq
RIeocYNzNOICRFEHwS3ighKXKOoBDi4Q1CDK5vo3shjARAMuKASdmKgZ3EA9ERWMqCyumAweXGLE
KArKIoiI+M/tpCbNMMzr7tevu6r7q3PmMPBqufXd4v2qq6tubbPffvt9LyQIQAACEIAABHJDYJvp
06d/v9tuu0nnzp1z02k6CgEIQAACEMgLgY8//liWLl0q8+fPl1mzZsnixYtlm+//nfICgH5CAAIQ
gAAE8k5AJwOIf95HAf2HAAQgAIHcEUD8c+dyOgwBCEAAAnkngPjnfQTQfwhAAAIQyB0BxD93LqfD
EIAABCCQdwKIf95HAP2HAAQgAIHcEUD8c+dyOgwBCEAAAnkngPjnfQTQfwhAAAIQyB0BxD93LqfD
EIAABCCQdwKIf95HAP2HAAQgAIHcEUD8c+dyOgwBCEAAAnkngPjnfQTQfwhAAAIQyB0BxD93LqfD
```

and I want to concatenate them into a single line so that I can paste it in my code as a value of a string variable. So I paste those in vim and use the command below.

```
:%s/$\n^//g
```

Tada! This is the result

```
iVBORw0KGgoAAAANSUhEUgAAAf8AAAE7CAYAAADTiIgcAAAgAElEQVR4Xu2dCZQVxfWHr+PCDiIqRIeocYNzNOICRFEHwS3ighKXKOoBDi4Q1CDK5vo3shjARAMuKASdmKgZ3EA9ERWMqCyumAweXGLEKArKIoiI+M/tpCbNMMzr7tevu6r7q3PmMPBqufXd4v2qq6tubbPffvt9LyQIQAACEIAABHJDYJvp06d/v9tuu0nnzp1z02k6CgEIQAACEMgLgY8//liWLl0q8+fPl1mzZsnixYtlm+//nfICgH5CAAIQgAAE8k5AJwOIf95HAf2HAAQgAIHcEUD8c+dyOgwBCEAAAnkngPjnfQTQfwhAAAIQyB0BxD93LqfDEIAABCCQdwKIf95HAP2HAAQgAIHcEUD8c+dyOgwBCEAAAnkngPjnfQTQfwhAAAIQyB0BxD93LqfDEIAABCCQdwKIf95HAP2HAAQgAIHcEUD8c+dyOgwBCEAAAnkngPjnfQTQfwhAAAIQyB0BxD93LqfD
```

