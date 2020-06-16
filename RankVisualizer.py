import matplotlib.pyplot as plt
import matplotlib as mpl
from os.path import join
import sys
import json

### Store path to folder containing data and settings (none selects current dir)
folder = "" if len(sys.argv) == 1 else sys.argv[1]

### Import data and settings from files
print("Loading data... ", end='')
with open(join(folder, "data.json"), 'r') as file:
    data = json.load(file)
print("Done")

print("Loading settings... ", end='')
with open(join(folder, "settings.json"), 'r') as file:
    settings = json.load(file)
print("Done")

### Plot results
fig, ax = plt.subplots(constrained_layout=True)

# Set custom rainbow cycler
rainbowCycle = mpl.cycler(color=['C12F1D', 'D94E1F', 'F16C20', 'EF8B2C', 'ECAA38', 'ECAA38', 'EBC844', '89B37D', '1395BA', '117899', '0F5B78', '0D3C55'])
ax.set_prop_cycle(rainbowCycle)

# Plot data from file
print("Plotting data... ", end='')
x = settings["x_data"]
initOrder = list(data.keys())
for k in initOrder:
    ax.plot(x, data[k], lw=2, clip_on=False)
    ax.scatter(x, data[k], clip_on=False)

# When using ranks, 1 is best (need to invert axis)
ax.invert_yaxis()
print("Done")

### Plot settings
print("Applying settings... ", end='')
plt.tick_params(
    axis="both",
    bottom=False,
    left=False,
    labelbottom=settings["show_x_labels"],
    labelleft=settings["show_y_labels"])

if settings["x_title"]: # X Axis title
    plt.xlabel(settings["x_title"])
if settings["show_x_labels"]: # X tick labels
    plt.xticks(x)
if settings["y_title"]: # Y axis title
    plt.ylabel(settings["y_title"])
if settings["show_y_labels"]: # Y labels
    plt.yticks(list(range(1, len(data.keys())+1)), initOrder)
if settings["title"]: # Graph title
    plt.title(settings["title"], fontsize=13)

# Remove edge splines and margins
# mplstyle setting ported into code (I use custom .mplsytle files to make this easier usually)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.margins(x=0, y=0)

# Set bg Color
bg = "#ecf0f1"
fig.patch.set_facecolor(bg)
ax.set_facecolor(bg)
print("Done")

# Final layout settings
fig.set_size_inches(settings["width"], settings["height"])

### Save Image
print("Saving image... ", end="")
fig.savefig(join(folder, 'RankVisual.png'), dpi=settings["dpi"], facecolor=bg, edgecolor=bg)
print("Done")
plt.show()
