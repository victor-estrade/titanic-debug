# titanic-debug
Debug script to detect dead nodes on titanic cluster


# Usage

First stage is running the jobs on each nodes of the cluster with :
```
python main.py run
```

Second stage is evaluating what run finished correctly using :
```
python main.py eval
```

# Logs

Run logs are saved in `log/DEAD-{node_id}` directory where `{node_id}` are simply the first and last letter of a node name.

TODO : add a command to clean old logs.

# Docker image and other configuration

The docker image and other configuration are hard coded in the fill_template() function in dispatch.py

TODO : make a separated config file (json ?) and functions to read it correctly
TODO : turn all these configuration elements into command line options (in cli.py)


# What it does

Creates one job for every nodes (listed in dispatch.py).
This jobs are running `run.torch_net` script (dispatch.py:75).

TODO : make other tests scripts (for tensorflow and others ?)
TODO : what if one is running a pytorch code with a tensorflow docker image ? (Can it be automatically detected for better error msg ?)

This job runs a simple forward/backward of random data into a small network using pytorch.
At the ends it prints out some dummy end message (captures into the logs).


The *evaluation mode* simply reads the latest log files for all nodes and check that the end message is correct.

TODO : better way of evaluating that the job ended correctly ?
TODO : Print indications explaining why the latest run failed (like error msg or slurm status)
TODO : Print the date and hours (to quickly know if it is a old run)
