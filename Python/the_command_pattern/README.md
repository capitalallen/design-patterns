## The Command Pattern 
- helps us encapsulate an operation (undo, redo, copy, paste, and so forth) as an object. 


### Use cases:
- The Event class describes an event.
### Implementation
Implement the most basic file utilities:
- Creating a file and optionally writing text (a string) to it 
- Reading the contents of a file
- Renaming a file
- Deleting a file
- Undo can actually be implemented on delete file operations. One technique is to use a special trash/wastebasket directory that stores all the deleted files, so that they can be restored when the user requests it. This is the default behavior used on all modern desktop environments and is left as an exercise.
