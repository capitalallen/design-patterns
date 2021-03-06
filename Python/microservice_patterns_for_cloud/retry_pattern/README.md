## The Retry pattern
- Parts of a cloud-native application may experience transient faults or failures
    - some mini-issues that can look like bugs, but are not due to your application itself but to some constraints outside of your control such as the networking or the external server/service performance.
- The answer to the risk of such failures is to put in place some retry logic, so that we pass through the issue, by calling the service again, maybe immediately or after some wait time (such as a few seconds).
### Real-world examples
- the Retrying library
- tenacity library
### Use cases
- not recommended for handling failures such as internal exceptions caused by errors in the application logic itself.
- If the application experiences frequent busy faults, it's often a sign that the service being accessed has a scaling issue that should be addressed.

### Example 1
- write and update a file using two different programs (which could be services).

### Example 2
- Use a third-party module