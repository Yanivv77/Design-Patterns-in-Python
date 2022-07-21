# Command
 * An object which represents an instruction to perform a particular action.
  Contains all the information necessary for the action to be taken.

## Why to use Command pattern
   - Ordinary statements are perishable
   - Cannot undo member assignment
   - Cannot directly serialize a sequence of actions (calls)
   - Want an object that represents an operation
   - person should change its age to value 22
   - car should do explode()
   - Uses: GUI commands , multilevel undo/redo, macro recording and more!