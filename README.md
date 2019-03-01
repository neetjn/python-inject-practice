# python-inject-practice
Practice with python dependency injection using python-inject @ https://github.com/ivankorobkov/python-inject

This project was created to learn how to perform dependency injection, the pythonic way using [**python-inject**](https://github.com/ivankorobkov/python-inject).

## Experiments

...

## What I've Learned

> Preface: Until recently (3/1/2019) I've never *knowingly* used dependency injection. The design pattern was not something I was consciously aware of, however I have leveraged it in several projects as well as production.

* Dependency injection is more of a development pattern than anything else.
* Contrary to my original confusion, there are multiple ways of tackling dependency injection.
* Angular.js, which I've been actively using for the past couple of years, revolves around dependency injection:
  ```
  angular.module('myModule', [])
    .factory('serviceId', ['depService', depService => {
      // ...
    }])
  ```
* Spring and Guice tackle this ...

## Closing Thoughts

* Dependency injection is certainly a useful concept for, and leveraging this in Python can help keep otherwise redundant code clean and concise.

## Resources

* Wikipedia (Dependency injection) - https://en.wikipedia.org/wiki/Dependency_injection
* baeldung (IoC and Dependency Injection in Spring) - https://www.baeldung.com/inversion-control-and-dependency-injection-in-spring
* angularjs/docs - https://docs.angularjs.org/guide/di

___

Copyright (c) 2019 John Nolette Licensed under the MIT License.
