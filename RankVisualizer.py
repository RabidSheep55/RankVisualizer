import matplotlib.pyplot as plt
import matplotlib as mpl
import json

### Import data from file
with open("data.json", 'r') as file:
    raw = json.load(file)
    settings = raw["settings"]
    data = raw["data"]

### Plot results
fig, ax = plt.subplots(constrained_layout=True)

# Set custom rainbow cycler
rainbowCycle = mpl.cycler(color=['C12F1D', 'D94E1F', 'F16C20', 'EF8B2C', 'ECAA38', 'ECAA38', 'EBC844', '89B37D', '1395BA', '117899', '0F5B78', '0D3C55'])
ax.set_prop_cycle(rainbowCycle)

# Plot data from file
x = settings["x_data"]
initOrder = list(data.keys())
for k in initOrder:
    ax.plot(x, data[k], lw=2, clip_on=False)
    ax.scatter(x, data[k], clip_on=False)

# When using ranks, 1 is best (need to invert axis)
ax.invert_yaxis()

### Plot settings
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

# Final layout settings
fig.set_size_inches(1.6, 1.9)
fig.savefig('RankVisual.png', dpi=400, facecolor=bg, edgecolor=bg)
plt.show()
