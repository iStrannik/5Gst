# SpeedtestService

[![Build Status](https://github.com/SkoltechSummerCamp/SpeedtestService/workflows/Build%20docker%20image/badge.svg)](https://github.com/SkoltechSummerCamp/SpeedtestService/actions)

## How To Build Service

1. Clone main repo

    ```bash
    git clone --recursive --recurse-submodules https://github.com/SkoltechSummerCamp/5Gst.git
    cd 5Gst/service/
    ```

    or

    ```bash
    git clone https://github.com/SkoltechSummerCamp/5Gst.git
    cd 5Gst/service/
    git submodule init
    git submodule update
    ```

    **iPerf binary is placed in the same directory as `iperf_wrapper.py` script.**

    > Don't foget to `git checkout BRANCH` to your branch.

2. Build Iperf

    `./scripts/build-iperf.sh`

3. Setup environment variables

    ```bash
    YOU_IP=;        #specify your ip
    BALANCER_IP=;   #specify balancer ip
    BALANCER_PORT=; #specify balancer port

    export ALLOWED_HOSTS=127.0.0.1,$YOU_IP; # Hosts on which you want to start service
    export BALANCER_ADDRESS=$BALANCER_IP:$BALANCER_PORT;
    export BALANCER_BASE_URL=/Skoltech_OpenRAN_5G/iperf_load_balancer/0.1.0;
    export CONNECTING_TIMEOUT=30;
    export DEBUG=True;
    export DJANGO_SETTINGS_MODULE=service.settings;
    export IPERF_PORT=5005;
    export SECRET_KEY=123;
    export SERVICE_IP_ADDRESS=$YOU_IP;
    export SERVICE_PORT=5004
    ```

4. Install everything from Pipfile

    ```bash
    pipenv install --dev #if not installed, use: `sudo pip install pipenv`
    pipenv shell # to exit: `deactivate`
    ```

5. Run python

    ```bash
    python3 manage.py migrate
    python3 manage.py runserver $SERVICE_IP_ADDRESS:5004
    ```

## Usage

**iPerf binary is placed in the same directory as `iperf_wrapper.py` script.**


To start the server you need to run the command:

1. Build Iperf
2. Setup environment variables

```
ALLOWED_HOSTS=127.0.0.1; # Hosts on which you want to start service
BALANCER_ADDRESS=127.0.0.1:5555;
BALANCER_BASE_URL=/Skoltech_OpenRAN_5G/iperf_load_balancer/0.1.0;
CONNECTING_TIMEOUT=30;
DEBUG=True;
DJANGO_SETTINGS_MODULE=service.settings;
IPERF_PORT=5005;
SECRET_KEY=123;
SERVICE_IP_ADDRESS=127.0.0.1;
SERVICE_PORT=5004
```
3. Install everything from Pipfile
4. Run python

```
python3 manage.py runserver HERE_IS_YOUR_HOSTNAME 
```

The server listens port `5000` and can handle the following GET requests:

* start-iperf
* stop-iperf

> Set environment variables for IPERF_PORT and SERVICE_PORT, to allow multiple service on one server 

### start-iperf GET request

To start the iPerf with parameters, specified in `args`.

```bash
http://localhost:5000/start-iperf?args=-s%20-t%2010
```

If request has no `args`, iPerf will start with `-s -u` parameters.

If iPerf is already running, it will restart with new `args`.

### stop-iperf GET request

Stop the iPerf process.

```bash
http://localhost:5000/stop-iperf
```
