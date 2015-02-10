# *-* coding: utf-8 *-*
from flask import Blueprint, jsonify
from psutil import Process, get_pid_list

process = Blueprint('process', __name__, 
                    template_folder='')

@process.route('/process', methods=['GET'])
def processs():
    lprocess = get_pid_list()
    lAllprocess=[]
    dprocess={}
    for pid in lprocess:
        pName=Process(pid).name()
        pMemoryPercent=Process(pid).memory_percent()
        pMemoryInfo=Process(pid).memory_info()
        pCpuAfinity=Process(pid).cpu_affinity()
        pGids=Process(pid).gids()
        pUids=Process(pid).uids()
        pUsername=Process(pid).username()
        try:
            pCwd=Process(pid).cwd()
        except:
            pCwd=''
        dprocess={'pid': pid,
                'name': pName,
                'Memory%': pMemoryPercent,
                'Cpu Afinity': pCpuAfinity,
                'CWD': pCwd,
                'Memory info': pMemoryInfo,
                'Gids': pGids,
                'Uids': pUids,
                'Username': pUsername}
        lAllprocess.append(dprocess)
    return jsonify(process=lAllprocess)


@process.route('/process/children/<int:pid>', methods=['GET'])
def get_children(pid):
    lchildren=[]
    if pid != 0:
        pchild=Process(pid)
        for child in pchild.children(recursive=True):
            lchildren.append({'name': child.name(), 
                'pid': child.pid,
                'Memory%': child.memory_percent(),
                'Cpu Afinity': child.cpu_affinity(),
                'Gids': child.gids(),
                'Uids': child.uids(),
                'Username': child.username(),
                'Uids': child.uids()})
    return jsonify(children=lchildren)
