---
---

## edges
(optional)[list]    
The connections between **nodes**, **edges** objects take on a similar data structure as the **nodes**themselves. Each edge can have only one source and one target node.  Edges are always directed, meaning that source and target nodes are always specified using `\_source` and `\_target`.  Depending on the use case, the 'direction' of the edge may or may not be relevant.  Edges *do not* need to be specified in both directions, unless the underlying data model needs them to be. If bidirectionality is more natural to the data model, this can be taken care of with the **bidirectional** key in [**edgeStyle**](#edgestyle_2).  For instance, *"friends"* on Facebook will always be specified with a **source** and **target** node, even though we know the edge is 'reciprocal' and it is not relevant which node is target and which is source.  Meanwhile, in the context of the Twitter Graph, the source and target nodes are extremely important to the "follows" relationship and can have important implications for the analytics and visualizations generated from the data.

Additionally, Graphs can contain disconnected nodes, and so strictly speaking, edge dictionaries are in fact NOT required for all nodes in a GraphJSON object.

Each edge should hold the following top level keys:
* **\_source**
* **\_target**
* **caption**
* **edgeStyle**
* **{optional\_edge\_data}**

Typical edges:
{% highlight json %}
{"edges":[
    {"_source": 10,
    "_target": 12,
    "caption": "worked at",
    "type" : "WORKED_AT",
    "properties": {
        "start_date": "10-13-2009",
        "end_date": "4-15-2012",
        "is_current": false,
        "title": "Supervisor",
        "duties": ["Managing TPS Reports", "Drinking coffee", "Writing Documentation"]}
    },
    {"_source": 10,
    "_target": 203,
    "caption": "worked at",
    "type": "WORKED_AT",
    "properties" {
        "start_date": "5-13-2012",
        "is_current": true,
        "title": "Managing Supervisor of Supervisors",
        "duties": ["Managing Manager TPS Reports", "Drinking coffee"],
        "edge_properties_can_store_anything": true}
    }]
}
{% endhighlight json %}
### usage

#### \_source 
(required)[integer or string]    
A string or integer and must be unique within the GraphJSON object.  Additionally, **\_source** must be identical to the value passed to **\_id** to the corresponding **source** node.

#### \_target 
(required)[integer or string]    
A string or integer and must be unique within the GraphJSON object.  Additionally, **target** must be identical to the value passed to **\_id** for the corresponding **target** node.

#### OptionalEdgeData
(optional)[value, dictionary, or list]    
Just like the **nodes**, **edges** can contain an arbitrary number of objects which are all optional and can refer to a dictionary, or to primitives as a list or single value.  A Neo4j user might store a **properties** dictionary and a **type** key value in the edge object.  For example, `...{..."type": "...", "properties":{...}...}...`.  A Titan user might store a **label** key value and a **properties** dictionary.  For example, `...{"label":...,"properties":{...}...}...`.  Just like with nodes, a user may even choose to store all data as top-level key-values e.g. `...{"start\_time":..., "isCurrent":..., "weight":...,...}...`.

#### edgeStyle
(optional)[dictionary]    
The **edgeStyle** object attached to a specific **edge** will apply style rules to that edge only.  **edgeStyle** contains rules that can be defined with all of the same parameters that the top level **edgeStyle** dictionary carries.  
Any rules specified by a specific edge will override *defaults* specified in the top level **style** object.  If style rules conflict with rules handed down from the top level, rules attached to the edge directly will always take priority.
