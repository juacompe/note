Set Proxy For Wifi On Command Line
====

As a Mac user, I want to set my web proxy for my Wi-Fi to `http://hogwartsjenkins:443` so that I can connect to the Internet at my office.

```
networksetup -setwebproxy Wi-Fi hogwartsjenkins 443
```

As a Mac user, I want to unset my web proxy for my Wi-Fi interface so that I can connect to the Internet at my home.

```
networksetup -setwebproxystate Wi-Fi off
```

ref: [How to change proxy setting using Command line in Mac OS?](http://superuser.com/questions/316502/how-to-change-proxy-setting-using-command-line-in-mac-os)
