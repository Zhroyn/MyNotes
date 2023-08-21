
#### Random Number
```py
randint(a, b) method of random.Random instance
    Return random integer in range [a, b], including both end points.

random() method of Random instance
    Return x in the interval [0, 1).

randrange(start, stop=None, step=1) method of Random instance
    Choose a random item from range(stop) or range(start, stop[, step]).

uniform(a, b) method of Random instance
    Get a random float in the range [a, b] or [b, a].
```

#### Choice Element
```py
choice(seq) method of Random instance
    Choose a random element from a non-empty sequence.

choices(population, weights=None, *, cum_weights=None, k=1)
    Return a k sized list of population elements chosen with replacement.
    The size of weights must be equal to population.
    Probability of element being choiced is its weight devided by total weight.

sample(population, k, *, counts=None)
    Chooses k unique random elements from a population sequence.
    If the population contains repeats, then each is a possible selection.
    counts can be used to repeat elements.
```

#### Shuffle
```py
shuffle(x) method of Random instance
    Shuffle list x in place, and return None.
```

