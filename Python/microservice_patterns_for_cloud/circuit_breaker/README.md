## circuit breaker
- wrap a fragile function call (or an integration point with an external service) in a special (circuit breaker) object, which monitors for failures. Once the failures reach a certain threshold, the circuit breaker trips, and all further calls to the circuit breaker return with an error, without the protected call being made at all.

### Real-world examples
- The pybreaker Python library
- Hystrix, from Netflix, a sophisticated tool for dealing with latency and fault
tolerance for distributed systems
- The Java library Jrugged 

### Use cases
- the Circuit Breaker pattern is recommended when you need a component from your system to be fault-tolerant to long-lasting failures when communicating with an external component, service, or resource.

### Implementation
- use a circuit breaker on a flaky function (for example, fragile due to the networking environment it depends on).