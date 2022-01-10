## The Template Pattern
- behavioral design pattern that defines the skeleton of an algorithm in the superclass but lets subclasses override specific steps of the algorithm without changing its structure.

### Solution
- break down an algorithm into a series of steps, turn these steps into methods, and put a series of calls to these methods inside a single template method.
- the steps may either be abstract, or have some default implementation. To use the algorithm, the - - client is supposed to provide its own subclass, implement all abstract steps, and override some of the optional ones if needed
- As you can see, we’ve got two types of steps:
    - abstract steps must be implemented by every subclass
    - optional steps already have some default implementation, but still can be overridden if needed
- hooks are placed before and after crucial steps of algorithms, providing subclasses with additional extension points for an algorithm.

### Applicability
- Use the Template Method pattern when you want to let clients extend only particular steps of an algorithm, but not the whole algorithm or its structure.
- The Template Method lets you turn a monolithic algorithm into a series of individual steps which can be easily extended by subclasses while keeping intact the structure defined in a superclass.
- Use the pattern when you have several classes that contain almost identical algorithms with some minor differences. As a result, you might need to modify all classes when the algorithm changes.

###  How to Implement
1. Analyze the target algorithm to see whether you can break it into steps. Consider which steps are common to all subclasses and which ones will always be unique.
2. Create the abstract base class and declare the template method and a set of abstract methods representing the algorithm’s steps. Outline the algorithm’s structure in the template method by executing corresponding steps. Consider making the template method final to prevent subclasses from overriding it.
3. It’s okay if all the steps end up being abstract. However, some steps might benefit from having a default implementation. Subclasses don’t have to implement those methods.
4. Think of adding hooks between the crucial steps of the algorithm.
5. For each variation of the algorithm, create a new concrete subclass. It must implement all of the abstract steps, but may also override some of the optional ones.

### Usage examples
- he Template Method pattern is quite common in Python frameworks. Developers often use it to provide framework users with a simple means of extending standard functionality using inheritance.

