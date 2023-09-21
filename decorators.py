import time

commands = {"configure", "measure_temp", "measure_humidity", "commando1", "commando2"}

def check_command(f):
    def inner(self, command):
        if command in commands:
            print(f'command: "{command}" recognized')
            f(self, command)
        else:
            print(f'command: "{command}" not recognized')
    return inner

def log_command(f):
    def inner(self, command):
        f(self, command)
        print(f"Command has been send") 
        return
    return inner

def measure_rate(f):
    def inner(self):
        start_time = time.time()
        f(self)
        duration = time.time() - start_time
        print(f'Rate of measurements: {round(1/duration)} Hz')
        return
    return inner