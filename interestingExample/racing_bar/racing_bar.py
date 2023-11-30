import bar_chart_race as bcr
import pandas

bcr.load_dataset()
# 读取数据
df = pandas.read_csv(
    "./data/WHO-COVID-19-cleaned-data.csv", index_col="Date_reported"
).iloc[:, 1:]
# 设置参数
bcr.bar_chart_race(
    df=df,
    filename="./video/covid19_horiz_10.mp4",
    orientation="h",
    sort="desc",
    n_bars=15,
    fixed_order=False,
    fixed_max=True,
    steps_per_period=20,
    interpolate_period=False,
    label_bars=True,
    bar_size=1,
    period_label={"x": 0.99, "y": 0.25, "ha": "right", "va": "center"},
    # period_fmt='%B %d, %Y',
    period_summary_func=lambda v, r: {
        "x": 0.99,
        "y": 0.18,
        "s": f"死亡总数: {v.nlargest(6).sum():,.0f}",
        "ha": "right",
        "size": 8,
    },
    perpendicular_bar_func="median",
    period_length=500,
    figsize=(5, 3),
    dpi=144,
    # cmap='dark12_r',
    title="各国新冠累计死亡人数",
    title_size="",
    bar_label_size=7,
    tick_label_size=7,
    shared_fontdict={"family": "SimHei", "color": ".1"},
    # shared_fontdict={'color' : '.1'},
    scale="linear",
    writer=None,
    fig=None,
    bar_kwargs={"alpha": 0.7},
    filter_column_colors=True,
)
