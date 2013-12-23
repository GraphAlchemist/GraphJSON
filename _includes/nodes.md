---
---

## nodes
(required)[list]    
The top level GraphJSON object **nodes** is a list of dictionaries with declarative information about the individual nodes.

Each node dictionary is capable of holding the following top level keys:
* [**\_id**](#_id)
* [**caption**](#caption)
* [**x**](#x)
* [**y**](#y)
* [**nodeStyle**](#nodestyle_2)
* [**{optional\_node\_data}**](#optionalnodedata)

A classic node:
{% highlight json %}
{"nodes": [
    {
        "_id": 10,
        "caption": "Kevin Bacon",
        "properties" {
            "age": 55,
            "height": "5'10"
            "description": "Kevin Norwood Bacon is an American actor and musician...",
            "first_name": "Kevin",
            "last_name": "Bacon",
            "properties_can_store_anything": true
        },
        "labels": ["Actor", "Musician", "Director", "Male", "Person"],
        "mid": "some machine id",
        "IMDB_id": "IMDB id",
        "some other data": "etc."},
    ]
}
{% endhighlight json %}

### usage

#### \_id 
(required)[integer or string]    
A string or integer and must be unique within the GraphJSON object.  Additionally, **\_id** must be identical to the value passed to **\_source** (source id) and **\_target** (target id) in **edges**.

#### caption
(optional)[string]    
The value displayed by the node in the graph visualization.  **caption** may be the same as any value from other objects and need not be unique to a single node in the Graph.

#### x 
(optional)[integer]    
The **x** coordinate of the initial position of the node where `0` would be in the middle of the horizontal axis.  If **locked** is `true` (e.g. `"nodeStyle": {"locked": true,...}`) the node will remain at the x coordinate specified.

#### y
(optional)[integer]    
The **y** coordinate of the initial position of the node where `0` would be in the middle of the vertical axis.  If **locked** is `true` (e.g.`"nodeStyle": {"locked": true,...}`) the node will remain at the y coordinate specified.

*Note:* A common use of **x** and **y** would be to specify a root node that will be in the center and not move after the initial layout (e.g. `"x": 0, "y": 0, nodeStyle: {"locked": true, ...}`.  Additionally, using client side layout rendering can be extremely cumbersome or impossible if the Graph visualization includes more than 500 or 1,000 nodes and edges.  For large scale graph rendering formats passing layout from compute engines to rendering software, GraphJSON will specify the **x** and **y** position of each node in the layout.

#### nodeStyle 
(optional)[dictionary]    
The **nodeStyle** object attached to a specific node will apply style rules to that node only.  **nodeStyle** contains rules that can be defined with all of the same parameters that the top level **nodeStyle** dictionary carries.  ([[see nodeStyle|GraphJSON#nodestyle]])  

Any rules specified by a specific node will override **defaults** specified in the top level **style** key.  If style rules conflict with rules handed down from the top level, rules attached to the node directly will always take priority.  

#### OptionalNodeData
(optional)[value, dictionary, or list]    
Each node can contain an arbitrary number of objects which are all optional and can refer to a dictionary, or primitives as a list or single value.  All optional data related to a specific node instance is stored under the top level of that node object (e.g. next to **\_id** and **nodeStyle**, etc.) .  The purpose is to support data across different data sources and nuanced property graph data models.  For instance, a Neo4j user might store a **labels** list and a **properties** dictionary under each node (e.g. `"properties":{..,},"labels":[...]`).  A Titan user might store a **type** key value and a **properties** dictionary (e.g. `"properties":{...}, "type": "value"`).  Additionally, a user may even choose to store all optional node data as top-level key-values under the node directly (e.g. `{"name":..., "age":..., "hometown":...}`).

The optional objects held by nodes can be shared in common with other nodes or can be unique to the node holding them - for instance, `"firstName"`, `"app\_id"`, `"genre"`, `"title"`, `"category"`, `"properties"`, `"type"`, etc.  These objects can serve any number of purposes in the application layer for analytics, filtering of the data, etc.    

GraphJSON takes into account that their are nuanced differences in how underlying Graph Databases, Graph compute engines, document stores, and even relational databases store and classify nodes and edges.  Often times a high-fidelity property Graph model is able to take into account the end user experience, research question, or business value being created.  However, one of the key problems GraphJSON solves, is the inherent gap between the data model and the applications that leverage the data model.  We believe this is the best way to leave open maximum flexibility to the different users, while maintaining a standard - [feedback welcome](mailto:feedback@graphalchemist.com).
