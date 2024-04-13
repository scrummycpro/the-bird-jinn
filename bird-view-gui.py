import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import osmnx as ox
import matplotlib.pyplot as plt

def render_plot():
    place_name = place_entry.get()
    distance = 1000  # Adjust this value as needed

    location = ox.geocode(place_name)
    G = ox.graph_from_point(location, dist=distance, network_type='walk')

    fig, ax = ox.plot_graph(G, show=False, close=False, bgcolor='w', edge_color='k')
    ax.scatter(location[1], location[0], c='r', s=100, marker='o', edgecolor='k', zorder=5)

    plt.title(f"Walking Paths in the Vicinity of {place_name}")

    # Create a Figure object from Matplotlib
    fig = plt.gcf()

    # Clear the current Tkinter canvas (if any)
    for widget in plot_frame.winfo_children():
        widget.destroy()

    # Embed the Matplotlib plot into Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Adjust Tkinter window size based on plot size
    window.geometry(f"{fig.get_size_inches()[0] * 100}x{fig.get_size_inches()[1] * 100}")

def save_plot():
    file_path = tk.filedialog.asksaveasfilename(defaultextension=".png")
    if file_path:
        plt.savefig(file_path)

window = tk.Tk()
window.title("Map Viewer")

place_label = ttk.Label(window, text="Place:")
place_label.grid(row=0, column=0)

place_entry = ttk.Entry(window)
place_entry.grid(row=0, column=1)

render_button = ttk.Button(window, text="Render", command=render_plot)
render_button.grid(row=1, column=0)

save_button = ttk.Button(window, text="Save", command=save_plot)
save_button.grid(row=1, column=1)

# Frame to hold the plot
plot_frame = tk.Frame(window)
plot_frame.grid(row=2, columnspan=2)

window.mainloop()
