from Plotr import Plotter

sample_plotter = Plotter()
sample_plotter.set_csv("GDP_sample.csv")
sample_plotter.set_regions(
    ["中国", "美国", "日本", "印度", "俄罗斯", "英国"]
)
sample_plotter.set_strange_region("俄罗斯")
sample_plotter.set_russia_offset(29)
event_list = [
    (1978, "中国", "改革开放"),
    (1985, "日本", "广场协议"),
    (1989, "俄罗斯", "有限民主化")
]
sample_plotter.add_events(event_list)
sample_plotter.plot(fig_name="sample.pdf", xlabel="GDP / USD", ylabel="year", log_sc=True)