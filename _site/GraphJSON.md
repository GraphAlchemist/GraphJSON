 > [Home](Home) > **GraphJSON**

GraphJSON is an object that must specify **nodes** in the top level, and can have an **edges** and **style** toplevel key.  Most GraphJSON objects will include **edges**, however they are optional because a GraphJSON object (while not mathematically sound) can contain unconnected nodes.  Hypothetically a GraphJSON object could consist of one, unconnected node.  Meanwhile, if **style** is not included, a graph derived from GraphJSON will simply inherit styles from the application.

* GraphJSON
    * [[style|GraphJSON#style]]
        * [[nodeStyle|GraphJSON#nodestyle]]
        * [[edgeStyle|GraphJSON#edgestyle]]
        * [[nodeStyle.{path}|GraphJSON#nodestyle]]
        * [[edgeStyle.{path}|GraphJSON#edgestyle]]
    * [[nodes|GraphJSON#nodes]]
        * [[_id|GraphJSON#\_id]]
        * [[caption|GraphJSON#caption]]
        * [[x|GraphJSON#x]]
        * [[y|GraphJSON#y]]
        * [[nodeStyle|GraphJSON#nodestyle-1]]
        * [[OptionalNodeData}|GraphJSON#OptionalNodeData]]
    * [[edges|GraphJSON#edges]]
        * [[_source|GraphJSON#_source]]
        * [[_target|GraphJSON#_target]]
        * [[caption|GraphJSON#caption]]
        * [[edgeStyle|GraphJSON#edgeStyle]]
        * [[OptionalEdgeData|GraphJSON#OptionalEdgeData]]


## style
*(optional)[dictionary]*    
The highest level object that can define styles for the graph represented by the GraphJSON object.

GraphJSON does not require **style**.  If a GraphJSON object is passed with only **nodes** and **edges**, styles for the graph will simply be inherited by the application defaults.

All styles given to the GraphJSON document will *cascade* to the graph.  Styles can cascade to all parts nodes and edges, or only specific parts of the graph, as specified below.

**style** must include one or more of the following keys:

* **nodeStyle**
* **edgeStyle**
* **nodeStyle.{path}**
* **edgeStyle.{path}** 

Each object will contain a dictionary of styles associate with the "path" provided by the key, where the final value in the **{path}** variable can be a single *value* or *key*, or can be a *list* of any primitive (boolean, string, integer, etc.). 

For instance, *nodeStyle.category.movie* will provide the styles for all of the nodes that have `"category": "movie"` in their toplevel.  If the value *movie* is more deeply nested, the **{path}** simply needs to specify that.  For example, *nodeStyle.properties.category.movie* would declare styles for a node that has `"properties": {"category": "movie"}`.

*edgeStyle.data.type.ACTED_IN* will provide styles for all edges that have `"data": {"type": "ACTED_IN",...}`.  In this case `"ACTED_IN"`.  A key can also be specified - for example, `"nodeStyle.data.genre"` where the style dictionary would be applied to every node that contained a *genre* key.  This may often result in less preferable behavior, but can be a useful shortcut.

Applications should allow styles to cascade.  For example, all styles defined in `node` will be the default for all nodes.  Styles declared at lower levels e.g. *node.data.type.movie*, or, on individual objects themselves (see [[nodeStyles|GraphJSON#nodeStyles]] and [[edgeStyles|GraphJSON#edgeStyles]]) will always take preference.

Clearly multiple different style objects can be associated with a node or edge, and in some cases the rules defined by those objects may conflict.  e.g. *nodeStyle.genre.Romance* and *nodeStyle.category.award_winner* may apply conflicting styles to the same movie.  Applications should decide how to deal with nodes that happen to carry values that will apply conflicting {paths}.  GraphJSON generated from a solid underlying data model, and well thought out style rules should not experience this problem.  Additionally, it is important to keep in mind that even if multiple *style objects* apply to the same node or edge (e.g. *nodeStyle* and *nodeStyle.genre.Romance* and *nodeStyle.category.award_winner*) only in cases where two or more style objects carry rules that are explicitly the same, will there be a conflict.  For example, if two objects declare different values for **fill** or **strokeWidth**.  In all other cases, **nodes** and **edges** will always try to inherit as many declared styles as possible.

### *usage* 

#### nodeStyle
*(optional)[dictionary]*    
An object containing styles that will be passed to all nodes or a group of nodes (e.g. `"nodeStyle.{path}"`) and can contain any or all of the following optional keys that will effect the look of a graph visualization:

* **fill**    
    *(optional)[string]*    
    Is simply a string RGB or hex value value that will determine the fill color for a given node. e.g. `"#E89619"`

* **size**    
    *(optional)[integer]*     
    An integer pixel value for the radius of a node e.g `14`

* **stroke**    
    *(optional)[string]*    
    An RGB or hex value for the color of the outline of a node. e.g. `"rgba(232, 150, 25, 0.4)"`

* **strokeWidth**    
    *(optional)[float]*       
    The pixel value of the outline of a given node e.g. `.75`.

* **locked**    
    *(optional)[boolean]*      
    Defaults to "false" so that nodes can move freely throughout the graph.

*example*:
```json
{"an example":true}
```

#### edgeStyle
*(optional)[dictionary]*    
Aan object containing styles that will be passed to all edges or a groups of edges (e.g. `"edgeStyle.{path}"`).  The following objects can be used to specify styles related to edges:

* **stroke**    
    *(optional)[string]*    
    A string value that results in an RGB or hex value for color.  e.g. `"#333"`

* **strokeWidth**    
    *(optional)[float]*    
    Determines the visual 'thickness' in pixels of the edge connecting two nodes.

* **straight**    
    *(optional)[boolean]*    
    Defaults to `false`, but can be set to true to make edges between nodes appear straight.

* **bidirectional**    
    *(optional)[boolean]*    
    Defaults to `false` where every edge in the Graph is directed.  `...{"edgeStyle":{"bidirectional": true,...}...}`  will make all edges in the graph undirected.  *note:* Proper usage of the Graph model will not duplicate relationships to create bidirectionality.  For example, creating two edges between two "FRIENDS" on Facebook).  Rather, GraphJSON would specify `...{"edgeStyle.type.FRIENDS": {"bidirectional": true,...}...}...`

* **arrows**    
    *(optional)[boolean]*    
    Defaults to `false`, determines whether edges should receive arrows at each end of the edge.  If **arrows** is `true` the **target** end of the edge will receive an arrowhead.  Additionally, if **bidirectional** is `true` both ends of the edge will receive an arrow.

*example*:
```json
{"an example":true}
```


## nodes
*(required)[list]*    
The top level GraphJSON object **nodes** is a list of dictionaries with declarative information about the individual nodes.

Each node dictionary is capable of holding the following top level keys:

* **_id**
* **caption**
* **x**
* **y**
* **nodeStyle**
* **{optional_node_data}**

*example:*
```json
{"an example":true}
```

### *usage*

#### _id 
*(required)[integer or string]*    
A string or integer and must be unique within the GraphJSON object.  Additionally, **_id** must be identical to the value passed to **_source** (source id) and **_target** (target id) in **edges**.

#### caption
*(optional)[string]*    
The value displayed by the node in the graph visualization.  **caption** may be the same as any value from other objects and need not be unique to a single node in the Graph.

#### x 
*(optional)[integer]*    
The **x** coordinate of the initial position of the node where `0` would be in the middle of the horizontal axis.  If **locked** is `true` (e.g. `"nodeStyle": {"locked": true,...}`) the node will remain at the x coordinate specified.

#### y
*(optional)[integer]*    
The **y** coordinate of the initial position of the node where `0` would be in the middle of the vertical axis.  If **locked** is `true` (e.g.`"nodeStyle": {"locked": true,...}`) the node will remain at the y coordinate specified.

*Note:* A common use of **x** and **y** would be to specify a root node that will be in the center and not move after the initial layout (e.g. `"x": 0, "y": 0, nodeStyle: {"locked": true, ...}`.  Additionally, using client side layout rendering can be extremely cumbersome or impossible if the Graph visualization includes more than 500 or 1,000 nodes and edges.  For large scale graph rendering formats passing layout from compute engines to rendering software, GraphJSON will specify the **x** and **y** position of each node in the layout.

#### nodeStyle 
*(optional)[dictionary]*    
The **nodeStyle** object attached to a specific node will apply style rules to that node only.  **nodeStyle** contains rules that can be defined with all of the same parameters that the top level **nodeStyle** dictionary carries.  ([[see nodeStyle|GraphJSON#nodestyle]])  

Any rules specified by a specific node will override **defaults** specified in the top level **style** key.  If style rules conflict with rules handed down from the top level, rules attached to the node directly will always take priority.  

#### OptionalNodeData
*(optional)[value, dictionary, or list]*    
Each node can contain an arbitrary number of objects which are all optional and can refer to a dictionary, or primitives as a list or single value.  All optional data related to a specific node instance is stored under the top level of that node object (e.g. next to **_id** and **nodeStyle**, etc.) .  The purpose is to support data across different data sources and nuanced property graph data models.  For instance, a Neo4j user might store a **labels** list and a **properties** dictionary under each node (e.g. `"properties":{..,},"labels":[...]`).  A Titan user might store a **type** key value and a **properties** dictionary (e.g. `"properties":{...}, "type": "value"`).  Additionally, a user may even choose to store all optional node data as top-level key-values under the node directly (e.g. `{"name":..., "age":..., "hometown":...}`).

The optional objects held by nodes can be shared in common with other nodes or can be unique to the node holding them - for instance, `"firstName"`, `"app_id"`, `"genre"`, `"title"`, `"category"`, `"properties"`, `"type"`, etc.  These objects can serve any number of purposes in the application layer for analytics, filtering of the data, etc.  Additionally, the GraphJSON **nodeStyle** object makes use of optional node data in an important way through [[(paths)|GraphJSON#style]].

GraphJSON takes into account that their are nuanced differences in how underlying Graph Databases, Graph compute engines, document stores, and even relational databases store and classify nodes and edges.  Often times a high-fidelity property Graph model is able to take into account the end user experience, research question, or business value being created.  However, one of the key problems GraphJSON solves, is the inherent gap between the data model and the applications that leverage the data model.  We believe this is the best way to leave open maximum flexibility to the different users, while maintaining a standard - [feedback welcome](mailto:feedback@graphalchemist.com).

*example*:
```json
{"an example":true}
```

#### node example
*example*:
```json
{"an example":true}
```

## edges
*(required)[list]*    
The connections between **nodes**.  **edges** objects take on a similar data structure as the **nodes** themselves. Each edge can have only one source and one target node.  Edges are always directed, meaning that source and target nodes are always specified using `_source` and `_target`.  Depending on the use case, the 'direction' of the edge may or may not be relevant.  Edges *do not* need to be specified in both directions, unless the underlying data model needs them to be. If bidirectionality is more natural to the data model, this can be taken care of in [[data|GraphJSON#edge-data]].  For instance, *"friends"* on Facebook will always be specified with a **source** and **target** node, even though we know the edge is bidirectional and it is not relevant which node is target and which is source.  However, in the context of the Twitter Graph, the source and target nodes are extremely important to the "follows" relationship and can have important implications for the analytics and visualizations generated from the data.

Additionally, Graphs can contain disconnected nodes, and so strictly speaking, edge dictionaries are in fact NOT required for all nodes in a GraphJSON object.

Each edge should hold the following top level keys:
* **_source**
* **_target**
* **caption**
* **edgeStyle**
* **{optional_edge_data}**

*example:*
```json
{"an example":true}
```
### *usage*

#### _source 
*(required)[integer or string]*    
A string or integer and must be unique within the GraphJSON object.  Additionally, **_source** must be identical to the value passed to **_id** to the corresponding **source** node.

#### _target 
*(required)[integer or string]*    
A string or integer and must be unique within the GraphJSON object.  Additionally, **target** must be identical to the value passed to **_id** for the corresponding **target** node.

#### OptionalEdgeData
*(optional)[value, dictionary, or list]*    
Just like the **nodes**, **edges** can contain an arbitrary number of objects which are all optional and can refer to a dictionary, or to primitives as a list or single value.  A Neo4j user might store a **properties** dictionary and a **type** key value in the edge object.  For example, `...{..."type": "...", "properties":{...}...}...`.  A Titan user might store a **label** key value and a **properties** dictionary.  For example, `...{"label":...,"properties":{...}...}...`.  Just like with nodes, a user may even choose to store all data as top-level key-values e.g. `...{"start_time":..., "isCurrent":..., "weight":...,...}...`.

*example*:
```json
{"an example":true}
```



#### edgeStyle
*(optional)[dictionary]*    
The **edgeStyle** object attached to a specific **edge** will apply style rules to that edge only.  **edgeStyle** contains rules that can be defined with all of the same parameters that the top level **edgeStyle** dictionary carries.  ([[see edgeStyle|GraphJSON#edgestyle]])  
Any rules specified by a specific edge will override *defaults* specified in the top level **style** object.  If style rules conflict with rules handed down from the top level, rules attached to the edge directly will always take priority.
