import psutil


def cpuFreq():
    return str(psutil.cpu_freq()[0])

# chek it => moeen


def cpuAvailable():
    return str(100-psutil.cpu_percent())+" %"


def memAvailable():
    value = psutil.virtual_memory()[1]
    if(value < 1024):
        return str(value)
    elif(value < 1024**2):
        return str(value//1024)+" KB"
    elif(value < 1024**3):
        return str(value//(1024**2))+" MB"
    else:
        return str(value//(1024**3))+" GB"


def memAvailablePercentage():
    return str(psutil.virtual_memory().available *
               100 // psutil.virtual_memory().total)+" %"


def haveCpu(count):
    if(100 - psutil.cpu_percent() > count):
        return True
    else:
        return False


def haveMem(count):
    cnt = 0
    if "kb" in count.lower():
        cnt = int(count.split()[0])*1024
    elif "mb" in count.lower():
        cnt = int(count.split()[0])*(1024**2)
    elif "gb" in count.lower():
        cnt = int(count.split()[0])*(1024**3)

    if((psutil.virtual_memory()[0] - psutil.virtual_memory()[1]) > cnt):
        return True
    else:
        return False
