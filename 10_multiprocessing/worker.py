import multiprocessing as mp
from steps_aver_func import steps_aver, unite_steps_aver
def worker(ins, outs):
    outs.put(steps_aver(ins.get()))
