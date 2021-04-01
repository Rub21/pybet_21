import matplotlib.pyplot as plt
import numpy as np


def create_line_graph(eventId, markets_dict):
    plt.figure()
    for key, values in markets_dict.items():
        label = values["label"]
        title = values["title"]
        data = values["data"]

        odds = list(map(lambda x: x["odds"], data))
        minutes = list(map(lambda x: x["minutes"], data))

        plt.plot(minutes, odds, label=label)
        plt.title(title)

        plt.xlabel("minutes")
        plt.ylabel("ods")

        plt.legend()
        plt.savefig(f"images/{eventId}.png")
    return f"images/{eventId}.png"
