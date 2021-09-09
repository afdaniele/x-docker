# `x-docker` - Command Line Wrapper

**x-docker** (cli) is a wrapper around **docker-cli** that lets you run GUI applications by exposing the X11 server to the container.

## Install x-docker

Clone the repository and run the following command to install **x-docker**:

```
sudo ./install
```

## How to use it

If your application has a GUI, replace **docker** with **x-docker** in your command. For example, you can run
Inkscape simply by running:

```
x-docker run jess/inkscape
```
