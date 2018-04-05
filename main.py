from Plotr import Plotter

sample_plotter = Plotter()
sample_plotter.set_csv("GDP_sample.csv")
sample_plotter.set_regions(
    ["China", "U.S.", "Japan", "India", "Russia", "U.K."]
)
sample_plotter.set_russia_offset(29)
event_list = [
    (1978, "China", "Chinese Economic Reform"),
    (1985, "Japan", "Plaza Accord"),
    (1989, "Russia", "Limited Democratization of SU")
]
sample_plotter.add_events(event_list)
sample_plotter.plot(xlabel="GDP / USD", ylabel="year", log_sc=True)