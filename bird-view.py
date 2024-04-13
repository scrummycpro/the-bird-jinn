import osmnx as ox
import osmnx as ox
import matplotlib.pyplot as plt

# Define the location (neighborhood or area) you want to retrieve
place_name = "2101 Jade Creek Street, Las Vegas, Nevada, USA"  # Or replace with the name of your desired location

# Specify the maximum distance from the center of the location (in meters)
distance = 1000  # Adjust this value as needed

# Get the latitude and longitude of the place
location = ox.geocode(place_name)

# Retrieve the walking network for the specified location within the specified distance
G = ox.graph_from_point(location, dist=distance, network_type='walk')

# Plot the walking paths with a pinpoint
fig, ax = ox.plot_graph(G, show=False, close=False, bgcolor='w', edge_color='k')

# Add a pinpoint
ax.scatter(location[1], location[0], c='r', s=100, marker='o', edgecolor='k', zorder=5)

# Add a title
plt.title("Walking Paths in the Vicinity of 2101 Jade Creek Street, Las Vegas")

# Show the plot
plt.show()

