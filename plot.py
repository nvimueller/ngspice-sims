import subprocess
import os
from bokeh.plotting import figure, output_file, save

CIR_FILE = "inverter.cir"
RAW_FILE = "inverter.raw"
HTML_FILE = "inverter.html"

print("Running ngspice...")
# Run sim, then write ascii file, then exit. All in 1 command
cmd = f"ngspice -b {CIR_FILE} -c 'run; set wr_vecnames; write {RAW_FILE} v(in) v(out) v(vdd) time; exit'"
result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

if not os.path.exists(RAW_FILE):
    print("ngspice output:")
    print(result.stdout)
    print(result.stderr)
    exit(1)

with open(RAW_FILE, encoding="latin-1") as f:
    lines = f.readlines()

labels = []
data = {}
reading_data = False

for line in lines:
    line = line.strip()
    if not line: continue
    if line.startswith("Values:"):
        reading_data = True
        continue
    if not reading_data:
        parts = line.split()
        if len(parts) == 2 and parts[0].isdigit():
            labels.append(parts[1])
            data[parts[1]] = []
    else:
        parts = line.split()
        if len(parts) == len(labels):
            for i, name in enumerate(labels):
                data[name].append(float(parts[i]))

print(f"Loaded {len(data['time'])} points")

output_file(HTML_FILE)
p = figure(title="CMOS Inverter", x_axis_label="Time (s)",
           y_axis_label="Voltage (V)", width=900, height=400,
           background_fill_color="#1e1e1e", border_fill_color="#1e1e1e",
           tools="pan,wheel_zoom,box_zoom,reset,hover")

colors = ["#58a6ff", "#f85149", "#3fb950"]
for i, name in enumerate(labels[1:]):
    p.line(data['time'], data[name], legend_label=name, line_width=2, color=colors[i % len(colors)])

p.xaxis.axis_label_text_color = "white"
p.yaxis.axis_label_text_color = "white"
p.xaxis.major_label_text_color = "white"
p.yaxis.major_label_text_color = "white"
p.title.text_color = "white"
p.legend.label_text_color = "white"
p.grid_line_color = "#333"

save(p)
print(f"Done -> termux-open {HTML_FILE}")
