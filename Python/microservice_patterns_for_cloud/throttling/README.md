## Throttling
- based on limiting the number of requests a user can send to a given web service in a given amount of time, in order to protect the resources of the service from being overused by some users.
- The answer to the risk of such failures is to put in place some retry logic, so that we pass through the issue, by calling the service again, maybe immediately or after some wait time (such as a few seconds).

### Real-world examples
- The built-in support in Django-Rest-Framework
- Django-throttle-requests 
- The flask-limiter

### Use cases
- This pattern is recommended when you need to ensure your system continuously delivers the service as expected, or when you need to optimize the cost of usage of the service, or when you need to handle bursts in activity.
- In practice, you may implement the following rules:
    - Limit the number of total requests to an API as N/day (for example, N=1000)
    - Limit the number of requests to an API as N/day from a given IP address, or from a given country or region
    - Limit the number of reads or writes for authenticated users
