from psutil import cpu_percent

def usage_percent(trange=3):
    lpercent = []
    for x in range(trange):
        lpercent.append(cpu_percent(1, percpu=True))
    return lpercent
        
