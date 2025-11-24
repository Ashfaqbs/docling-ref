## Contents

move to sidebar

hide

- [(Top)](#)
- [1 Operations](#Operations)
- [2 Common data structures for graph representation](#Common_data_structures_for_graph_representation) Toggle Common data structures for graph representation subsection
    - [2.1 More efficient representation of adjacency sets](#More_efficient_representation_of_adjacency_sets)
- [3 Parallel representations](#Parallel_representations) Toggle Parallel representations subsection
    - [3.1 Shared memory](#Shared_memory)
    - [3.2 Distributed memory](#Distributed_memory)
- [4 Compressed representations](#Compressed_representations)
- [5 Applications of Graphs](#Applications_of_Graphs) Toggle Applications of Graphs subsection
    - [5.1 Breadth first search and depth first search](#Breadth_first_search_and_depth_first_search)
    - [5.2 Pathfinding](#Pathfinding)
- [6 See also](#See_also)
- [7 References](#References)
- [8 External links](#External_links)

Toggle the table of contents

# Graph (abstract data type)

25 languages

- [العربية](https://ar.wikipedia.org/wiki/%D8%A8%D9%8A%D8%A7%D9%86_(%D9%86%D9%88%D8%B9_%D8%A8%D9%8A%D8%A7%D9%86%D8%A7%D8%AA))
- [Български](https://bg.wikipedia.org/wiki/%D0%93%D1%80%D0%B0%D1%84_(%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B0_%D0%BE%D1%82_%D0%B4%D0%B0%D0%BD%D0%BD%D0%B8))
- [Bosanski](https://bs.wikipedia.org/wiki/Grafovi)
- [Català](https://ca.wikipedia.org/wiki/Graf_(estructura_de_dades))
- [Ελληνικά](https://el.wikipedia.org/wiki/%CE%93%CF%81%CE%AC%CF%86%CE%B7%CE%BC%CE%B1_(%CE%B1%CF%86%CE%B7%CF%81%CE%B7%CE%BC%CE%AD%CE%BD%CE%BF%CF%82_%CF%84%CF%8D%CF%80%CE%BF%CF%82_%CE%B4%CE%B5%CE%B4%CE%BF%CE%BC%CE%AD%CE%BD%CF%89%CE%BD))
- [Español](https://es.wikipedia.org/wiki/Grafo_(tipo_de_dato_abstracto))
- [Esperanto](https://eo.wikipedia.org/wiki/Reprezentado_de_grafeo)
- [فارسی](https://fa.wikipedia.org/wiki/%DA%AF%D8%B1%D8%A7%D9%81_(%D8%B3%D8%A7%D8%AE%D8%AA%D8%A7%D8%B1_%D8%AF%D8%A7%D8%AF%D9%87))
- [Français](https://fr.wikipedia.org/wiki/Graphe_(type_abstrait))
- [한국어](https://ko.wikipedia.org/wiki/%EA%B7%B8%EB%9E%98%ED%94%84_(%EC%9E%90%EB%A3%8C_%EA%B5%AC%EC%A1%B0))
- [Hrvatski](https://hr.wikipedia.org/wiki/Graf_(struktura_podataka))
- [Italiano](https://it.wikipedia.org/wiki/Grafo_(tipo_di_dato_astratto))
- [Lietuvių](https://lt.wikipedia.org/wiki/Grafas_(duomen%C5%B3_strukt%C5%ABra))
- [日本語](https://ja.wikipedia.org/wiki/%E3%82%B0%E3%83%A9%E3%83%95_(%E3%83%87%E3%83%BC%E3%82%BF%E6%A7%8B%E9%80%A0))
- [Polski](https://pl.wikipedia.org/wiki/Reprezentacja_grafu)
- [Português](https://pt.wikipedia.org/wiki/Grafo_(tipo_de_dado_abstrato))
- [Русский](https://ru.wikipedia.org/wiki/%D0%93%D1%80%D0%B0%D1%84_(%D1%82%D0%B8%D0%BF_%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85))
- [Српски / srpski](https://sr.wikipedia.org/wiki/%D0%93%D1%80%D0%B0%D1%84_(%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B0_%D0%BF%D0%BE%D0%B4%D0%B0%D1%82%D0%B0%D0%BA%D0%B0))
- [Srpskohrvatski / српскохрватски](https://sh.wikipedia.org/wiki/Graf_(struktura_podataka))
- [Svenska](https://sv.wikipedia.org/wiki/Graf_(datastruktur))
- [Tagalog](https://tl.wikipedia.org/wiki/Grap_(uri_ng_datos))
- [ไทย](https://th.wikipedia.org/wiki/%E0%B8%81%E0%B8%A3%E0%B8%B2%E0%B8%9F_(%E0%B9%81%E0%B8%9A%E0%B8%9A%E0%B8%8A%E0%B8%99%E0%B8%B4%E0%B8%94%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%A1%E0%B8%B9%E0%B8%A5%E0%B8%99%E0%B8%B2%E0%B8%A1%E0%B8%98%E0%B8%A3%E0%B8%A3%E0%B8%A1))
- [Українська](https://uk.wikipedia.org/wiki/%D0%93%D1%80%D0%B0%D1%84_(%D0%B0%D0%B1%D1%81%D1%82%D1%80%D0%B0%D0%BA%D1%82%D0%BD%D0%B8%D0%B9_%D1%82%D0%B8%D0%BF_%D0%B4%D0%B0%D0%BD%D0%B8%D1%85))
- [粵語](https://zh-yue.wikipedia.org/wiki/%E5%9C%96_(%E6%8A%BD%E8%B1%A1%E8%B3%87%E6%96%99%E9%A1%9E%E5%9E%8B))
- [中文](https://zh.wikipedia.org/wiki/%E5%9B%BE_(%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84))

[Edit links](https://www.wikidata.org/wiki/Special:EntityPage/Q2479726#sitelinks-wikipedia)

- [Article](\wiki\Graph_(abstract_data_type))
- [Talk](\wiki\Talk:Graph_(abstract_data_type))

English

- [Read](\wiki\Graph_(abstract_data_type))
- [Edit](\w\index.php?title=Graph_(abstract_data_type)&action=edit)
- [View history](\w\index.php?title=Graph_(abstract_data_type)&action=history)

Tools

Tools

move to sidebar

hide

Actions

- [Read](\wiki\Graph_(abstract_data_type))
- [Edit](\w\index.php?title=Graph_(abstract_data_type)&action=edit)
- [View history](\w\index.php?title=Graph_(abstract_data_type)&action=history)

General

- [What links here](\wiki\Special:WhatLinksHere\Graph_(abstract_data_type))
- [Related changes](\wiki\Special:RecentChangesLinked\Graph_(abstract_data_type))
- [Upload file](https://en.wikipedia.org/wiki/Wikipedia:File_Upload_Wizard)
- [Permanent link](\w\index.php?title=Graph_(abstract_data_type)&oldid=1322467391)
- [Page information](\w\index.php?title=Graph_(abstract_data_type)&action=info)
- [Cite this page](\w\index.php?title=Special:CiteThisPage&page=Graph_%28abstract_data_type%29&id=1322467391&wpFormIdentifier=titleform)
- [Get shortened URL](\w\index.php?title=Special:UrlShortener&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FGraph_%28abstract_data_type%29)
- [Download QR code](\w\index.php?title=Special:QrCode&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FGraph_%28abstract_data_type%29)

Print/export

- [Download as PDF](\w\index.php?title=Special:DownloadAsPdf&page=Graph_%28abstract_data_type%29&action=show-download-screen)
- [Printable version](\w\index.php?title=Graph_(abstract_data_type)&printable=yes)

In other projects

- [Wikimedia Commons](https://commons.wikimedia.org/wiki/Category:Graph_(abstract_data_type))
- [Wikidata item](https://www.wikidata.org/wiki/Special:EntityPage/Q2479726)

Appearance

move to sidebar

hide

From Wikipedia, the free encyclopedia

Abstract data type in computer science

A directed graph with three vertices (blue circles) and three edges (black arrows).

<!-- image -->

In [computer science](\wiki\Computer_science) , a **graph** is an [abstract data type](\wiki\Abstract_data_type) that is meant to implement the [undirected graph](\wiki\Graph_(discrete_mathematics)) and [directed graph](\wiki\Directed_graph) concepts from the field of [graph theory](\wiki\Graph_theory) within [mathematics](\wiki\Mathematics) .

A graph data structure consists of a finite (and possibly mutable) [set](\wiki\Set_(computer_science)) of *vertices* (also called *nodes* or *points* ), together with a set of unordered pairs of these vertices for an undirected graph or a set of ordered pairs for a directed graph. These pairs are known as *edges* (also called *links* or *lines* ), and for a directed graph are also known as *edges* but also sometimes *arrows* or *arcs* . The vertices may be part of the graph structure, or may be external entities represented by integer indices or [references](\wiki\Reference_(computer_science)) .

A graph data structure may also associate to each edge some *edge value* , such as a symbolic label or a numeric attribute (cost, capacity, length, etc.).

## Operations

[ [edit](\w\index.php?title=Graph_(abstract_data_type)&action=edit&section=1) ]

UML class diagram of a Graph (abstract data type)

<!-- image -->

The basic operations provided by a graph data structure *G* usually include: [[ 1 ]](#cite_note-gt-ops-1)

- adjacent( *G* , *x* , *y* ) : tests whether there is an edge from the vertex *x* to the vertex *y* ;
- neighbors( *G* , *x* ) : lists all vertices *y* such that there is an edge from the vertex *x* to the vertex *y* ;
- add\_vertex( *G* , *x* ) : adds the vertex *x* , if it is not there;
- remove\_vertex( *G* , *x* ) : removes the vertex *x* , if it is there;
- add\_edge( *G* , *x* , *y* , *z* ) : adds the edge *z* from the vertex *x* to the vertex *y* , if it is not there;
- remove\_edge( *G* , *x* , *y* ) : removes the edge from the vertex *x* to the vertex *y* , if it is there;
- get\_vertex\_value( *G* , *x* ) : returns the value associated with the vertex *x* ;
- set\_vertex\_value( *G* , *x* , *v* ) : sets the value associated with the vertex *x* to *v* .

Structures that associate values to the edges usually also provide: [[ 1 ]](#cite_note-gt-ops-1)

- get\_edge\_value( *G* , *x* , *y* ) : returns the value associated with the edge ( *x* , *y* );
- set\_edge\_value( *G* , *x* , *y* , *v* ) : sets the value associated with the edge ( *x* , *y* ) to *v* .

## Common data structures for graph representation

[ [edit](\w\index.php?title=Graph_(abstract_data_type)&action=edit&section=2) ]

[Adjacency list](\wiki\Adjacency_list) [[ 2 ]](#cite_note-2)

Vertices are stored as records or objects, and every vertex stores a

[list](\wiki\List_(computing)) of adjacent vertices. This data structure allows the storage of additional data on the vertices. Additional data can be stored if edges are also stored as objects, in which case each vertex stores its incident edges and each edge stores its incident vertices.

[Adjacency matrix](\wiki\Adjacency_matrix) [[ 3 ]](#cite_note-3)

A two-dimensional matrix, in which the rows represent source vertices and columns represent destination vertices. Data on edges and vertices must be stored externally. Only the cost for one edge can be stored between each pair of vertices.

[Incidence matrix](\wiki\Incidence_matrix) [[ 4 ]](#cite_note-4)

A two-dimensional matrix, in which the rows represent the vertices and columns represent the edges. The entries indicate the incidence relation between the vertex at a row and edge at a column.

The following table gives the [time complexity](\wiki\Time_complexity) cost of performing various operations on graphs, for each of these representations, with | *V* | the number of vertices and | *E* | the number of edges. [ [*citation needed*](\wiki\Wikipedia:Citation_needed) ] In the matrix representations, the entries encode the cost of following an edge. The cost of edges that are not present are assumed to be ∞.

|                                                                                          | Adjacency list                                                                                       | Adjacency matrix                                                                            | Incidence matrix                                                                                               |
|------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Store graph                                                                              | O  (  |  V  |  +  |  E  |  )  {\displaystyle O(|V|+|E|)}  {\displaystyle O(|V|+|E|)}  <!-- image --> | O  (  |  V  |  2  )  {\displaystyle O(|V|^{2})}  {\displaystyle O(|V|^{2})}  <!-- image --> | O  (  |  V  |  ⋅  |  E  |  )  {\displaystyle O(|V|\cdot |E|)}  {\displaystyle O(|V|\cdot |E|)}  <!-- image --> |
| Add vertex                                                                               | O  (  1  )  {\displaystyle O(1)}  {\displaystyle O(1)}  <!-- image -->                               | O  (  |  V  |  2  )  {\displaystyle O(|V|^{2})}  {\displaystyle O(|V|^{2})}  <!-- image --> | O  (  |  V  |  ⋅  |  E  |  )  {\displaystyle O(|V|\cdot |E|)}  {\displaystyle O(|V|\cdot |E|)}  <!-- image --> |
| Add edge                                                                                 | O  (  1  )  {\displaystyle O(1)}  {\displaystyle O(1)}  <!-- image -->                               | O  (  1  )  {\displaystyle O(1)}  {\displaystyle O(1)}  <!-- image -->                      | O  (  |  V  |  ⋅  |  E  |  )  {\displaystyle O(|V|\cdot |E|)}  {\displaystyle O(|V|\cdot |E|)}  <!-- image --> |
| Remove vertex                                                                            | O  (  |  E  |  )  {\displaystyle O(|E|)}  {\displaystyle O(|E|)}  <!-- image -->                     | O  (  |  V  |  2  )  {\displaystyle O(|V|^{2})}  {\displaystyle O(|V|^{2})}  <!-- image --> | O  (  |  V  |  ⋅  |  E  |  )  {\displaystyle O(|V|\cdot |E|)}  {\displaystyle O(|V|\cdot |E|)}  <!-- image --> |
| Remove edge                                                                              | O  (  |  V  |  )  {\displaystyle O(|V|)}  {\displaystyle O(|V|)}  <!-- image -->                     | O  (  1  )  {\displaystyle O(1)}  {\displaystyle O(1)}  <!-- image -->                      | O  (  |  V  |  ⋅  |  E  |  )  {\displaystyle O(|V|\cdot |E|)}  {\displaystyle O(|V|\cdot |E|)}  <!-- image --> |
| Are vertices  *x*  and  *y*  adjacent (assuming that their storage positions are known)? | O  (  |  V  |  )  {\displaystyle O(|V|)}  {\displaystyle O(|V|)}  <!-- image -->                     | O  (  1  )  {\displaystyle O(1)}  {\displaystyle O(1)}  <!-- image -->                      | O  (  |  E  |  )  {\displaystyle O(|E|)}  {\displaystyle O(|E|)}  <!-- image -->                               |
| Remarks                                                                                  | Slow to remove vertices and edges, because it needs to find all vertices or edges                    | Slow to add or remove vertices, because matrix must be resized/copied                       | Slow to add or remove vertices and edges, because matrix must be resized/copied                                |

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

Adjacency lists are generally preferred for the representation of [sparse graphs](\wiki\Sparse_graph) , while an adjacency matrix is preferred if the graph is dense; that is, the number of edges | E | {\displaystyle |E|} is close to the number of vertices squared, | V | 2 {\displaystyle |V|^{2}} , or if one must be able to quickly look up if there is an edge connecting two vertices. [[ 5 ]](#cite_note-clrs-5) [[ 6 ]](#cite_note-gt-6)

{\displaystyle |E|}

<!-- image -->

{\displaystyle |V|^{2}}

<!-- image -->

### More efficient representation of adjacency sets

[ [edit](\w\index.php?title=Graph_(abstract_data_type)&action=edit&section=3) ]

The time complexity of operations in the adjacency list representation can be improved by storing the sets of adjacent vertices in more efficient data structures, such as [hash tables](\wiki\Hash_table) or [balanced binary search trees](\wiki\Binary_search_tree#Balanced_binary_search_trees) (the latter representation requires that vertices are identified by elements of a linearly ordered set, such as integers or character strings). A representation of adjacent vertices via hash tables leads to an [amortized](\wiki\Amortized_analysis) average time complexity of O ( 1 ) {\displaystyle O(1)} to test adjacency of two given vertices and to remove an edge and an [amortized](\wiki\Amortized_analysis) average time complexity [[ 7 ]](#cite_note-Cormen_et_al_p253-280_(hashtable)-7) of O ( deg ⁡ ( x ) ) {\displaystyle O(\deg(x))} to remove a given vertex x of degree deg ⁡ ( x ) {\displaystyle \deg(x)} . The time complexity of the other operations and the asymptotic space requirement do not change.

{\displaystyle O(1)}

<!-- image -->

{\displaystyle O(\deg(x))}

<!-- image -->

{\displaystyle \deg(x)}

<!-- image -->

## Parallel representations

[ [edit](\w\index.php?title=Graph_(abstract_data_type)&action=edit&section=4) ]

The parallelization of graph problems faces significant challenges: Data-driven computations, unstructured problems, poor locality and high data access to computation ratio. [[ 8 ]](#cite_note-Bader2013-8) [[ 9 ]](#cite_note-9) The graph representation used for parallel architectures plays a significant role in facing those challenges. Poorly chosen representations may unnecessarily drive up the communication cost of the algorithm, which will decrease its [scalability](\wiki\Scalability) . In the following, shared and distributed memory architectures are considered.

### Shared memory

[ [edit](\w\index.php?title=Graph_(abstract_data_type)&action=edit&section=5) ]

In the case of a [shared memory](\wiki\Shared_memory) model, the graph representations used for parallel processing are the same as in the sequential case, [[ 10 ]](#cite_note-Sanders2019-10) since parallel read-only access to the graph representation (e.g. an [adjacency list](\wiki\Adjacency_list) ) is efficient in shared memory.

### Distributed memory

[ [edit](\w\index.php?title=Graph_(abstract_data_type)&action=edit&section=6) ]

In the [distributed memory](\wiki\Distributed_memory) model, the usual approach is to [partition](\wiki\Graph_partition) the vertex set V {\displaystyle V} of the graph into p {\displaystyle p} sets V 0 , ... , V p − 1 {\displaystyle V\_{0},\dots ,V\_{p-1}} . Here, p {\displaystyle p} is the amount of available processing elements (PE). The vertex set partitions are then distributed to the PEs with matching index, additionally to the corresponding edges. Every PE has its own [subgraph](\wiki\Subgraph_(graph_theory)) representation, where edges with an endpoint in another partition require special attention. For standard communication interfaces like [MPI](\wiki\Message_Passing_Interface) , the ID of the PE owning the other endpoint has to be identifiable. During computation in a distributed graph algorithms, passing information along these edges implies communication. [[ 10 ]](#cite_note-Sanders2019-10)

{\displaystyle V}

<!-- image -->

{\displaystyle p}

<!-- image -->

{\displaystyle V\_{0},\dots ,V\_{p-1}}

<!-- image -->

{\displaystyle p}

<!-- image -->

[Partitioning the graph](\wiki\Graph_partition) needs to be done carefully - there is a trade-off between low communication and even size partitioning [[ 11 ]](#cite_note-11) But partitioning a graph is a NP-hard problem, so it is not feasible to calculate them. Instead, the following heuristics are used.

1D partitioning: Every processor gets n / p {\displaystyle n/p} vertices and the corresponding outgoing edges. This can be understood as a row-wise or column-wise decomposition of the adjacency matrix. For algorithms operating on this representation, this requires an All-to-All communication step as well as O ( m ) {\displaystyle {\mathcal {O}}(m)} message buffer sizes, as each PE potentially has outgoing edges to every other PE. [[ 12 ]](#cite_note-Buluc2011-12)

{\displaystyle n/p}

<!-- image -->

{\displaystyle {\mathcal {O}}(m)}

<!-- image -->

2D partitioning: Every processor gets a submatrix of the adjacency matrix. Assume the processors are aligned in a rectangle p = p r × p c {\displaystyle p=p\_{r}\times p\_{c}} , where p r {\displaystyle p\_{r}} and p c {\displaystyle p\_{c}} are the amount of processing elements in each row and column, respectively. Then each processor gets a [submatrix](\wiki\Submatrix) of the adjacency matrix of dimension ( n / p r ) × ( n / p c ) {\displaystyle (n/p\_{r})\times (n/p\_{c})} . This can be visualized as a [checkerboard](\wiki\Checkerboard) pattern in a matrix. [[ 12 ]](#cite_note-Buluc2011-12) Therefore, each processing unit can only have outgoing edges to PEs in the same row and column. This bounds the amount of communication partners for each PE to p r + p c − 1 {\displaystyle p\_{r}+p\_{c}-1} out of p = p r × p c {\displaystyle p=p\_{r}\times p\_{c}} possible ones.

{\displaystyle p=p\_{r}\times p\_{c}}

<!-- image -->

{\displaystyle p\_{r}}

<!-- image -->

{\displaystyle p\_{c}}

<!-- image -->

{\displaystyle (n/p\_{r})\times (n/p\_{c})}

<!-- image -->

{\displaystyle p\_{r}+p\_{c}-1}

<!-- image -->

{\displaystyle p=p\_{r}\times p\_{c}}

<!-- image -->

## Compressed representations

[ [edit](\w\index.php?title=Graph_(abstract_data_type)&action=edit&section=7) ]

Graphs with trillions of edges occur in [machine learning](\wiki\Machine_learning) , [social network analysis](\wiki\Social_network_analysis) , and other areas. [Compressed](\wiki\Data_compression) graph representations have been developed to reduce I/O and memory requirements. General techniques such as [Huffman coding](\wiki\Huffman_coding) are applicable, but the adjacency list or adjacency matrix can be processed in specific ways to increase efficiency. [[ 13 ]](#cite_note-13)

## Applications of Graphs

[ [edit](\w\index.php?title=Graph_(abstract_data_type)&action=edit&section=8) ]

### Breadth first search and depth first search

[ [edit](\w\index.php?title=Graph_(abstract_data_type)&action=edit&section=9) ]

[Breadth-first search](\wiki\Breadth-first_search) (BFS) and [depth-first search](\wiki\Depth-first_search) (DFS) are two closely related approaches that are used for exploring all of the nodes in a given [connected component](\wiki\Connected_component_(graph_theory)) . Both start with an arbitrary node, the " [root](\wiki\Root_(graph_theory)) ". [[ 14 ]](#cite_note-Purti-14) [Strongly connected components](\wiki\Strongly_connected_component) can also be found using graph traversals using algorithms such as [Kosaraju's algorithm](\wiki\Kosaraju%27s_algorithm) , which is a modified DFS.

### Pathfinding

[ [edit](\w\index.php?title=Graph_(abstract_data_type)&action=edit&section=10) ]

[Dijkstra's Algorithm](\wiki\Dijkstra%27s_algorithm) is a [Pathfinding Algorithm](\wiki\Pathfinding) that can be used on a positively-weighted (meaning all edge weights must be greater than or equal to 0) and/or directed graphs. This can be used to find the shortest path between two arbitrarily chosen nodes which is commonly applied in  routing problems.

## See also

[ [edit](\w\index.php?title=Graph_(abstract_data_type)&action=edit&section=11) ]

- [Graph traversal](\wiki\Graph_traversal) for more information on graph walking strategies
- [Graph database](\wiki\Graph_database) for graph (data structure) persistency
- [Graph rewriting](\wiki\Graph_rewriting) for rule based transformations of graphs (graph data structures)
- [Graph drawing software](\wiki\Graph_drawing_software) for software, systems, and providers of systems for drawing graphs

## References

[ [edit](\w\index.php?title=Graph_(abstract_data_type)&action=edit&section=12) ]

1. ^ [***a***](#cite_ref-gt-ops_1-0) [***b***](#cite_ref-gt-ops_1-1) See, e.g. [Goodrich &amp; Tamassia (2015)](#CITEREFGoodrichTamassia2015) , Section 13.1.2: Operations on graphs, p. 360. For a more detailed set of operations, see [Mehlhorn, K.](\wiki\Kurt_Mehlhorn) ; Näher, S. (1999). "Chapter 6: Graphs and their data structures". [*LEDA: A platform for combinatorial and geometric computing*](https://people.mpi-inf.mpg.de/~mehlhorn/ftp/LEDAbook/Graphs.pdf) (PDF) . Cambridge University Press. pp. 240- 282.
2. [**^**](#cite_ref-2) [Cormen et al. (2001)](#CITEREFCormenLeisersonRivestStein2001) , pp. 528-529; [Goodrich &amp; Tamassia (2015)](#CITEREFGoodrichTamassia2015) , pp. 361-362.
3. [**^**](#cite_ref-3) [Cormen et al. (2001)](#CITEREFCormenLeisersonRivestStein2001) , pp. 529-530; [Goodrich &amp; Tamassia (2015)](#CITEREFGoodrichTamassia2015) , p. 363.
4. [**^**](#cite_ref-4) [Cormen et al. (2001)](#CITEREFCormenLeisersonRivestStein2001) , Exercise 22.1-7, p. 531.
5. [**^**](#cite_ref-clrs_5-0) [Cormen, Thomas H.](\wiki\Thomas_H._Cormen) ; [Leiserson, Charles E.](\wiki\Charles_E._Leiserson) ; [Rivest, Ronald L.](\wiki\Ronald_L._Rivest) ; [Stein, Clifford](\wiki\Clifford_Stein) (2001). "Section 22.1: Representations of graphs". [*Introduction to Algorithms*](\wiki\Introduction_to_Algorithms) (Second ed.). MIT Press and McGraw-Hill. pp. 527- 531. [ISBN](\wiki\ISBN_(identifier)) [0-262-03293-7](\wiki\Special:BookSources\0-262-03293-7) .
6. [**^**](#cite_ref-gt_6-0) [Goodrich, Michael T.](\wiki\Michael_T._Goodrich) ; [Tamassia, Roberto](\wiki\Roberto_Tamassia) (2015). "Section 13.1: Graph terminology and representations". *Algorithm Design and Applications* . Wiley. pp. 355- 364. [ISBN](\wiki\ISBN_(identifier)) [978-1-118-33591-8](\wiki\Special:BookSources\978-1-118-33591-8) .
7. [**^**](#cite_ref-Cormen_et_al_p253-280_(hashtable)_7-0) [Cormen, Thomas H.](\wiki\Thomas_H._Cormen) ; [Leiserson, Charles E.](\wiki\Charles_E._Leiserson) ; [Rivest, Ronald L.](\wiki\Ronald_L._Rivest) ; [Stein, Clifford](\wiki\Clifford_Stein) (2009). [*Introduction to Algorithms*](\wiki\Introduction_to_Algorithms) (3rd ed.). Massachusetts Institute of Technology. pp. 253- 280. [ISBN](\wiki\ISBN_(identifier)) [978-0-262-03384-8](\wiki\Special:BookSources\978-0-262-03384-8) .
8. [**^**](#cite_ref-Bader2013_8-0) Bader, David; Meyerhenke, Henning; Sanders, Peter; Wagner, Dorothea (January 2013). [*Graph Partitioning and Graph Clustering*](https://www.ams.org/conm/588/) . Contemporary Mathematics. Vol. 588. American Mathematical Society. [doi](\wiki\Doi_(identifier)) : [10.1090/conm/588/11709](https://doi.org/10.1090%2Fconm%2F588%2F11709) . [ISBN](\wiki\ISBN_(identifier)) [978-0-8218-9038-7](\wiki\Special:BookSources\978-0-8218-9038-7) .
9. [**^**](#cite_ref-9) Lumsdaine, Andrew; Gregor, Douglas; Hendrickson, Bruce; Berry, Jonathan (March 2007). "Challenges in Parallel Graph Processing". *Parallel Processing Letters* . **17** (1): 5- 20. [doi](\wiki\Doi_(identifier)) : [10.1142/s0129626407002843](https://doi.org/10.1142%2Fs0129626407002843) . [ISSN](\wiki\ISSN_(identifier)) [0129-6264](https://search.worldcat.org/issn/0129-6264) .
10. ^ [***a***](#cite_ref-Sanders2019_10-0) [***b***](#cite_ref-Sanders2019_10-1) Sanders, Peter; Mehlhorn, Kurt; Dietzfelbinger, Martin; Dementiev, Roman (2019). [*Sequential and Parallel Algorithms and Data Structures: The Basic Toolbox*](https://www.springer.com/gp/book/9783030252083) . Springer International Publishing. [ISBN](\wiki\ISBN_(identifier)) [978-3-030-25208-3](\wiki\Special:BookSources\978-3-030-25208-3) .
11. [**^**](#cite_ref-11) ["Parallel Processing of Graphs"](https://web.archive.org/web/20210825121127/https://www.graphengine.io/downloads/papers/ParallelProcessingOfGraphs.pdf) (PDF) . Archived from [the original](https://www.graphengine.io/downloads/papers/ParallelProcessingOfGraphs.pdf) (PDF) on 2021-08-25 . Retrieved 2020-03-09 .
12. ^ [***a***](#cite_ref-Buluc2011_12-0) [***b***](#cite_ref-Buluc2011_12-1) Buluç, A.; Madduri, Kamesh (2011). "Applications". *Parallel breadth-first search on distributed memory systems* . 2011 International Conference for High Performance Computing, Networking, Storage and Analysis. [CiteSeerX](\wiki\CiteSeerX_(identifier)) [10.1.1.767.5248](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.767.5248) . [doi](\wiki\Doi_(identifier)) : [10.1145/2063384.2063471](https://doi.org/10.1145%2F2063384.2063471) . [ISBN](\wiki\ISBN_(identifier)) [978-1-4503-0771-0](\wiki\Special:BookSources\978-1-4503-0771-0) . [S2CID](\wiki\S2CID_(identifier)) [6540738](https://api.semanticscholar.org/CorpusID:6540738) .
13. [**^**](#cite_ref-13) Besta, Maciej; Hoefler, Torsten (27 April 2019). "Survey and Taxonomy of Lossless Graph Compression and Space-Efficient Graph Representations". [arXiv](\wiki\ArXiv_(identifier)) : [1806.01799](https://arxiv.org/abs/1806.01799) [ [cs.DS](https://arxiv.org/archive/cs.DS) ].
14. [**^**](#cite_ref-Purti_14-0) Purti (July-September 2018). ["Graph Traversals and its Applications"](http://ijrar.com/upload_issue/ijrar_issue_1836.pdf) (PDF) . *International Journal of Research and Analytical Reviews* . **5** (3): 2.

## External links

[ [edit](\w\index.php?title=Graph_(abstract_data_type)&action=edit&section=13) ]

<!-- image -->

Wikimedia Commons has media related to [Graph (abstract data type)](https://commons.wikimedia.org/wiki/Category:Graph_(abstract_data_type)) .

- [Boost Graph Library: a powerful C++ graph library](http://www.boost.org/libs/graph) s.a. [Boost (C++ libraries)](\wiki\Boost_(C%2B%2B_libraries))
- [Networkx: a Python graph library](https://networkx.org/)
- [GraphMatcher](http://www.graphmatcher.com/) a java program to align directed/undirected graphs.
- [GraphBLAS](http://graphblas.org/) A specification for a library interface for operations on graphs, with a particular focus on sparse graphs.

| - [v](\wiki\Template:Graph_representations) - [t](\wiki\Template_talk:Graph_representations) - [e](\wiki\Special:EditPage\Template:Graph_representations)  Graph representations   |                                                                                                                                                                                                                                                                                            |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Data structures                                                                                                                                                                    | - Graph (abstract data type) - [Adjacency list](\wiki\Adjacency_list) - [Edge list](\wiki\Edge_list) - [Adjacency matrix](\wiki\Adjacency_matrix) - [Incidence matrix](\wiki\Incidence_matrix)                                                                                             |
| XML-based formats                                                                                                                                                                  | - [DGML](\wiki\DGML) - DotML - GEXF - [GraphML](\wiki\GraphML) - [GXL](\wiki\GXL) - [XGMML](\wiki\XGMML)                                                                                                                                                                                   |
| Text-based formats                                                                                                                                                                 | - [DOT](\wiki\DOT_(graph_description_language)) - [Graph Modelling Language](\wiki\Graph_Modelling_Language) (GML) - [LCF notation](\wiki\LCF_notation) for cubic Hamiltonian graphs - [Newick format](\wiki\Newick_format) for trees - [Trivial Graph Format](\wiki\Trivial_Graph_Format) |
| Related concepts                                                                                                                                                                   | - [Graph database](\wiki\Graph_database) - [Graph drawing](\wiki\Graph_drawing) - [Linked data](\wiki\Linked_data)                                                                                                                                                                         |

| - [v](\wiki\Template:Data_structures) - [t](\wiki\Template_talk:Data_structures) - [e](\wiki\Special:EditPage\Template:Data_structures)  [Data structures](\wiki\Data_structure)   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Types                                                                                                                                                                              | - [Collection](\wiki\Collection_(abstract_data_type)) - [Container](\wiki\Container_(abstract_data_type))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [Abstract](\wiki\Abstract_data_type)                                                                                                                                               | - [Associative array](\wiki\Associative_array)     - [Multimap](\wiki\Multimap)     - [Retrieval Data Structure](\wiki\Retrieval_Data_Structure) - [List](\wiki\List_(abstract_data_type)) - [Stack](\wiki\Stack_(abstract_data_type)) - [Queue](\wiki\Queue_(abstract_data_type))     - [Double-ended queue](\wiki\Double-ended_queue) - [Priority queue](\wiki\Priority_queue)     - [Double-ended priority queue](\wiki\Double-ended_priority_queue) - [Set](\wiki\Set_(abstract_data_type))     - [Multiset](\wiki\Set_(abstract_data_type)#Multiset)     - [Disjoint-set](\wiki\Disjoint-set_data_structure)                                                                                                                             |
| [Arrays](\wiki\Array_(data_structure))                                                                                                                                             | - [Bit array](\wiki\Bit_array) - [Circular buffer](\wiki\Circular_buffer) - [Dynamic array](\wiki\Dynamic_array) - [Hash table](\wiki\Hash_table) - [Hashed array tree](\wiki\Hashed_array_tree) - [Sparse matrix](\wiki\Sparse_matrix)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Linked](\wiki\Linked_data_structure)                                                                                                                                              | - [Association list](\wiki\Association_list) - [Linked list](\wiki\Linked_list) - [Skip list](\wiki\Skip_list) - [Unrolled linked list](\wiki\Unrolled_linked_list) - [XOR linked list](\wiki\XOR_linked_list)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Trees](\wiki\Tree_(data_structure))                                                                                                                                               | - [B-tree](\wiki\B-tree) - [Binary search tree](\wiki\Binary_search_tree)     - [AA tree](\wiki\AA_tree)     - [AVL tree](\wiki\AVL_tree)     - [Red-black tree](\wiki\Red%E2%80%93black_tree)     - [Self-balancing tree](\wiki\Self-balancing_binary_search_tree)     - [Splay tree](\wiki\Splay_tree) - [Heap](\wiki\Heap_(data_structure))     - [Binary heap](\wiki\Binary_heap)     - [Binomial heap](\wiki\Binomial_heap)     - [Fibonacci heap](\wiki\Fibonacci_heap) - [R-tree](\wiki\R-tree)     - [R* tree](\wiki\R*_tree)     - [R+ tree](\wiki\R%2B_tree)     - [Hilbert R-tree](\wiki\Hilbert_R-tree) - [Rope](\wiki\Rope_(data_structure)) - [Trie](\wiki\Trie)     - [Hash tree](\wiki\Hash_tree_(persistent_data_structure)) |
| Graphs                                                                                                                                                                             | - [Binary decision diagram](\wiki\Binary_decision_diagram) - [Directed acyclic graph](\wiki\Directed_acyclic_graph) - [Directed acyclic word graph](\wiki\Deterministic_acyclic_finite_state_automaton)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| - [List of data structures](\wiki\List_of_data_structures)                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

Retrieved from " [https://en.wikipedia.org/w/index.php?title=Graph\_(abstract\_data\_type)&amp;oldid=1322467391](https://en.wikipedia.org/w/index.php?title=Graph_(abstract_data_type)&oldid=1322467391) "

[Categories](\wiki\Help:Category)

:

- [Graph theory](\wiki\Category:Graph_theory)
- [Graph data structures](\wiki\Category:Graph_data_structures)
- [Abstract data types](\wiki\Category:Abstract_data_types)
- [Graphs](\wiki\Category:Graphs)
- [Hypergraphs](\wiki\Category:Hypergraphs)

Hidden categories:

- [Articles with short description](\wiki\Category:Articles_with_short_description)
- [Short description matches Wikidata](\wiki\Category:Short_description_matches_Wikidata)
- [All articles with unsourced statements](\wiki\Category:All_articles_with_unsourced_statements)
- [Articles with unsourced statements from November 2011](\wiki\Category:Articles_with_unsourced_statements_from_November_2011)
- [Commons category link from Wikidata](\wiki\Category:Commons_category_link_from_Wikidata)

Search

Search

Toggle the table of contents

Graph (abstract data type)

25 languages

[Add topic](#)