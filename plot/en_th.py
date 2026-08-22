from bokeh.plotting import figure, save, output_file

with open("32nm_lp_en_th.txt", "r") as file:
    data_32nm_lp = [line.split() for line in file if line.strip()]
with open("45nm_lp_en_th.txt", "r") as file:
    data_45nm_lp = [line.split() for line in file if line.strip()]
with open("32nm_hp_en_th.txt", "r") as file:
    data_32nm_hp = [line.split() for line in file if line.strip()]
with open("45nm_hp_en_th.txt", "r") as file:
    data_45nm_hp = [line.split() for line in file if line.strip()]

th_32nm_lp = [float(row[0]) for row in data_32nm_lp]
en_32nm_lp = [float(row[1]) for row in data_32nm_lp]
th_45nm_lp = [float(row[0]) for row in data_45nm_lp]
en_45nm_lp = [float(row[1]) for row in data_45nm_lp]
th_32nm_hp = [float(row[0]) for row in data_32nm_hp]
en_32nm_hp = [float(row[1]) for row in data_32nm_hp]
th_45nm_hp = [float(row[0]) for row in data_45nm_hp]
en_45nm_hp = [float(row[1]) for row in data_45nm_hp]

output_file("en_th.html", title="ngspice")

plot = figure(
        title="ngspice",
        x_axis_label="threshold voltage (V)",
        y_axis_label="energy dissipated (fJ)",
        sizing_mode="stretch_both",
        tools="pan,wheel_zoom,box_zoom,reset,hover,save"
        )

colors = ["#0072B2", "#56B4E9", "#E69F00", "#D55E00"]

plot.line(th_32nm_lp, en_32nm_lp, legend_label="32nm_lp", line_width=2, color=colors[0])
plot.line(th_45nm_lp, en_45nm_lp, legend_label="45nm_lp", line_width=2, color=colors[2])
plot.line(th_32nm_hp, en_32nm_hp, legend_label="32nm_hp", line_width=2, color=colors[1])
plot.line(th_45nm_hp, en_45nm_hp, legend_label="45nm_hp", line_width=2, color=colors[3])

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

with open("en_th.html", "r") as file:
    html_content = file.read()

html_content = html_content.replace("</head>", f"{touch_fix_css}\n</head>")

with open("en_th.html", "w") as file:
    file.write(html_content)
