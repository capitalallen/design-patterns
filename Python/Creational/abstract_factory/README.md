## The abstract factory 
- allows us to create one product through inheritance
- a generalization of the factory method.
- an abstract factory is a (logical) group of factory methods, where each factory method is responsible for generating a different kind of object.
- create families of related products

### Applicability:
- A system should be independent of how its products are created
- A system should be configured with one of multiple families of products
- A family of related product objects are designed to be used together, and you need to enforce this constraint
- You want to provide a class library of products, and you want to reveal just their interfaces, not their implementations

### Consequences:
- Isolates concrete classes
    - Client controls when objects are created
    - Factory controls which objects are created and how
- Makes exchanging product families easy
    - Promotes consistency among products
    - Supporting new kinds of products is difficult

### Example 
creating a game or we want to include a mini-game as part of our application to entertain our users. We want to include at least two games, one for children and one for adults. We will decide which game to create and launch at runtime, based on user input. 
An abstract factory takes care of the game creation part.

#### The summary for the implementation 
1. We define the Frog and Bug classes for the FrogWorld game.
2. We add the FrogWorld class, where we use our Frog and Bug classes.
3. We define the Wizard and Ork classes for the WizardWorld game.
4. We add the WizardWorld class, where we use our Wizard and Ork classes.
5. We define the GameEnvironment class.
6. We add the validate_age() function.
7. Finally, we have the main() function, followed by the conventional trick for calling it. The following are the aspects of this function:
    - We get the user's input for name and age
    - We decide which game class to use based on the user's age
    - We instantiate the right game class, and then the GameEnvironment class
    - We call .play() on the environment object to play the game