By using the extends keyword, subclasses inherit all members of the parent class. "Members" includes:

All instance and static variables
All methods
All nested classes
Note that constructors are not inherited, and private members cannot be directly accessed by subclasses.


adding super() has no difference from the constructor we wrote before. It just makes explicit what was done implicitly by Java before. However, if we were to define another constructor in VengefulSLList, Java's implicit call may not be what we intend to call.