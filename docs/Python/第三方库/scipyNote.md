
#### Integrate
```py
from scipy.integrate import quad
val, err = quad(lambda x : np.sin(x),
                0,
                np.pi)
```

```py
from scipy.integrate import dblquad
val, err = dblquad(lambda y, x : x**2 * (y + 1) ,
                   0,
                   1,
                   lambda x : -x,
                   lambda x : x)
```

```py
from scipy.integrate import tplquad
val, err = tplquad(lambda z, y, x : 1,
                   0,
                   1,
                   0,
                   lambda x : np.sqrt(1 - x**2),
                   0,
                   lambda x, y : np.sqrt(1 - x**2 - y**2))
```


