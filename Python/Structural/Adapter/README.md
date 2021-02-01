## Adapter 
- Convert the interface of a class into another interface clients expect. Adapter lets classes work together that couldn’t otherwise because of incompatible interfaces.
- helps us make two incompatible interfaces compatible.

### Explain
- If we have an old component and we want to use it in a new system, or a new component that we want to use in an old system, the two can rarely communicate without requiring any code changes. But, changing the code is not always possible, either because we don't have access to it, or because it is impractical. 
- write an extra layer that makes all the required modifications for enabling the communication between the two interfaces. This layer is called an adapte

### Applicability:
- You want to use an existing class, and its interface does not match the one you need
- You want to create a reusable class that cooperates with unrelated or unforeseen classes that don’t necessarily have compatible interfaces
- (Object Adapter only) You need to use several existing subclasses, but it’s impractical to adapt their interface by subclassing every one. An object adapter can adapt the interface of its parent class.


### Consequences (class adapter):
- Adapts an Adaptee to Target by committing to a concrete Adapter class; a class adapter won’t work when we want to adapt a class and all of its subclasses
- Lets Adapter override some of Adaptee’s behaviour, since it’s a subclass of Adaptee
- Introduces only one object, and no additional pointer indirection is needed to get to the adaptee
### Consequences (object adapter):
- Lets a single Adapter work with many Adaptees including both the Adaptee itself and all of its subclasses
- Makes it harder to override Adaptee behaviour as it will require subclassing Adaptee and making Adapter refer to the subclass instead of the Adapter itself

### Use cases
- Usually, one of the two incompatible interfaces is either foreign or old/legacy. If the interface is foreign, it means that we have no access to the source code. If it is old, it is usually impractical to refactor it.
- Using an adapter for making things work after they have been implemented is a good approach because it does not require access to the source code of the foreign interface. It is also often a pragmatic solution if we have to reuse some legacy code.


### Example
-  a club's activities, mainly the need to organize performances and events for the entertainment of its clients, by hiring talented artists.