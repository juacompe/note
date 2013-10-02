Add a sudo user on Ubuntu
====

As a Ubuntu user, I want to add a new user with sudo privilege so that I can use that user to do crazy stuffs

Add a new linux user
----

```
$> adduser juacompe
```

User juacompe will be created with group juacompe and home folder at `/home/juacompe`

Add the user to sudo group (so that the user has sudo power)
----

```
$> usermod -aG sudo juacompe
```

Test which groups that user juacompe belongs to
----

```
$> groups juacompe
juacompe sudo
```

refs:
[adduser vs useradd: Ubuntu, Debian, Gentoo, Fedora, CentOS](http://www.garron.me/go2linux/useradd-vs-adduser-ubuntu-linux.html)


