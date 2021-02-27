## The Chain of Responsiblity 
-  used when we want to give a chance to multiple objects to satisfy a single request, or when we don't know in advance which object (from a chain of objects) should process a specific request.

### Use cases:
- The Event class describes an event.
### Example
- The Event class describes an event.
- The Widget class is the core class of the application. 
- The parent aggregation shown in the UML diagram indicates that each widget can have a reference to a parent object
- The handle() method uses dynamic dispatching through hasattr() and getattr() to decide who is the handler of a specific request (event).
