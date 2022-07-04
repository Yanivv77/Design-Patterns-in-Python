# Builder
When piecewise object construction is complicated,
provide an API for doing it clearly

* some objects are simply and can be created in a single
  initializer call
* other objects require a lot of ceremony to create
* having an object with 10 initializer arguments is not
  productive
* instead, opt for piecewise construction
* Builder provides an API for constructing an object
  step-by-step
