# Memento
 * A token/handle representing the system state. Lets us roll back to the state
  when the token was generated. May or may not directly expose system
  information.

## Why to use Memento pattern
- An object or system goes through changes
  - E.g., a bank account gets deposits and withdrawals
- There are different ways of navigating those changes
- One way is to record every change (Command) and teach a command to
  'undo' itself
- Another way is to create snapshots of the system (Memento)