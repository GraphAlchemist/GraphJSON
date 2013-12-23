---
---
# GraphJSON
{:.no_toc}

A GraphJSON object must specify **nodes** in the top level, and can have an **edges** and **style** toplevel key.  Most GraphJSON objects will include **edges**, however they are optional because a GraphJSON object (while not mathematically sound) can contain unconnected nodes.  Hypothetically a GraphJSON object could consist of one, unconnected node, even though it would not be terribly useful.  Additionally, if **style** is not included, a graph derived from GraphJSON will simply inherit styles from the application.

{% include style.md %}
{% include nodes.md %}
{% include edges.md %}
