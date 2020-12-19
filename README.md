# CorrelAid matplotlib Style sheet

This repository aims to provide a [matplotlib style sheet](https://matplotlib.org/3.3.3/tutorials/introductory/customizing.html) following the CorrelAid style guide, possibly useful in the CorrelAid context, i.e. talks, blog posts, and such. 

## Use

Besides the default style, matplotlib comes with several built-in styles that we can use readily. To see a list of the available styles use: 

```python
import matplotlib.style as style
print(style.available)
```

```python
['seaborn-deep', 'seaborn-muted', 'bmh', 'seaborn-white', 'dark_background','seaborn-notebook', 'seaborn-darkgrid', 'grayscale', 'seaborn-paper', 'seaborn-talk', 'seaborn-bright', 'classic', 'seaborn-colorblind', 'seaborn-ticks', 'ggplot', 'seaborn', '_classic_test', 'fivethirtyeight', 'seaborn-dark-palette', 'seaborn-dark', 'seaborn-whitegrid', 'seaborn-pastel', 'seaborn-poster']
```
For instance, with the 'ggplot' one can use a style that is similar to the default R ggplot style:

```python
style.use('ggplot')
```

Here, we contribute a CorrelAid theme. The stlye file should be placed in your user folder in the .matplotlib folder (should already exist), in a folder `stylelib`  as follows:
```bash
~/.matplotlib/stylelib/correlaid.mplstyle
```
You may verify that it is detected by using the above `style.available` command. The the style file can then be used as follows:
```python
style.use('correlaid')
```

## Contribute
The style file is not yet complete and will only work for a subset of all the possible matplotlib and seaborn plots. There may still be lines appearing that may not have been correctly styled yet. Feel free to add more parameters to the file via a pull request or raise an issue for plot types that appear not yet as expected.

## More Information
The style is only the beginning to better looking matplotlib plots. This post gives some nice ideas how to add better lookings titles and subtiles and a signature bar:
- https://www.dataquest.io/blog/making-538-plots/
