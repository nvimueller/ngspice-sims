from bokeh.plotting import figure, save, output_file
from bokeh.models import CustomJS

with open("data.txt", "r") as f:
    data = [line.split() for line in f if line.strip()]

time_us = [float(row[0]) * 1e9 for row in data]
v_in    = [float(row[1]) for row in data]
v_out   = [float(row[2]) for row in data]
# i_vdd   = [float(row[3]) for row in data]

output_file("plot.html", title="ngspice")

p = figure(
        title="ngspice",
        x_axis_label="time (ns)",
        y_axis_label="voltage (v)",
        sizing_mode="stretch_both",
        tools="pan,wheel_zoom,box_zoom,reset,hover,save"
        )

p.line(time_us, v_in, legend_label="v(in)", line_width=2, color="#1f77b4")
p.line(time_us, v_out, legend_label="v(out)", line_width=2, color="#ff7f0e")
p.legend.click_policy = "hide"

save(p)

touch_fix_css = """
<style>
  html, body {
    width: 100%;
    height: 100%;
    margin: 0;
    padding: 0;
    overflow: hidden;
    touch-action: none;
  }
</style>
"""

with open("plot.html", "r") as f:
    html_content = f.read()

html_content = html_content.replace("</head>", f"{touch_fix_css}\n</head>")

with open("plot.html", "w") as f:
    f.write(html_content)
