## Proxy
- A class that functions as an interface to a particular resource.
  The resource can be remote, expensive to construct, or may
  require logging or some other added functionality
  
## Why to use Proxy pattern
- Same interface, entirely different behavior
- Types: logging, virtual,  guarding

## Proxy vs Decorator
- Proxy provides identical inferface, decorator provides enhanced 
  interface
- Decorator typically aggregates (or has reference to) what it is
  decorating; proxy doesn't have to
- Proxy might not even be working with a materialized object