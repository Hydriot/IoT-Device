# IoT-Device
The Hydriot automation software that reads sensors and automate hydroponic processes

## Setup
This application must be run on a Linux based system

### Using Windows Subsystem for Linux (WSL)
1. Enable WSL: Open PowerShell in admin mode and run ```wsl --install``` and ```wsl --set-default-version 2```
2. Download Ubuntu distro: ```wsl --install -d Ubuntu```
3. Start Ubuntu App from start and update ```sudo apt-get update``` and ```sudo apt update && sudo apt upgrade -y```
4. Install Python 3.10 
```sudo apt install software-properties-common -y```
```sudo add-apt-repository ppa:deadsnakes/ppa```
```sudo apt install python3.10```
```sudo apt install python3-pip```
```python3 -m venv python_local```
```sudo chmod -R 755 python_local/```
```source python_local/bin/activate```
```pip install -r requirements.txt```

### Checking out solution
1. Install Git ```sudo apt-get install git```
2. Checkout this repository ```git clone https://github.com/Hydriot/IoT-Device.git hydriot```
3. Open folder in VS Code ```cd hydriot``` then ```code .```

### Checking out solution

