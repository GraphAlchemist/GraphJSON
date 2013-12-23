---
---
# Graphs are Everywhere
{:.no_toc}
Graphs are the most expressive and intuitive data structure.

GraphJSON documents are a standardized way to represent graph information, while keeping intact the expressiveness and elegance of the underlying data itself.

GraphJSON can be used to describe structural as well as stylistic features of graphs, regardless of the data domain or content.  The end goal is proliferation of meaningful graph representations of complex information through visualizations and analytics.  GraphJSON works towards this goal by creating a ubiquitous way to represent Graphs.

# Overview
{:.no_toc}

* The table of contents goes here!
{:toc}

## Definitions
{:.no_toc}
JavaScript Object Notation (JSON), and the terms object, name, value, array, and number, are defined in IETF RTC 4627,
at http://www.ietf.org/rfc/rfc4627.txt.

The key words "must", "must not", "required", "shall", "shall not", "should", "should not", "recommended", "may", and "optional" in this document are to be interpreted as described in IETF RFC 2119, at http://www.ietf.org/rfc/rfc2119.txt.

## High Level
GraphJSON refers to a well formatted JSON object.  GraphJSON can contain the bare minimum that it takes to construct a graph - the two top level keys: `nodes` and `edges` without any style information.  When an API or data service provides Graph JSON without any styles associated by the Graph are taken into account by the Applications defaults.  However, when it comes to conveying important information through graph visualization, style is incredibly important.  Additionally, since the graph visualizations are as generic and expressive as Geographic Maps, and Graph JSON provides a well defined framework for articulating important information related to how Graph data should be consumed for visualization.

In addition to `nodes` and `edges` *Complete GraphJSON* will also contain a top level `style` key that will implement graph styles, including layout, sizing, color, and other descriptive and style features for the entire Graph.    

A well formatted **GraphJSON** object *must* include the following top level keys:    
    `"nodes"`

Should contain:    
    `"edges"`

And may also include:   
    `"style"`

## Usage
GraphJSON objects can be used in a wide variety of situations.  Prototyping and designing small graphs for documentations, as an interchange format from a graph database like [Neo4j], [Titan], [Orient DB], for use in a Network analysis package like [Networkx], to be rendered in a visualization application like [Gephi], or even as documents within a document store.  Additionally, libraries are in the works to easily convert CSV, XML, or even traditional network files (like UCINET or Pajek) into GraphJSON files.

## Contributing
The GraphJSON contributors and graph community wholeheartedly invite you to weigh in on how the specifications can be made better.  Additionally, if you'd rather work on living breathing GraphJSON based applications, check out the following:
* [GraphJSON.io](graphjson.io)

## Thoughts
While `nodes` are sometimes referred to as "vertices", `edges` inherit even more of a naming controversy and can be referred to as "links", "lines", or "relationships".  We've chosen `nodes` and `edges` because they are a humane way to refer to the underlying data model, while remaining non-generic and unique to the graph world.  Feedback is welcome.
Thank you to the Authors of GeoJSON - GraphJSON is inspired in part by [GeoJSON](http://www.geojson.org/).
