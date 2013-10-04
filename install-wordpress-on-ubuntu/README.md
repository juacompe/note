Install Wordpress on Ubuntu
====

Install Apache
----

```
sudo apt-get install apache2
```

access the web and you should see *It's works*

Install Wordpress
----

```
sudo apt-get install wordpress
```

The wordpress is downloaded at `/usr/share/wordpress/`. We need to copy it to root folder of our web application. By default, the web root is at `/var/www/`.

```
sudo cp -R /usr/share/wordpress/ /var/www/
```

Then `chwon` the folder so that `www-data` can access.

```
sudo chown -R www-data: /var/www/wordpress/
```

Then restart apache and try to access the web at http://<host>/wordpress/

```
sudo service apache2 restart
```

Then we see the error like below:

```
Neither /etc/wordpress/config-54.254.162.246.php nor /etc/wordpress/config-254.162.246.php could be found. 
Ensure one of them exists, is readable by the webserver and contains the right password/username.
```

Oops! It seems that our wordpress config is not found. We need `mysql` and the configuration file for the wordpress to works.

```
sudo apt-get install mysql-server
```

Then we need to run the setup script that wordpress has prepared for us (assuming our domain is `myscrum.com`).

```
sudo bash /usr/share/doc/wordpress/examples/setup-mysql -n myscrum_com myscrum.com
```

Now we should be able to acess http://myscrum.com/wordpress/ to finish the setup.

ref: <https://help.ubuntu.com/community/WordPress>
