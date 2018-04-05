import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


class Plotter(object):
    def __init__(self):
        super(Plotter).__init__()
        self.csv_name = "GDP_sample.csv"
        self.cn_map = {
            "China" :   1,
            "U.S."  :   2,
            "Japan" :   3,
            "India" :   4,
            "Russia":   5,
            "U.K."  :   6
        }
        self._marker_prio = [">", "o", "s", "*"]
        self.russia_offset = 29
        self.event_list = []

    def set_csv(self, csv_name:str):
        self.csv_name = csv_name

    def set_regions(self, region_list:list):
        self.cn_map = dict()
        for i, region in enumerate(region_list):
            self.cn_map[region] = i + 1

    def set_russia_offset(self, russia_offset):
        self.russia_offset = russia_offset

    def add_event(self, year:int, region:str, description:str):
        self.event_list.append((year, region, str(year) + ": " + description))

    def clear_events(self):
        self.event_list = list()

    def add_events(self, events:list):
        self.clear_events()
        events.sort(key=lambda tup: tup[0])
        for year, region, desc in events:
            self.add_event(year, region, desc)

    def plot(self, fig_name="sample.png", xlabel="x", ylabel="y", log_sc=False):
        data_pool = np.loadtxt(self.csv_name, delimiter=',')
        fig, ax = plt.subplots()
        years = data_pool[:, 0]
        years = years.flatten()
        begin_year = years[0]
        gdp_lines = []
        event_dots = []
        color_map = dict()
        for nation, offset in self.cn_map.items():
            nation_data = data_pool[:, offset]
            nation_data = nation_data.flatten()
            if nation == "Russia":
                years_clip = years[29:]
                nation_data = nation_data[29:]
            else:
                years_clip = years
            gdp_line, = ax.plot(years_clip, nation_data, label=nation)
            color_map[nation] = gdp_line.get_color()
            gdp_lines.append(gdp_line)
        region_counter = dict()
        for year, region, label in self.event_list:
            if region not in region_counter:
                region_counter[region] = 0
            event_dot = ax.scatter(
                year,
                data_pool[int(year - begin_year), self.cn_map[region]],
                label=label,
                color=color_map[region],
                marker=self._marker_prio[region_counter[region]]
            )
            region_counter[region] += 1
            event_dots.append(event_dot)
        if log_sc:
            ax.set_yscale("log", nonposy='clip')
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        first_legend = plt.legend(
            handles=gdp_lines,
            bbox_to_anchor=(0., 1.02, 1., .102),
            loc=3,
            ncol=6,
            mode="expand",
            borderaxespad=0.
        )
        ax.add_artist(first_legend)
        if self.event_list:
            ax.legend(
                handles=event_dots,
                loc="lower right",
                bbox_to_anchor=(0., 0.01, 0.99, .102),
                ncol=1,
                borderaxespad=0.
            )
        fig.savefig(fig_name)
