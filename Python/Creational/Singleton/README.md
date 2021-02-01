## Singleton 
- The singleton pattern restricts the instantiation of a class to one object, which is useful when you need one object to coordinate actions for the system.
- only one instance of a particular class, doing a job, is created for the needs of the program.

### Use Case:
- useful when you need to create only one object or you need some sort of object capable of maintaining a global state for your program.
- possible use cases
    - Controlling concurrent access to a shared resource. For example, the class managing the connection to a database.
    - A service or resource that is transversal in the sense that it can be accessed from different parts of the application or by different users and do its work. For example, the class at the core of the logging system or utility.


### Example 
- implement a program to fetch content from web pages
-  be able to track the list of web pages that were tracked, hence the use of the singleton pattern: we need a single object to maintain that global state.
