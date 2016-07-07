=================
Options Reference
=================

This is the list of options supported by Pycha. These options are defined
in a dictionary and passed to the chart constructor as the second argument.

In the following reference each option name is the key path in the options
dictionary. So if an option is named *foo.bar*, to set that option in the
options dictionary, you should create a nested dictionary::

 options = {
   'foo': {
     'bar': 1.0,
   }

In this example we set the option *foo.bar* the value 1.0.

Some options can have a None value. In this case the option is considered to
be unseted.

Using the *Chavier* application is a great way to discover how an option
affect the final chart.

Axis options
============

The following options affect how both axes are rendered.

**axis.lineWidth**
  * Description: width for both axis lines.
  * Type: float
  * Default: 1.0

**axis.lineColor**
  * Description: color for both axis lines.
  * Type: color
  * Default: '#0f0000'

**axis.tickSize**
  * Description: length of the ticks for both axis lines.
  * Type: float
  * Default: 3.0

**axis.labelColor**
  * Description: color of the axis label for both axis. This option has no
    effect if either the axis.x.label or axis.y.label are not set (which is
    the default).
  * Type: color
  * Default: '#666666'

**axis.labelFont**
  * Description: font of the axis label for both axis. This option has no
    effect if either the axis.x.label or axis.y.label are not set (which is
    the default).
  * Type: string
  * Default: 'Tahoma'

**axis.labelFontSize**
  * Description: font size in points of the axis label for both axis. This
    option has no effect if either the axis.x.label or axis.y.label are not
    set (which is the default).
  * Type: integer
  * Default: 9

**axis.tickFont**
  * Description: font family for tick texts.
  * Type: string
  * Default: 'Tahoma'

**axis.tickFontSize**
  * Description: font size in points for tick texts.
  * Type: integer
  * Default: 9

**axis.x.hide**
  * Description: True if the x axis should be hidden. False otherwise.
  * Type: boolean
  * Default: False

**axis.x.ticks**
  * Description:
  * Type: list
  * Default: None

**axis.x.tickCount**
  * Description:
  * Type: integer
  * Default: 10

**axis.x.tickPrecision**
  * Description:
  * Type: integer
  * Default: 1

**axis.x.range**
  * Description:
  * Type: list
  * Default: None

**axis.x.rotate**
  * Description: clockwise angle in degrees for the tick texts rotation or
    None for no rotation.
  * Type: float
  * Default: None

**axis.x.label**
  * Description: text that will appear under the axis.
  * Type: string
  * Default: None

**axis.x.interval**
  * Description:
  * Type: integer
  * Default: 0

**axis.x.showLines**
  * Description:
  * Type: boolean
  * Default: False

**axis.y.hide**
  * Description:
  * Type: boolean
  * Default: False

**axis.y.ticks**
  * Description:
  * Type: list
  * Default: None

**axis.y.tickCount**
  * Description:
  * Type: integer
  * Default: 10

**axis.y.tickPrecision**
  * Description:
  * Type: integer
  * Default: 1

**axis.y.range**
  * Description:
  * Type: list
  * Default: None

**axis.y.rotate**
  * Description:
  * Type: list
  * Default: None

**axis.y.label**
  * Description:
  * Type: string
  * Default: None

**axis.y.interval**
  * Description:
  * Type: integer
  * Default: 0

**axis.y.showLines**
  * Description:
  * Type: boolean
  * Default: True

Background options
==================

**background.hide**
  * Description:
  * Type: boolean
  * Default: False

**background.basecolor**
  * Description:
  * Type: color
  * Default: None

**background.chartColor**
  * Description:
  * Type: color
  * Default: '#f5f5f5'

**background.lineColor**
  * Description:
  * Type: color
  * Default: '#ffffff'

**background.lineWidth**
  * Description:
  * Type: float
  * Default: 1.5

Legend options
==============

**legend.opacity**
  * Description:
  * Type: float
  * Default: 0.8

**legend.borderColor**
  * Description:
  * Type: color
  * Default: '#000000'

**legend.borderWidth**
  * Description:
  * Type: float
  * Default: 2.0

**legend.hide**
  * Description:
  * Type: boolean
  * Default: False

**legend.position.top**
  * Description:
  * Type: float
  * Default: 20.0

**legend.position.left**
  * Description:
  * Type: float
  * Default: 40.0

**legend.position.bottom**
  * Description:
  * Type: float
  * Default: None

**legend.position.right**
  * Description:
  * Type: float
  * Default: None

Padding options
===============

**padding.left**
  * Description:
  * Type: float
  * Default: 10.0

**padding.right**
  * Description:
  * Type: float
  * Default: 10.0

**padding.top**
  * Description:
  * Type: float
  * Default: 10.0

**padding.bottom**
  * Description:
  * Type: float
  * Default: 10.0

Stroke options
==============

**stroke.color**
  * Description:
  * Type: color
  * Default: '#fffffff'

**stroke.hide**
  * Description:
  * Type: boolean
  * Default: False

**stroke.shadow**
  * Description:
  * Type: boolean
  * Default: True

**stroke.width**
  * Description:
  * Type: float
  * Default: 2.0

Yvals options
=============

**yvals.show**
  * Description:
  * Type: boolean
  * Default: False

**yvals.inside**
  * Description:
  * Type: boolean
  * Default: False

**yvals.fontSize**
  * Description:
  * Type: integer
  * Default: 11

**yvals.fontColor**
  * Description:
  * Type: color
  * Default: '#000000'

**yvals.skipSmallValues**
  * Description:
  * Type: boolean
  * Default: True

**yvals.snapToOrigin**
  * Description:
  * Type: boolean
  * Default: False

**yvals.renderer**
  * Description:
  * Type: ??
  * Default: None

Color scheme options
====================

TODO: link to the color scheme chapter

**colorScheme.name**
  * Description:
  * Type: string
  * Default: 'gradient'

**colorScheme.args**
  * Description:
  * Type: dict
  * Default: {initialColor: DEFAULT_COLOR, colors: None}


Other options
=============

**fillOpacity**
  * Description:
  * Type: float
  * Default: 1.0

**shouldFill**
  * Description:
  * Type: boolean
  * Default: True

**barWidthFillFraction**
  * Description:
  * Type: float
  * Default: 0.75

**pieRadius**
  * Description:
  * Type: float
  * Default: 0.4

**title**
  * Description:
  * Type: string
  * Default: None

**titleColor**
  * Description:
  * Type: color
  * Default: '#000000'

**titleFont**
  * Description:
  * Type: string
  * Default: 'Tahoma'

**titleFontSize**
  * Description:
  * Type: integer
  * Default: 12

**encoding**
  * Description:
  * Type: string
  * Default: 'utf-8'
