# Strategy
 * Enables the exact behavior of a system to be selected at run-time

## Why to use Strategy pattern
- Many algorithms can be decomposed into higher and lower level parts
- Making tea can be decomposed into
  - The process of making a hot beverage (boil water, pour into cup); and
  - Tea-specific things (put teabag into water)
- The high-level algorithm can then be reused for making coffee or hot
  chocolate
  - Supported by beverage-specific strategies