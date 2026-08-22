from bokeh.plotting import figure, save, output_file
from bokeh.models import CustomJS

with open("32nm_lp.txt", "r") as file:
    data_32nm_lp = [line.split() for line in file if line.strip()]
with open("45nm_lp.txt", "r") as file:
    data_45nm_lp = [line.split() for line in file if line.strip()]
with open("32nm_hp.txt", "r") as file:
    data_32nm_hp = [line.split() for line in file if line.strip()]
with open("45nm_hp.txt", "r") as file:
    data_45nm_hp = [line.split() for line in file if line.strip()]


th_32nm_lp = [float(row[1]) for row in data_32nm_lp]
td_32nm_lp = [float(row[0]) for row in data_32nm_lp]
th_45nm_lp = [float(row[1]) for row in data_45nm_lp]
td_45nm_lp = [float(row[0]) for row in data_45nm_lp]
th_32nm_hp = [float(row[1]) for row in data_32nm_hp]
td_32nm_hp = [float(row[0]) for row in data_32nm_hp]
th_45nm_hp = [float(row[1]) for row in data_45nm_hp]
td_45nm_hp = [float(row[0]) for row in data_45nm_hp]


output_file("plot.html", title="ngspice")

plot = figure(
        title="ngspice",
        x_axis_label="threshold voltage (V)",
        y_axis_label="propagation delay (ns)",
        sizing_mode="stretch_both",
        tools="pan,wheel_zoom,box_zoom,reset,hover,save"
        )

colors = ["#0072B2", "#56B4E9", "#E69F00", "#D55E00"]

plot.line(th_32nm_lp, td_32nm_lp, legend_label="32nm_lp", line_width=2, color=colors[0])
plot.line(th_45nm_lp, td_45nm_lp, legend_label="45nm_lp", line_width=2, color=colors[2])
plot.line(th_32nm_hp, td_32nm_hp, legend_label="32nm_hp", line_width=2, color=colors[1])
plot.line(th_45nm_hp, td_45nm_hp, legend_label="45nm_hp", line_width=2, color=colors[3])

plot.legend.click_policy = "hide"

save(plot)

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

with open("plot.html", "r") as file:
    html_content = file.read()

html_content = html_content.replace("</head>", f"{touch_fix_css}\n</head>")

with open("plot.html", "w") as file:
    file.write(html_content)
