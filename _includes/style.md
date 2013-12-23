---
---

## style
(optional)[dictionary]    
The highest level object that can define styles for the graph represented by the GraphJSON object.

GraphJSON does not require **style**.  If a GraphJSON object is passed with only **nodes** and **edges**, styles for the graph will simply be inherited by the application defaults or styles assigned to individual [nodes](#nodestyle_2) and [edges](#edgestyle_2).

All styles given to the GraphJSON document under the top level **style** will *cascade* to the graph. Styles can cascade to all parts nodes and edges, or only specific parts of the graph, as specified below.

**style** must include one or more of the following keys:

* **nodeStyle**
* **edgeStyle**
* **nodeStyle.{path}**
* **edgeStyle.{path}** 

Each object will contain a dictionary of styles associate with the "path" provided by the key, where the final value in the **{path}** variable can be a single *value* or *key*, or can be a *list* of any primitive (boolean, string, integer, etc.). 

For instance:

`"nodeStyle.category.movie"` will provide the styles for all of the nodes that have `"category": "movie"` in their toplevel.  However, if the value *movie* is more deeply nested, the **{path}** simply needs to specify that.  For example:

`"nodeStyle.properties.category.movie"` would declare styles for all nodes that have `"properties": {"category": "movie"}`.

`"edgeStyle.type.ACTED\_IN"` will behave similiarly and provide styles for all edges that have `"data": {"type": "ACTED\_IN"}`. 

Additionally, the end of **{path}** may specify a key. For example:

`"nodeStyle.genre"` where the style dictionary would be applied to every node that contained a *genre* key.  This may often result in less preferable behavior: e.g. the following nodes with `"genre": "comedy"`, `"genre": "drama"`, and `"genre": "action"` would all receive the same styles specified by `"nodeStyle.genre"`.

**Cascading Styles**

Applications should allow styles to cascade.  For example, all styles defined in `"nodeStyle"` will be the default for all nodes.  Styles declared at lower levels e.g. `"node.type.movie"`, or, on individual objects themselves (see [nodes](#nodestyle_2) and [edges](#edgeStyle_2) will always take preference.

**Precedence**

Clearly multiple different style objects can be associated with a node or edge, and in some cases the rules defined by those objects may conflict.  e.g. `"nodeStyle.genre.Romance"` and `"nodeStyle.category.award\_winner"` may apply conflicting styles to the same movie.  Applications should decide how to deal with nodes that happen to carry values that will try to apply conflicting styles to the same **{path}**.

Even if multiple style objects apply to the same node or edge (e.g. `"nodeStyle"`, `"nodeStyle.genre.Romance"` and `"nodeStyle.category.award\_winner"` may reference the same movie), only in cases where two or more style objects carry rules that are explicitly the same, will there be a conflict.  For example, if two objects declare different values for **fill** or **strokeWidth**.  In all other cases, **nodes** and **edges** will always try to inherit as many declared styles as possible.

### usage

#### nodeStyle
*(optional)[dictionary]*    
An object containing styles that will be passed to all nodes or a group of nodes (e.g. `"nodeStyle.{path}"`) and can contain any or all of the following optional keys that will effect the look of a graph visualization:

* **fill**    
    (optional)[string]    
    Is simply a string RGB or hex value value that will determine the fill color for a given node. e.g. `"#E89619"`

* **size**    
    (optional)[integer]    
    An integer pixel value for the radius of a node e.g `14`

* **stroke**    
    (optional)[string]    
    An RGB or hex value for the color of the outline of a node. e.g. `"rgba(232, 150, 25, 0.4)"`

* **strokeWidth**    
    (optional)[float]    
    The pixel value of the outline of a given node e.g. `.75`.

* **captionStroke**    
    (optional)[float]    
    An RGB or hex value for the color of the caption of a node. e.g. `"rgba(232, 150, 25, 0.4)"`

* **locked**    
    (optional)[boolean]     
    Defaults to "false" so that nodes can move freely throughout the graph.


**example**:
Declaring styles for *people* and *buildings*:

{% highlight json %}
{"style": {
    "nodeStyle.type.person": {
        "fill": "#3d84db",
        "stroke": "#b5430e"
    },
    "nodeStyle.type.building": {
        "fill": "#ffea00",
        "stroke": "#0dff00"
    }
}
{% endhighlight json %}

And might generate an image that looks like this:

{% include examples/node_style_example.html %}


#### edgeStyle
(optional)[dictionary]    
An object containing styles that will be passed to all edges or a groups of edges (e.g. `"edgeStyle.{path}"`).  The following objects can be used to specify styles related to edges:

* **stroke**    
    (optional)[string]    
    A string value that results in an RGB or hex value for color.  e.g. `"#333"`

* **strokeWidth**    
    (optional)[float]    
    Determines the visual 'thickness' in pixels of the edge connecting two nodes.

* **straight**    
    (optional)[boolean]    
    Defaults to `false`, but can be set to true to make edges between nodes appear straight.

* **bidirectional**    
    (optional)[boolean]    
    Defaults to `false` where every edge in the Graph is directed.  `...{"edgeStyle":{"bidirectional": true,...}...}`  will make all edges in the graph undirected.  *note:* Proper usage of the Graph model will not duplicate relationships to create bidirectionality.  For example, creating two edges between two "FRIENDS" on Facebook).  Rather, GraphJSON would specify `...{"edgeStyle.type.FRIENDS": {"bidirectional": true,...}...}...`

* **arrows**    
    (optional)[boolean]    
    Defaults to `false`, determines whether edges should receive arrows at each end of the edge.  If **arrows** is `true` the **target** end of the edge will receive an arrowhead.  Additionally, if **bidirectional** is `true` both ends of the edge will receive an arrow.

**example**:
Declaring styles for *LIVES_AT* edge:
{% highlight json %}
{"style": {
    "edgeStyle.type.LIVES_AT": {
        "stroke": "#00ff3c"
    }
}
{% endhighlight json %}

And might generate an image that looks like this:

{% include examples/edge_style_example.html %}
