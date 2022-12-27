#### Inheritance
By using the extends keyword, subclasses inherit all members of the parent class. "Members" includes:
- All instance and static variables
- All methods
- All nested classes

Note that constructors are not inherited, and private members cannot be directly accessed by subclasses.


adding super() has no difference from the constructor we wrote before. It just makes explicit what was done implicitly by Java before. However, if we were to define another constructor in VengefulSLList, Java's implicit call may not be what we intend to call.


#### Autobox
- Java can implicitly convert between primitive and wrapper types
- Arrays are never autoboxes or auto-unboxed, e.g. if you have an array of integers `int[] x`, and try to put its address into a variable of type `Integer[]`, the compiler will not allow your program to compile.

#### Widening
- Java will also automatically widen a primitive if needed
- If you want to go from a wider type to a narrower type, you must manually cast