## Logging internet speed

This is a simple script with instructions that allows you to monitor the actual speed of your internet connection
over a longer period of time. I use it to compare real world speed of different ISPs.

## Setup
Clone this repository on a linux server of your choosing:

``` bash
git clone https://github.com/robertcv/log_internet_speed
```

Setup a new python virtual environment and install dependencies:

``` bash
python3 -m venv speed_test_venv
source speed_test_venv/bin/activate
pip install wheel
pip install -r requirements.txt
```

Setup a cron job to rerun the script repeatable every 10 minutes. Be aware that cron jobs are run with
root user so change `~/` to the absolut path of files location (don't forget to also change it in the script).

Run the command:

``` bash
crontab -e
```

And append the line:

``` bash
*/10 * * * * ~/log_internet_speed/speed_test_venv/bin/python ~/log_internet_speed/log_internet_speed.py
```

Observe results in the `log_internet_speed.csv` file:

``` bash
$ cat ~/log_internet_speed/log_internet_speed.csv
Server ID,Sponsor,Server Name,Timestamp,Distance,Ping,Download,Upload,Share,IP Address
41545,Goingnet GmbH,Going am Wilden Kaiser,2021-11-27T21:40:02.280443Z,263.3430080744952,66.617,43331972.74262524,39585193.34496518,,***.***.***.***
```
