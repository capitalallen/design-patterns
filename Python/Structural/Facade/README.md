## Facade 
- helps us to hide the internal complexity of our systems and expose only what is necessary to the client through a simplified interface. In essence, façade is an abstraction layer implemented over an existing complex system.
### Real-world examples:
- When you call a bank or a company, you are usually first connected to the customer service department. The customer service employee acts as a façade between you and the actual department (billing, technical support, general assistance, and so on), and the employee that will help you with your specific problem.
- a key used to turn on a car or motorcycle can also be considered a façade. 
### Use cases:
- The most usual reason to use the façade pattern is for providing a single, simple entry point to a complex system. 
- useful if you have more than one layer in your system. You can introduce one façade entry point per layer, and let all layers communicate with each other through their façades.
### Example
- Assume that we want to create an operating system using a multi-server approach, similar to how it is done in MINIX 3 (j.mp/minix3) or GNU Hurd (j.mp/gnuhurd). 
- shines when used for implementing cross-cutting concerns
    - Data validation 
    - Caching 
    - Logging
    - Monitoring 
    - Debugging 
    - Business rules 
    - Encryption
- In general, all parts of an application that are generic and can be applied to many other parts of it are considered to be cross-cutting concerns.