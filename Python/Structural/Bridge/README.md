## Bridge 
- Decouple an abstraction from its implementation so that the two can vary independently.
- is designed up-front to decouple an implementation from its abstraction
### Applicability:
- You want to avoid a permanent binding between an abstraction and its implementation
- Both the abstractions and their implementations should be extensible by subclassing; Bridge lets you combine the different abstractions and implementations and extend them independently
- Changes in the implementation of an abstraction should have no impact on clients
- You want to share an implementation among multiple objects and this fact should be hidden from the client

### Consequences:
- Decouples interface and implementation → the two are not bound permanently
- Can potentially change implementation at run-time
- Improved extensibility → can extend Abstraction and Implementor independently
- Hides implementation details from clients

- A decorator and its component are not identical
    - Decorators act as transparent enclosures
    - However, we can no longer rely on object identity when using decorators
- Added complexity
    - Lots of little objects
    - Those new to Java often experience a WTF? moment when first discovering the many stream and reader classes available
    - “What happened to simple file I/O?”
### Use cases
- Using the bridge pattern is a good idea when you want to share an implementation among multiple objects. 
- Basically, instead of implementing several specialized classes, defining all that is required within each class, you can define the following special components:
    - An abstraction that applies to all the classes
    - A separate interface for the different objects involved

### Example 
- building an application where the user is going to manage and deliver content after fetching it from diverse sources
    - A web page (based on its URL)
    - A resource accessed on an FTP server 
    - A file on the local file system
    - A database server
- instead of implementing several content classes, each holding the methods responsible for getting the content pieces, assembling them, and showing them inside the application, we can define an abstraction for the Resource Content and a separate interface for the objects that are responsible for fetching the content.