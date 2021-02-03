## Flyweight 
- a technique used to minimize memory usage and improve performance by introducing data sharing between similar objects.
- a shared object that contains state-independent, immutable (also known as intrinsic) data.
- The state- dependent, mutable (also known as extrinsic) data should not be part of flyweight because this is information that cannot be shared, since it differs per object. 
### Definitions:
- Flyweight
    - A shared object that can be used in multiple contexts simultaneously
    - Acts as an independent object in each context – indistinguishable from an instance of the object that’s not shared
- Intrinsic state
    - Stored in the flyweight
    - Information that is independent of the flyweight’s context, thus making it shareable
- Extrinsic state
    - Depends on / varies with the flyweight’s context
    - Can’t be shared
### Applicability:
- An application uses a large number of objects
- Storage costs are high because of the sheer quantity of objects
- Most object state can be made extrinsic
- Many groups of objects can be replaced by relatively few shared objects once extrinsic state is removed
- The application doesn’t depend on object identity
- Since flyweight objects are shared, identity tests will return true for conceptually distinct objects
### Consequences:
- The obvious: reduced memory requirements
- May introduce run-time costs (transferring, finding, computing extrinsic state)
    - Should be offset by space savings
    - Savings increase as more flyweights are shared

### Use cases:
- All embedded systems (phones, tablets, games consoles, microcontrollers, and so forth) and performance-critical applications (games, 3-D graphics processing, real-time systems, and so forth) can benefit from it.
- requirements that need to be satisfied to effectively use the flyweight pattern:
    - The application needs to use a large number of objects.
    - There are so many objects that it's too expensive to store/render them. Once the mutable state is removed (because if it is required, it should be passed explicitly to flyweight by the client code), many groups of distinct objects can be replaced by relatively few shared objects.
    - Object identity is not important for the application. We cannot rely on object identity because object sharing causes identity comparisons to fail (objects that appear different to the client code end up having the same identity).
### Example
- create a small car park to illustrate the idea, making sure that the whole output is readable in a single terminal page. However, no matter how large you make the car park, the memory allocation stays the same.re generic and can be applied to many other parts of it are considered to be cross-cutting concerns.
### memoization vs the flyweight pattern
- Memoization is an optimization technique that uses a cache to avoid recomputing results that were already computed in an earlier execution step. Memoization does not focus on a specific programming paradigm such as object-oriented programming (OOP).
- Flyweight is an OOP-specific optimization design pattern that focuses on sharing object data.