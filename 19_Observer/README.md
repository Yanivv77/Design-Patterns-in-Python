# Observer
 * An observer is an object that wishes to be informed about events happening
  in the system. The entity generating the event is an observable.

## Why to use Observer pattern
- We need to be informed when certain things happen
  - Object's property changes
  - Object does something
  - Some external event
- We want to listen to events and be notified when they occur
  - Notification should include useful data
- Want to unsubscribe from events if we're no longer interested