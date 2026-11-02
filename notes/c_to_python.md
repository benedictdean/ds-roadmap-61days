Differences

1. Typing
    IN C: int x = 5; (static)
    IN Python: x = 5 (dynamic)
    Takeaway: the type(s) belong to the object(s) at runtime instead of the variable name.
        ~an object is a basic unit for storing data and behavior, while a type (or class) defines what an object is allowed to do (like what values the object can hold, the operations, etc.)
        ~the data lives in the object itself, and the object knows that kind of thing it is.

2. Variables
    IN C: fixed memory boxes
    IN Python: name bindings (labels)
    Takeaway: when we reassign x, the label moves to a new object in memory. since again, di man siya fixed.

3. Blocks
    IN C: {} & ;
    IN Python: 4 space indentation
    Takeaway: to send a code or to start a new line of code properly, there has to be 4 spaces of indentation. and indentation is syntax; misaligning causes IndentationError

4. Loops 
    IN C: for (int i = 0; i < 10; i++);
    IN Python: for x in iterable  OR  range(n)
    Takeaway: It iterates directly over the items instead of manually indexing

5. Sequences
    IN C: int a[10] (fixed array type)
    IN Python: list [a, "a", 3.0]
    Takeaway: lists can have multiple types, and can grow dynamically. so no more alloc and the same idea from c

6. Records 
    IN C: struct
    IN Python: dict({"k": v})  OR  @dataclass
    Takeaway: dictionaries give instant o(1) key-value lookups

7. Pointers vs Refs
    IN C: *p or &x (explicit)
    IN Python: implicit object references
    Takeaway: a = b = [] points both names to the exact same list in memory (alias)

8. Null Value
    IN C: NULL (0)
    IN Python: None
    Takeaway: you check with if x is None:, instead of ==

9. Formatting
    IN C: printf("x = %d", n);
    IN Python: print(f"x={x}");
    Takeaway: f strings evaluate expressions directly inside curly brace.

10. Memory
    IN C: malloc / free()
    IN Python: Automatic Garbage Collection
    Takeaway: Reference counting + cycle detector frees unused objects automatically.

11. Division
    IN C: 5 / 2 gives 2 (int)
    IN Python: 5 / 2 gives 2.5 ; 5 // 2 gives 2
    Takeaway: / is always float division. and // is int floor division

12. Truthiness
    IN C: generally, 0 is false and non zero is true 
    IN Python: anything empty (including 0) is False.
    Takeaway: checking of empty list is 
        if not list:
    instead of 
        if len(list) == 0