## The Chain of Responsiblity 
- used when we want to give a chance to multiple objects to satisfy a single request, or when we don't know in advance which object (from a chain of objects) should process a specific request.
- the Chain of Responsibility relies on transforming particular behaviors into stand-alone objects called handlers. 
- link these handlers into a chain. Each linked handler has a field for storing a reference to the next handler in the chain. 
- the pattern allows multiple objects to handle the request without coupling sender class to the concrete classes of the receivers. The chain can be composed dynamically at runtime with any handler that follows a standard handler interface.
### Use cases:
- The Event class describes an event.
### Example
- The Event class describes an event.
- The Widget class is the core class of the application. 
- The parent aggregation shown in the UML diagram indicates that each widget can have a reference to a parent object
- The handle() method uses dynamic dispatching through hasattr() and getattr() to decide who is the handler of a specific request (event).
