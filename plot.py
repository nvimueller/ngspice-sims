from bokeh.plotting import figure, save, output_file
from bokeh.models import CustomJS

# 1. Read ngspice output data
with open("output.txt", "r") as f:
    data = [line.split() for line in f if line.strip()]

time_us = [float(row[0]) * 1e6 for row in data]
v_in    = [float(row[1]) for row in data]
v_out   = [float(row[3]) for row in data]

output_file("simulation_results.html", title="ngspice Plot")

# 2. Use sizing_mode="stretch_both" so the plot fills the full screen height and width
p = figure(
    title="ngspice Transient Response",
    x_axis_label="Time (µs)",
    y_axis_label="Voltage (V)",
    sizing_mode="stretch_both",
    tools="pan,wheel_zoom,box_zoom,reset,hover,save"
)

p.line(time_us, v_in, legend_label="V(in)", line_width=2, color="#1f77b4")
p.line(time_us, v_out, legend_label="V(out)", line_width=2, color="#ff7f0e")
p.legend.click_policy = "hide"

save(p)

# 3. Inject CSS into the saved HTML to lock touch scrolling and enable full screen
touch_fix_css = """
<style>
  html, body {
    width: 100%;
    height: 100%;
    margin: 0;
    padding: 0;
    overflow: hidden;         /* Prevents browser page scrolling */
    touch-action: none;      /* Redirects all touch drag gestures directly to the Bokeh canvas */
  }
</style>
"""

with open("simulation_results.html", "r") as f:
    html_content = f.read()

# Insert the touch fix right before the </head> tag
html_content = html_content.replace("</head>", f"{touch_fix_css}\n</head>")

with open("simulation_results.html", "w") as f:
    f.write(html_content)

print("Plot updated with touch lock and fullscreen layout!")

