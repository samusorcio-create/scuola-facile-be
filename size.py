#from repository import * as verifica



# def verifica_compatibilita(id_cpu = None, id_motherboard = None, id_memoria_volatile = None, id_gpu = None, id_alimentatore = None, id_case = None, id_raffreddamento = None):
    
    # if id_cpu == None:

    # cpu = cpu_repository.get_by_id(id_cpu)
    # motherboard = maderboard_repository.get_by_id(id_motherboard)
    # memoria_volatile = memoria_volatile_repository.get_by_id(id_memoria_volatile)
    # gpu = gpu_repository.get_by_id(id_gpu)
    # alimentatore = alimentatore_repository.get_by_id(id_alimentatore)
    # case = case_repository.get_by_id(id_case)
    # raffreddamento = raffreddamento_repository.get_by_id(id_raffreddamento)

    # if cpu.socket != motherboard.socket:
    #     return False

    # if memoria_volatile.tipo != motherboard.slot_espansione_ram:
    #     return False

    # if gpu.formato != motherboard.slot_espansione_gpu:
    #     return False

    # if alimentatore.TDP < (cpu.TDP + gpu.TDP + memoria_volatile.TDP + motherboard.TDP):
    #     return False

    # if case.formato != motherboard.formato:
    #     return False

    # if raffreddamento.tipo != cpu.socket:
    #     return False

    # return True



# 