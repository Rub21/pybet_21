from db_package import get_Events
from graphs import create_line_graph
import os

if not os.path.exists("images"):
    os.makedirs("images")

data = get_Events(100)

for event_id, markets_dict in data.items():
    print(event_id)
    create_line_graph(event_id, markets_dict)
    # print(data)
