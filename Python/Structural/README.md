## Structural Design Pattern 
- proposes a way of composing objects for creating new functionality.
- Concerned with how classes/objects are composed to form larger structures
- Two types:
    - Class Structural
        - Use inheritance to compose interfaces and implementations
    - Object Structural
        - Describe ways to compose objects to realize new functionality
        - Added flexibility → can change composition at run-time


### Applicability:
- When the classes to instantiate are specified at run-time, for example, by dynamic loading; or
- When instances are expensive to create, but easy to copy; or
- When instances of a class can have one of only a few different combinations of state; in such a case, it may be more convenient to install a corresponding number of prototypes and clone them rather than instantiating the class manually, each time with the appropriate state

### Consequences:
- Hides the concrete product classes from the client 
– we don’t have to know which concrete type we’re cloning
- Specify new objects by varying values
- Configuring an application with classes dynamically
- Add/remove varieties at run time from a pool of prototypes
- May reduce need for subclassing
- May even remove need for Factory subclasses

### Example 
- When you have to manage multiple websites, there is a point where it becomes difficult to follow. You need to access information quickly such as IP addresses that are involved, domain names and their expiration dates, and maybe details about the DNS parameters. So you need a kind of inventory tool.
