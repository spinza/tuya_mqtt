# Introduction

This links Tuya devices to MQTT using the following:

* Devices are accessed using [tinytuya](https://pypi.org/project/tinytuya/) package.
* Device details are published using the [Homie convention](https://homieiot.github.io/) on MQTT

# Installation

1. Clone this project.
2. `cd tuya_mqtt`
3. Setup the python3 environment using by running `python3 -m venv .venv`
4. Activate the environment by running `source .venv/bin/activate`.
5. Install requirements with `pip install -r requirements.txt`.  This would also install `tinytuya` needed for the following steps.
6. Follow the instructions for `tinytuya` [here](https://pypi.org/project/tinytuya/).
  * Setup the Tuya app.
  * Setup a Tuya account.
  * Run the wizard tool.
  * Note the properites here is discovered via the cloud, so run the wizard tool at least 24h after your device was connected to the Tuya cloud.
  * Also try and activate the full DP settings [per these instructions](https://github.com/jasonacox/tinytuya/blob/master/DP_Mapping.md). 
7. You can then edit the `devices.json` to only include the devices you are interested in.
8.  Copy `config_sample.py` to `config.py` and edit appropriately.
9. You can then run the server by running `./server.py`.
10. The service can also be activated copying the service file `tuya_mqtt.service` to an appropriate location and editing the file to match your setup.

Some things to note:

* Please make sure to set the instruction set to the full set per [these instructions](https://github.com/jasonacox/tinytuya/blob/master/DP_Mapping.md).
* Note that you may need to rerun the wizard tool using `python -m tinytuya wizard` a day our two after first adding your device to ensure the full device details are populated.
