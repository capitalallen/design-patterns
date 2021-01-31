## Builder 
- Separate the construction of a complex object from its representation so that the same construction process can create different representations.

### Applicability
- The algorithm for creating a complex object should be independent of the parts that make up the object and how they’re assembled
- The construction process must allow different representations for the object that’s constructed

### Classes
- Director
    - Responsible for the sequence of build operations
- Builder
    - Abstract interface for creating products
- Concrete Builder
    - Implements construction and assembly of parts
- Product
    - Object that will be created by Concrete Builder

### Consequences:
- Lets you vary a product’s internal representation
- Isolates code for construction and representation
- Gives you finer control over the construction process

### Builder vs. Abstract Factory
- Abstract Factory
    - Deals with families of related objects
    - Available immediately
- Builder
    - Creates one, complex product, usually made up of different parts
    - Available via getResult()

### Example 
- make a pizza-ordering application.
- When using the builder pattern, the end product does not have many responsibilities, since it is not supposed to be instantiated directly. 
