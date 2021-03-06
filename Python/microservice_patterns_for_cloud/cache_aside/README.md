## Cache-Aside
- applications use a cache to optimize repeated access to information stored in a database or data store.
- Load data on demand into a cache from a data store, as an attempt to improve performance, while maintaining consistency between data held in the cache and the data in the underlying data store.

### Real-world examples
- Memcached: a cache server
- Redis
- Amazon's ElastiCache

### Use cases
- The Cache-Aside pattern is useful for data that doesn't change often, and for data storage that doesn't depend on the consistency of a set of entries in the storage (multiple keys).
    - ex. it might work for certain kinds of document stores, where keys are never updated, and occasionally documents are deleted but there is no strong requirement to continue to serve them for some time (until the cache is refreshed).
- this pattern might not be suitable in the cases where the cached data set is static, or for caching session state information in a web application hosted in a web farm.

### Implementation
- steps needed when implementing the Cache-Aside pattern, involving a database and a cache, as follows:
    - Case 1: When we want to fetch a data item: return the item from cache if found in it. If not found in cache, read the data from the database. Put the read item in the cache and return it.
    - Case 2: When we want to update a data item: write the item in the database and remove the corresponding entry from the cache.