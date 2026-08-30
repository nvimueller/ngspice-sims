#set page(paper: "us-letter", margin: 2cm)
#set text(font: "New Computer Modern", size: 10pt)
#set par(justify: true)

#align(center)[
  #text(16pt)[*Energy Dissipation and Propagation Delay as Functions of Threshold Voltage: a CMOS Study*]
]

= Summary
My research focus has shifted from a low-power 32nm CMOS process to a standard 90nm CMOS. This change was prompted by difficulties in achieving a balanced voltage transfer characteristic, specifically aligning the intersection of $V_"in"$ and $V_"out"$ near 50% of the supply voltage. Despite iterative adjustments to the load capacitance and transistor width, establishing an equilibrium in the MOSFET characteristics proved challenging at 32nm. Transitioning to the 90nm technology node provides a larger channel length, effectively mitigating several UDSM effects during simulation. With this more stable baseline, I simulated the impact of threshold voltage variations on energy dissipation and propagation delay---addressing a gap identified in our primary reference literature. Additionally, I improved the `Python` script that generates `HTML` plots for mobile devices, facilitating multi-platform analysis of the data.

= Progress and Activities
- Changed analysis from 32nm to 90nm transistor to facilitate balance configurations.
- Analysed the propagation delay as a function of a sweeping threshold.
- Analysed the energy dissipated as a function of a sweeping threshold.
- Improved the `Python` script to generate multiple plots from a single file.

#figure(
    image("voltage.png", width: 100%),
    caption: [$V_"in"$ and $V_"out"$ intersection.],
  ) <voltage_plot>


#columns(2, gutter: 16pt)[
  #figure(
    image("delay.png", width: 95%),
    caption: [Propagation delay as a function of threshold voltage.],
  ) <delay_plot>
  
  #colbreak()
  
  #figure(
    image("energy.png", width: 95%),
    caption: [Energy dissipation as a function of threshold voltage.],
  ) <energy_plot>  
  #colbreak()
  
]
