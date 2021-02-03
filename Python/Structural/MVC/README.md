## MVC 
- MVC is considered an architectural pattern rather than a design pattern.
### Use cases
- When implementing MVC from scratch, be sure that you create smart models, thin controllers, and dumb views.

A model is considered smart because it does the following:
- Contains all the validation/business rules/logic
- Handles the state of the application
- Has access to application data (database, cloud, and so on) 
- Does not depend on the UI

A controller is considered thin because it does the following:
- Updates the model when the user interacts with the view
- Updates the view when the model changes
- Processes the data before delivering it to the model/view, if necessary Does not display the data
- Does not access the application data directly
- Does not contain validation/business rules/logic

A view is considered dumb because it does the following:
- Displays the data
- Allows the user to interact with it
- Does only minimal processing, usually provided by a template language (for example, using simple - variables and loop controls)
- Does not store any data
- Does not access the application data directly Does not contain validation/business rules/logic
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