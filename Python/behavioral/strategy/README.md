## The Strategy Pattern
- a behavioral design pattern that turns a set of behaviors into objects and makes them interchangeable inside original context object.
- take a class that does something specific in a lot of different ways and extract all of these algorithms into separate classes called strategies.
- the original class, called context, must have a field for storing a reference to one of the strategies. The context delegates the work to a linked strategy object instead of executing it on its own.
- the context isn’t responsible for selecting an appropriate algorithm for the job. Instead, the client passes the desired strategy to the context. In fact, the context doesn’t know much about strategies. It works with all strategies through the same generic interface, which only exposes a single method for triggering the algorithm encapsulated within the selected strategy.
- strategy is based on composition: you can alter parts of the object’s behavior by supplying it with different strategies that correspond to that behavior. 

### Applicability
- Use the Strategy pattern when you want to use different variants of an algorithm within an object and be able to switch from one algorithm to another during runtime.
- the Strategy pattern lets you indirectly alter the object’s behavior at runtime by associating it with different sub-objects which can perform specific sub-tasks in different ways.

### When to use 
- use the Strategy when you have a lot of similar classes that only differ in the way they execute some behavior.
- use the pattern to isolate the business logic of a class from the implementation details of algorithms that may not be as important in the context of that logic.
- use the pattern when your class has a massive conditional operator that switches between different variants of the same algorithm.

### How to impolement 
1. In the context class, identify an algorithm that’s prone to frequent changes. It may also be a massive conditional that selects and executes a variant of the same algorithm at runtime.
2. Declare the strategy interface common to all variants of the algorithm.
3. One by one, extract all algorithms into their own classes. They should all implement the strategy interface.
4. In the context class, add a field for storing a reference to a strategy object. Provide a setter for replacing values of that field. The context should work with the strategy object only via the strategy interface. The context may define an interface which lets the strategy access its data.
4. Clients of the context must associate it with a suitable strategy that matches the way they expect the context to perform its primary job.

### Usage examples
- The Strategy pattern is very common in Python code. It’s often used in various frameworks to provide users a way to change the behavior of a class without extending it.

### Pros 
-  You can swap algorithms used inside an object at runtime.
- You can isolate the implementation details of an algorithm from the code that uses it.
- You can replace inheritance with composition.
- Open/Closed Principle. You can introduce new strategies without having to change the context.

### Cons 
- If you only have a couple of algorithms and they rarely change, there’s no real reason to overcomplicate the program with new classes and interfaces that come along with the pattern.
- Clients must be aware of the differences between strategies to be able to select a proper one.
- A lot of modern programming languages have functional type support that lets you implement different versions of an algorithm inside a set of anonymous functions. Then you could use these functions exactly as you’d have used the strategy objects, but without bloating your code with extra classes and interfaces

