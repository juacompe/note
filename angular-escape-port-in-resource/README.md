AngularJS Escaping port number in resource
----

In Angular the colon (`:`) is used to specify parameters in the URL. To specify port number, the `:` must be escaped with double backslashes (`\\`).

```
url = 'http://localhost\\:3000/wine';
```
