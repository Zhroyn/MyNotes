
### Create Figures

```py
plt.figure(
    num=None,
    figsize=None,
    dpi=None,
    *,
    facecolor=None,
    edgecolor=None,
    frameon=True,
    FigureClass=<class 'matplotlib.figure.Figure'>,
    clear=False,
    **kwargs,
) -> Figure
```

- `num` : `int | str | .Figure | .SubFigure`
    - A unique identifier for the figure.
    - If a figure with that identifier already exists, this figure is made active and returned.
    - If there is no figure with the identifier or `num` is not given, a new figure is created, made active and returned.
    - If `num` is an int, it will be used for the ``Figure.number`` attribute, otherwise, an auto-generated integer value is used (starting at 1 and incremented for each new figure).
    - If `num` is a string, the figure label and the window title is set to this value.
    - If `num` is a ``SubFigure``, its parent ``Figure`` is activated.
- `figsize` : `(float, float)`
    - Width, height in inches.
    - Default is `(6.4, 4.8)`.
- `dpi` : `float`
    - The resolution of the figure in dots-per-inch.
    - Default is `100`.
- `frameon` : If False, suppress drawing the figure frame, which means some arguments will become invalid. 
- `clear` : If True and the figure already exists, then it is cleared.


### Create Subplot

- `fig.add_subplot(*args, **kwargs) -> Axes`
    - Add an `~.axes.Axes` to the figure as part of a subplot arrangement.
    - `*args` : `int | (int, int, int) | .SubplotSpec`
        - Three integers (*nrows*, *ncols*, *index*). The subplot will take the `index` position on a grid with `nrows` rows and `ncols` columns.
        - `index` starts at 1 in the upper left corner and increases to the right.
        - `index` can also be a two-tuple specifying the (*first*, *last*) indices (1-based, and including *last*) of the subplot,.
        - A 3-digit integer. The digits are interpreted as if given separately as three single-digit integers.
        - A `.SubplotSpec`.
    - `projection` : `{None, 'aitoff', 'hammer', 'lambert', 'mollweide', 'polar', 'rectilinear', str}`
        - The projection type of the subplot.
        - `str` is the name of a custom projection.
        - The default `None` results in a `'rectilinear'` projection.
    - `polar` : `bool`
        - If True, equivalent to `projection='polar'`.
    - `sharex, sharey` : `~.axes.Axes`
        - The axis will have the same limits, ticks, and scale as the axis of the shared axes.
- `plt.subplot(*args, **kwargs) -> Axes`
    - Add an Axes to the current figure or retrieve an existing Axes.
- `plt.subplots(*args, **kwargs) -> (Figure, Axes)`
    - Create a figure and a set of subplots.





### Show and Save

- `plt.show(*, block=None)` Display all open figures.
- `plt.imshow(X, cmap=None, norm=None, *)`
    - Display data as an image, i.e., on a 2D regular raster.
    - `X` : array-like or PIL image.
    - `cmap` : str or `~matplotlib.colors.Colormap`
        - The Colormap instance or registered colormap name used to map scalar data to colors.
    - `norm` : str or `~matplotlib.colors.Normalize`
        - The normalization method used to scale scalar data to the [0, 1] range.
        - By default, a linear scaling is used, mapping the lowest value to 0 and the highest to 1.

<div style="margin-top: 25pt"></div>

- `plt.savefig(*args, **kwargs)`
    - Save the current figure.
    - `fname` : str or path-like or binary file-like
    - `format` : The file format, e.g. `'png', 'pdf', 'svg', ...`. The behavior when this is unset is documented under `fname`.





### Modify Axes

#### Add Title

- `plt.title(label, fontdict=None, loc=None, pad=None, *, y=None, **kwargs)`
- `ax.set_title(label, fontdict=None, loc=None, pad=None, *, y=None, **kwargs)`
    - Set a title for the Axes.
    - `label` : `str`
        - Text to use for the title
    - `fontdict` : dict
        - A dictionary controlling the appearance of the title text.
    - `loc` : `{'center', 'left', 'right'}`
    - `y` : `float`
        - Vertical Axes location for the title (1.0 is the top).
    - `pad` : float
        - The offset of the title from the top of the Axes, in points.

#### Add Label

- `plt.xlabel(xlabel, fontdict=None, labelpad=None, *, loc=None, **kwargs)`
- `ax.set_xlabel(xlabel, fontdict=None, labelpad=None, *, loc=None, **kwargs)`
    - Set the label for the x-axis.
    - `xlabel` : The label text.
    - `labelpad` : float
        - Spacing in points from the Axes bounding box including ticks and tick labels.  If None, the previous value is left as is.
    - `loc` : `{'left', 'center', 'right'}`
- `plt.ylabel(ylabel, fontdict=None, labelpad=None, *, loc=None, **kwargs)`
- `ax.set_ylabel(ylabel, fontdict=None, labelpad=None, *, loc=None, **kwargs)`
    - Set the label for the y-axis.

#### Set Limit

- `ax.set_xlim(left, right)`
- `ax.set_xlim((left, right))`
- `ax.set_ylim(bottom, top)`
- `ax.set_ylim((bottom, top))`

<div style="margin-top: 25pt"></div>

- `ax.get_xlim() -> (left, right)`
- `ax.get_ylim() -> (bottom, top)`

<div style="margin-top: 25pt"></div>

- `plt.xlim()` is equivalent to `ax.get_xlim()`
- `plt.xlim(left, right)` is equivalent to `ax.set_xlim(left, right)`
- `plt.ylim()` is equivalent to `ax.get_ylim()`
- `plt.ylim(bottom, top)` is equivalent to `ax.set_ylim(bottom, top)`

#### Set Ticks

- `ax.set_xticks(ticks, labels=None, *, minor=False, **kwargs)`
    - Set the xaxis' tick locations and optionally labels.
    - `ticks` : list of floats
    - `labels` : list of str, optional
    - `minor` : If False, set the major ticks; if True, the minor ticks.
- `ax.set_xticklabels(labels, *, fontdict=None, minor=False, **kwargs)`
    - Set the xaxis' labels with list of string labels.
    - This method should only be used after fixing the tick positions. Otherwise, the labels may end up in unexpected positions.

<div style="margin-top: 25pt"></div>

- `ax.get_xticks(*, minor=False)`
    - Return the xaxis' tick locations in data coordinates.
- `ax.get_xticklabels(minor=False, which=None)`
    - Get the xaxis' tick labels.

<div style="margin-top: 25pt"></div>

- `plt.xticks(ticks=None, labels=None, *, minor=False, **kwargs)`
    - Get or set the current tick locations and labels of the x-axis.
    - `locs, labels = xticks()` Get the current locations and labels.
    - `plt.xticks([])` Disable xticks.

#### Set Legend

- `ax.legend(*args, **kwargs)`
- `fig.legend(*args, **kwargs)`
- `plt.legend(*args, **kwargs)`
    - Place a legend on the Axes.
    - `handles` : A list of Artists (lines, patches) to be added to the legend.
    - `labels` : A list of labels to show next to the artists.

#### Add Text

- `ax.text(x, y, s, fontdict=None, **kwargs)`
    - Add the text `s` to the Axes at location `x`, `y` in data coordinates.
- `ax.annotate(text, xy, xytext=None, xycoords='data', textcoords=None, arrowprops=None, annotation_clip=None, **kwargs)`
    - Annotate the point `xy` with text `text`.
    - `text` : str
        - The text of the annotation.
    - `xy` : (float, float)
        - The point *(x, y)* to annotate. The coordinate system is determined by *xycoords*.
    - `xytext` : (float, float)
        - The position *(x, y)* to place the text at. The coordinate system is determined by *textcoords*.
        - Default is `xy`.
    - `arrowprops` : dict, optional
        - The properties used to draw a `.FancyArrowPatch` arrow between the positions `xy` and `xytext`.  Defaults to None, i.e. no arrow is drawn.






### Change Style

#### Show Config

- `print(matplotlib.rcParams)`
- `print(matplotlib.rcParamDafault)`
- `print(matplotlib.rc_params())`
- `print(matplotlib.get_configdir())`





