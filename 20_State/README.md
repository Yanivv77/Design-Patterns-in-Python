# State
 * A pattern in which the object's behavior is determined by its state. An
  object transitions from one state to another (something needs to trigger
  a transition).
 * A formalized construct which manages state and transitions is called a state machine.
  

## Why to use State pattern
- Consider an ordinary telephone
- What you do with it depends on the state of the phone/line
  - If it's ringing or you want to make a call, you can pick it up
  - Phone must be off the hook to talk/make a call
  - If you try calling someone, and it's busy, you put the handset down
- Change in state can be explicit or in response to an event (Observer pattern)