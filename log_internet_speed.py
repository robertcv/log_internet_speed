import os

import speedtest

LOG_FILE = "~/log_internet_speed/log_internet_speed.csv"

s = speedtest.Speedtest()
s.get_best_server()
s.download()
s.upload()

if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w") as f:
        f.write(s.results.csv_header() + "\n")

with open(LOG_FILE, "a") as f:
    f.write(s.results.csv() + "\n")
