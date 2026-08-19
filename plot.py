import pandas as pd
from bokeh.plotting import figure, show, output_file

# 1. Read exported ngspice file (whitespace-delimited)
# ngspice duplicates the x-axis (time) for each variable requested in wrdata
data = pd.read_csv("output.txt", delim_whitespace=True, header=None)

time_ns = data[0] * 1e6  # Convert seconds to microseconds
v_in = data[1]
v_out = data[3]

# 2. Setup Bokeh figure
output_file("simulation_results.html")
p = figure(
    title="ngspice Transient Simulation",
    x_axis_label="Time (µs)",
    y_axis_label="Voltage (V)",
    width=800,
    height=400,
    tools="pan,wheel_zoom,box_zoom,reset,hover,save"
)

# 3. Add lines
p.line(time_ns, v_in, legend_label="V(in)", line_width=2, color="blue")
p.line(time_ns, v_out, legend_label="V(out)", line_width=2, color="red")

p.legend.click_policy = "hide"

# 4. Display output
show(p)

