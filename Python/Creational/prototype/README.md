## Prototype 
- Specify the kinds of objects to create using a prototypical instance, and create new objects by copying the prototype.
- Useful when we have an existing object that needs to stay untouched, and we want to create an exact copy of it, allowing changes in some parts of the copy.

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
