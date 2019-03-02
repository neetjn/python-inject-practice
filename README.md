# python-inject-practice
> Practice with python dependency injection using python-inject @ https://github.com/ivankorobkov/python-inject

This project was created to learn how to perform dependency injection, the pythonic way using [**python-inject**](https://github.com/ivankorobkov/python-inject). I'll be recording my thoughts and experiments in this repository.

## Experiments

* "instance" injection using **python-inject**. This injection strategy allows me to pull a binded dependency by object type from my injector given my configuration. See: [instance_injection.py](https://github.com/neetjn/python-inject-practice/instance_injection.py)

* "attribute" injection **python-inject**. This injection strategy allows me to bind a dependency from my injector into class instances. See: [attribute_injection.py](https://github.com/neetjn/python-inject-practice/attribute_injection.py)

## What I've Learned

> Preface: Until recently (3/1/2019) I've never *knowingly* used dependency injection. The design pattern was not something I was consciously aware of, however I leverage it almost daily in both personal projects and in production.

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

## Resources

* Wikipedia (Dependency injection) - https://en.wikipedia.org/wiki/Dependency_injection
* baeldung (IoC and Dependency Injection in Spring) - https://www.baeldung.com/inversion-control-and-dependency-injection-in-spring
* angularjs/docs - https://docs.angularjs.org/guide/di
* pinject - https://github.com/google/pinject
* preslav (Dependency Injection In Python - The Java Guy's Perspective) - https://preslav.me/2018/12/20/dependency-injection-in-python/

___

Copyright (c) 2019 John Nolette Licensed under the MIT License.
