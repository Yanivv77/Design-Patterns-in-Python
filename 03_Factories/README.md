# Factories
 * A component responsible solely for the wholesale creation of objects

## Why to use Factories pattern
 * Object creation logic becomes too convoluted
 * Initializer is not descriptive
   - Name is always __init__
   - Cannot overload with same sets of arguments with different names
   - Can turn into 'optional parameter hell'
 * Wholesale object creation (non-piecewise, unlike Builder)
   can be outsourced to
   - A separate method (Factory Method)
   - That may exist in a separate clas (Factory)
   - Can create a hiearchy of factories of Abstract Factory