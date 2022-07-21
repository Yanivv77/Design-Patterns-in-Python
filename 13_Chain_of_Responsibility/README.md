# Chain of responsibility
 * A chain of components who all get a chance to process a command
  or a query, optionally having default processing implementation
  and an ability to terminate the processig chain.

## Why to use Chain of responsibility pattern
   - Command = asking for an action or change (e.g., please set your
   attack value to 2)
   - Query = asking for information (e.g., please give me your attack)
   - CQS = having separate means of sending commands and queries