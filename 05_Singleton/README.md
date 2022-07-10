# Singleton
 * A component which is instantiated only once

## Why to use Factories pattern
* For some components it only makes sense to have one in the system
   - Database repository
   - Object factory
* E.g., the initializer call is expensive
* We make a copy (clone) the prototype and customize it
   - We only do it once
   - We provide everyone with the same instance
* Want to prevent anyone from creating additional copies
* Need to take care of lazy instantiation