## Microservices and Patterns for the Cloud
- we can build an application as a set of loosely coupled, collaborating services.
- An application might consist of services such as the order management service, the customer management service, and so on. Services can be developed and deployed independently of one another.
### The Microservices pattern Use cases
We can use a microservices architecture-based design every time we are building an application that has at least one of the following characteristics:
- There is a requirement to support different clients, including desktop and mobile
- There is an API for third parties to consume
- We have to communicate with other applications using messaging
- We serve requests by accessing a database, communicating with other systems, and returning the right type of response (JSON, XML, HTML or even PDF)
- There are logical components corresponding to different functional areas of the application
### Implementation
- Switching from deploying a single application to deployments of many small services means that the number of things that need to be handled increases exponentially. 
- Using the microservices approach also means you need to use Containers.
- Thanks to Docker, things are getting easier, since we can run those services as containers. 
- The idea is that your application server, dependencies and runtime libraries, compiled code, configurations, and so on, are inside those containers. And then, all you have to do is run services packed as containers and make sure that they can communicate with each other.

A microservices framework for Python 
- lets service developers concentrate on application logic and encourages testability.

### RabbitMQ
- an open source multi-protocol messaging broker.