AngularJS Configure Open And Close Brackets
----

By default, the open and close brackets used in Angular templates are `{{` and `}}`.

This convention is also used by Django's teamplate. We cannot use the `{{` and `}}` on both Django and Angular templates.

To configure Angular to use different symbol:

```
myModule.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
  });
```

ref: <http://stackoverflow.com/questions/8302928/angularjs-with-django-conflicting-template-tags>

