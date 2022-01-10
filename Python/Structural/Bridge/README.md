## Bridge 
- Decouple an abstraction from its implementation so that the two can vary independently.
- is designed up-front to decouple an implementation from its abstraction
- a structural design pattern that lets you split a large class or a set of closely related classes into two separate hierarchies—abstraction and implementation—which can be developed independently of each other.
### Applicability:
- You want to avoid a permanent binding between an abstraction and its implementation
- Both the abstractions and their implementations should be extensible by subclassing; Bridge lets you combine the different abstractions and implementations and extend them independently
- Changes in the implementation of an abstraction should have no impact on clients
- You want to share an implementation among multiple objects and this fact should be hidden from the client
- Use the Bridge pattern when you want to divide and organize a monolithic class that has several variants of some functionality (for example, if the class can work with various database servers).
- Use the pattern when you need to extend a class in several orthogonal (independent) dimensions.
- Use the Bridge if you need to be able to switch implementations at runtime.

### How to Implement
1. Identify the orthogonal dimensions in your classes. These independent concepts could be: abstraction/platform, domain/infrastructure, front-end/back-end, or interface/implementation.
2. See what operations the client needs and define them in the base abstraction class.
3. Determine the operations available on all platforms. Declare the ones that the abstraction needs in the general implementation interface.
4. For all platforms in your domain create concrete implementation classes, but make sure they all follow the implementation interface.
5. Inside the abstraction class, add a reference field for the implementation type. The abstraction delegates most of the work to the implementation object that’s referenced in that field.
6. If you have several variants of high-level logic, create refined abstractions for each variant by extending the base abstraction class.
7. The client code should pass an implementation object to the abstraction’s constructor to associate one with the other. After that, the client can forget about the implementation and work only with the abstraction object.

### Pros 
- You can create platform-independent classes and apps.
- The client code works with high-level abstractions. It isn’t exposed to the platform details.
- Open/Closed Principle. You can introduce new abstractions and implementations independently from each other.
- Single Responsibility Principle. You can focus on high-level logic in the abstraction and on platform details in the implementation.

### Cons
- You might make the code more complicated by applying the pattern to a highly cohesive class.
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

### Usage examples: 
- The Bridge pattern is especially useful when dealing with cross-platform apps, supporting multiple types of database servers or working with several API providers of a certain kind (for example, cloud platforms, social networks, etc.)