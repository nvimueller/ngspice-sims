from bokeh.plotting import figure, save, output_file

def get_data(file_name):
    file = open(file_name, "r")
    data = [line.split() for line in file if line.strip()]
    file.close()
    return data

def set_output_file(file_name, file_title):
    output_file(file_name, title=file_title)

def get_plot(figure_title, x_label, y_label):
    plot = figure(
            title=figure_title,
            x_axis_label=x_label,
            y_axis_label=y_label,
            sizing_mode="stretch_both",
            tools="pan,wheel_zoom,box_zoom,reset,hover,save",
            output_backend="webgl",
            lod_threshold=1000
            )
    return plot

def get_colors():
    colors = ["#0072B2", "#56B4E9", "#E69F00", "#D55E00"]
    return colors

def plot_line(plot, x, y, line_label, tint):
    plot.line(x, y, legend_label=line_label, line_width=2, color=tint)

def save_plot(plot):
    plot.legend.click_policy = "hide"
    save(plot)

def get_css_fix():
    css_fix = """
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
    return css_fix

def fix_html(file_name):
    file = open(file_name, "r")
    html_content = file.read()
    file.close()
    css_fix = get_css_fix()
    html_content = html_content.replace("</head>", f"{css_fix}\n</head>")
    file = open(file_name, "w")
    file.write(html_content)
    file.close()

voltages = get_data("voltage.txt")
data = get_data("data.txt")

time = [float(row[0]) * 1e9 for row in voltages]
vin = [float(row[1]) for row in voltages]
vout = [float(row[2]) for row in voltages]

th = [float(row[0]) for row in data]
delay = [float(row[1]) for row in data]
energy = [float(row[2]) for row in data]

colors = get_colors()

voltage_plot = get_plot("V(IN) VS V(OUT)", "TIME (NS)", "VOLTAGE (V)")
plot_line(voltage_plot, time, vin, "V(IN)", colors[0])
plot_line(voltage_plot, time, vout, "V(OUT)", colors[2])
set_output_file("voltage.html", "VOLTAGE ANALYSIS")
save_plot(voltage_plot)

delay_plot = get_plot("DELAY X THRESHOLD", "THRESHOLD (V)", "DELAY (NS)")
plot_line(delay_plot, th, delay, "DELAY", colors[0]) 
set_output_file("delay.html", "DELAY ANALYSIS")
save_plot(delay_plot)

energy_plot = get_plot("ENERGY X THRESHOLD", "THRESHOLD (V)", "ENERGY (FJ)")
plot_line(energy_plot, th, energy, "ENERGY", colors[0])
set_output_file("energy.html", "ENERGY ANALYSIS")
save_plot(energy_plot)

fix_html("voltage.html")
fix_html("delay.html")
fix_html("energy.html")
