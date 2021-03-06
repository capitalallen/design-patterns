## The Observer Pattern in Reactive Programming
- Problem of Observer: in a situation where we have to deal with many events, some of them depending on each other, the traditional way could lead to complicated, difficult-to-maintain code. 
- react to many events, streams of events, while keeping our code clean.
- an Observable as a stream that can push or emit data to the Observer. 
### Real-world examples
- A spreadsheet application 
- Java (RxJava), Python (RxPY), and JavaScript (RxJS).
- The Angular Framework uses RxJS to implement the Observable pattern.
- rx: python 
    - An API for asynchronous programming with observable streams
### Implementation
#### 1st example 
- create an Observable from the list of quotes we get. The way we can do things as follows:
    1. Define a function that hands data items to the Observer
    2. Use an Observable.create() factory, and pass it that function, to set up the source or stream of data
    3. Make the Observer subscribe to the source
- The Observer class itself has three methods used for this type of communication:
    1. The on_next() is used to pass items
    2. The on_completed() will signal that no more items are coming 
    3. The on_error() signals an error
