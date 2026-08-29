from bokeh.plotting import figure, save, output_file

with open("vxt.txt", "r") as file:
    next(file)
    data = [line.split() for line in file if line.strip()]

time = [float(row[0]) * 1e9 for row in data]
vin = [float(row[1]) for row in data]
vout = [float(row[2]) for row in data]

output_file("vxt.html", title="ngspice")

plot = figure(
        title="ngspice",
        x_axis_label="time (ns)",
        y_axis_label="voltage (V)",
        sizing_mode="stretch_both",
        tools="pan,wheel_zoom,box_zoom,reset,hover,save",
        output_backend="webgl",
        lod_threshold=1000
        )

colors = ["#0072B2", "#56B4E9", "#E69F00", "#D55E00"]

plot.line(time, vin, legend_label="v(in)", line_width=2, color=colors[0])
plot.line(time, vout, legend_label="v(out)", line_width=2, color=colors[2])

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

with open("vxt.html", "r") as file:
    html_content = file.read()

html_content = html_content.replace("</head>", f"{touch_fix_css}\n</head>")

with open("vxt.html", "w") as file:
    file.write(html_content)
