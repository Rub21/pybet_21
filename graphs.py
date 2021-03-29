import matplotlib.pyplot as plt
import numpy as np


def create_line_graph(eventId, markets_dict):
    plt.figure()
    flag = False
    for key, values in markets_dict.items():
        label = values["label"]
        data = values["data"]
        if len(data) > 60:
            flag = True
            odds = list(map(lambda x: x["odds"], data))
            minutes = list(map(lambda x: x["minutes"], data))

            plt.plot(minutes, odds, label=label)
            plt.xlabel("minutes")
            plt.ylabel("ods")
    if flag:
        plt.legend()
        plt.savefig(f"images/{eventId}.png")
