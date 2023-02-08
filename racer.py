import wikipediaapi
import networkx as nx
import heapq
import json

# initialize Wikipedia API
wiki = wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI
    )

# create an empty graph
G = nx.Graph()

# function to find all links within a Wikipedia article
def find_links(page_title):
    page = wiki.page(page_title)
    links = []
    if page.exists():
        for link in page.links.keys():
            links.append(link)
    return links

# function to create a graph of Wikipedia articles
def create_graph(start_page, end_page):
    visited = set()
    # for node in G.nodes:
    #     visited.add(node)
    queue = [(0, start_page)]
    while queue:
        print(f'visited: {visited}')
        dist, page_title = heapq.heappop(queue)
        if page_title not in visited:
            visited.add(page_title)
            G.add_node(page_title)
            links = find_links(page_title)
            for link in links:
                G.add_edge(page_title, link)
                heapq.heappush(queue, (dist+1, link))
                if link == end_page:
                    return

def save_graph(graph, filepath):
    """Save a NetworkX graph to a file in JSON format."""
    nx.write_adjlist(graph, filepath)

def load_graph(filepath):
    """Load a NetworkX graph from a file in JSON format."""
    nx.read_adjlist(filepath)

# example usage
start_page = "Jesus"
end_page = "Bagel"
G = nx.read_adjlist("graphs/wiki.txt")
if start_page not in G or end_page not in G:    
    create_graph(start_page, end_page)
# calculate shortest path between two articles using A* search
shortest_path = nx.astar_path(G, start_page, end_page)
print(shortest_path)
save_graph(G, "graphs/wiki.txt")
