"""
Helper function to make matplotlib plots more beautiful.

Author: Marcus Voss, marcus.voss@gmail.com
License: MIT
"""


def add_title_and_subtitle(fig, title, subtitle, title_fontsize="x-large", subtitle_fontsize="large", title_y_pos=0.05, title_x_pos=0.0, subtitle_y_pos=-0.05, subtitle_x_pos=0.0):
    """
    Adds a title and subtitle to the plot.

    Parameters
    ----------

    fig : matplotlib.figure.Figure
        The current figure to add the title to.

    title : str
        The title.

    subtitle : str
        The subtitle.

    title_fontsize : int or str, default "x-large"
        If int, size in points, or relative size, e.g., 'smaller', 'x-large'

    subtitle_font_size : int or str, default "large"
        If int, size in points, or relative size, e.g., 'smaller', 'x-large'

    subtitle_y_pos : flooat, default: -0.05
        The y position is using figure coordinates. This value can be used to fine adjust subtitle y position relative to figure top.

    title_y_pos : flooat, default: 0.05
        The y position is using figure coordinates. This value can be used to fine adjust title y position relative to figure top.

    subtitle_x_pos : flooat, default: 0.0
        The y position is using figure coordinates. This value can be used to fine adjust subtitle x position relative to figure left.

    title_x_pos : flooat, default: 0.0
        The y position is using figure coordinates. This value can be used to fine adjust title x position relative to figure left.

    """
    ax = fig.axes[0]
    ax.text(x=0 + subtitle_x_pos, y=1 + subtitle_y_pos, s=subtitle, fontsize=subtitle_fontsize, alpha=.85, ha="left", va="top", transform=fig.transFigure)
    ax.text(x=0 + title_x_pos, y=1 + title_y_pos, s=title, fontsize=title_fontsize, weight='bold', ha="left", va="top", transform=fig.transFigure)


def add_signature(fig, source=None, fontsize="x-small", copyright_x_pos=0.0, source_x_pos=-0.05, y_pos=-0.01):
    """
    Adds a signature bar with Copyright and if available source to the figure.

    Parameters
    ----------

    fig : matplotlib.figure.Figure
        The current figure to add the signature to.

    source : str, optional, default = None
        The source to add to the plot if available.

    fontsize : int or str, default "x-small"
        If int, size in points, or relative size, e.g., 'smaller', 'x-large'

    source_x_pos : flooat, default: -0.05
        The x position is using figure coordinates. This value can be used to fine adjust x position relative to figure right margin.

    copyright_x_pos : flooat, default: 0.0
        The x position is using figure coordinates. This value can be used to fine adjust x position relative to figure left margin.

    y_pos : flooat, default: -0.05
        The x position is using figure coordinates. This value can be used to fine adjust x position relative to figure bottom.

    """
    ax = fig.axes[0]
    ax.text(x=0. + copyright_x_pos, y=0.0 + y_pos, s='©CorrelAid', fontsize=fontsize, ha="left", va="top", transform=fig.transFigure)
    if source:
        ax.text(x=1 + source_x_pos, y=0.0 + y_pos, s='Source: %s' % source, fontsize=fontsize, ha="right", va="top", transform=fig.transFigure)


def remove_axes_labels(fig):
    """
    When using a subtitle that describes the domains, one doesn't need the axes labels.

    Parameters
    ----------

    fig : matplotlib.figure.Figure
        The current figure to remove all the axes' labels from.

    """
    for ax in fig.axes:
        ax.set_xlabel("")
        ax.set_ylabel("")


def place_legend_outside(ax, x_pos=0.00, y_pos=0.0):
    """
    Places the legend to the right outside.

    Parameters
    ----------

    ax : matplotlib.axes.Axes
        The axes to move the legend.

    x_pos : flooat, default: 0.0
        The x position is using bounding box. This value can be used to fine adjust x position relative to bounding box.

    y_pos : flooat, default: 0.0
        The y position is using bounding box. This value can be used to fine adjust y position relative to bounding box.

    """
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels, loc="upper left", bbox_to_anchor=(1 + x_pos, 1 + y_pos))


def set_correlaid_style(fig, title, subtitle, source=None, title_fontsize="x-large", subtitle_fontsize="large", signature_fontsize="x-small",
                        title_y_pos=0.05, title_x_pos=0.0, subtitle_y_pos=-0.05, subtitle_x_pos=0.0,
                        copyright_x_pos=0.0, source_x_pos=-0.05, signature_y_pos=-0.01,
                        legend_x_pos=0.00, legend_y_pos=0.0):
    """
    Applies all the functions with default values.

    Parameters
    ----------

    fig : matplotlib.figure.Figure
        The current figure to add the title to.

    title : str
        The title.

    subtitle : str
        The subtitle.

    source : str, optional, default = None
        The source to add to the plot if available.

    title_fontsize : int or str, default "x-large"
        If int, size in points, or relative size, e.g., 'smaller', 'x-large'

    subtitle_font_size : int or str, default "large"
        If int, size in points, or relative size, e.g., 'smaller', 'x-large'

    signature_fontsize : int or str, default "x-small"
        If int, size in points, or relative size, e.g., 'smaller', 'x-large'

    subtitle_y_pos : flooat, default: -0.05
        The y position is using figure coordinates. This value can be used to fine adjust subtitle y position relative to figure top.

    title_y_pos : flooat, default: 0.05
        The y position is using figure coordinates. This value can be used to fine adjust title y position relative to figure top.

    subtitle_x_pos : flooat, default: 0.0
        The y position is using figure coordinates. This value can be used to fine adjust subtitle x position relative to figure left.

    title_x_pos : flooat, default: 0.0
        The y position is using figure coordinates. This value can be used to fine adjust title x position relative to figure left.

    source_x_pos : flooat, default: -0.05
        The x position is using figure coordinates. This value can be used to fine adjust x position relative to figure right margin.

    copyright_x_pos : flooat, default: 0.0
        The x position is using figure coordinates. This value can be used to fine adjust x position relative to figure left margin.

    signature_y_pos : flooat, default: -0.05
        The x position is using figure coordinates. This value can be used to fine adjust x position relative to figure bottom.

    legend_x_pos : flooat, default: 0.0
        The x position is using bounding box. This value can be used to fine adjust x position relative to bounding box.

    legend_y_pos : flooat, default: 0.0
        The y position is using bounding box. This value can be used to fine adjust y position relative to bounding box.

    """
    remove_axes_labels(fig)
    add_title_and_subtitle(fig, title, subtitle, title_fontsize, subtitle_fontsize, title_y_pos, title_x_pos, subtitle_y_pos, subtitle_x_pos)

    add_signature(fig, source, signature_fontsize, copyright_x_pos, source_x_pos, signature_y_pos)

    for ax in fig.axes:
        place_legend_outside(ax, legend_x_pos, legend_y_pos)
