# Visitor
 * A component (visitor) that knows how to traverse a data structure
  composed of (possibly related) types

## Why to use Visitor pattern
- Need to define a new operation on an entire class hierarchy
  - E.g., make a document model printable to HTML/Markdown
- Do not want to keep modifying every class in the hierarchy
- Need access to the non-common aspects of classes in the hiearchy
- Create an external component to handle rendering
  - But avoid explicit type checks