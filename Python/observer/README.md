## The Observer Pattern
- The Observer pattern describes a publish-subscribe relationship between a single object, the publisher, which is also known as the subject or observable, and one or more objects, the subscribers, also known as observers. 
- Assume that we are using the data of the same model in two views, for instance in a pie chart and in a spreadsheet. Whenever the model is modified, both the views need to be updated. That's the role of the Observer design pattern.
### Use cases:
- We generally use the Observer pattern when we want to inform/update one or more objects (observers/subscribers) about a change that happened on a given object (subject/publisher/observable). 
- news feeds
- Event-driven systems are another example where Observer is usually used. 
### Implementation
There is a default formatter that shows a value in the decimal format. However, we can add/register more formatters. In this example, we will add a hex and binary formatter. Every time the value of the default formatter is updated, the registered formatters are notified and take action. 
- Observer is actually one of the patterns where inheritance makes sense.
