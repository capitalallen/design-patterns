## Decorator 
- Attach additional responsibilities to an object dynamically. 
- Allows a programmer to add responsibilities to an object dynamically, and in a transparent manner (without affecting other objects).
- Decorators provide a flexible alternative to subclassing for extending functionality.
### Applicability:
- To add responsibilities to individual objects dynamically without affecting other objects
- For responsibilities that can be withdrawn
- When extension by subclassing is impractical
    - We may have a large number of independent extensions possible
    - The use of subclassing would produce an explosion of subclasses to support every combination
### Consequences:
- Provides more flexibility than static inheritance
    - Can add/remove responsibilities at run-time by attaching/detaching decorators
- Avoids feature-laden classes high up in the hierarchy
    - It would be inappropriate to put GZIP compression/decompression routines in the InputStream class
- A decorator and its component are not identical
    - Decorators act as transparent enclosures
    - However, we can no longer rely on object identity when using decorators
- Added complexity
    - Lots of little objects
    - Those new to Java often experience a WTF? moment when first discovering the many stream and reader classes available
    - “What happened to simple file I/O?”
### Use cases 
- used for extending the functionality of an object.
- shines when used for implementing cross-cutting concerns
    - Data validation 
    - Caching 
    - Logging
    - Monitoring 
    - Debugging 
    - Business rules 
    - Encryption
- In general, all parts of an application that are generic and can be applied to many other parts of it are considered to be cross-cutting concerns.