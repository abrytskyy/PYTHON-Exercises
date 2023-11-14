#Declare the following classes in the program:
#
# CPU - a class for describing processors.
# Memory - a class for describing memory.
# MotherBoard - a class for describing motherboards.
#
# Provide the ability to create objects of each class with the following commands:
#
# cpu = CPU(name, clock_speed)
# mem = Memory(name, size)
# mb = MotherBoard(name, cpu, memory1, memory2, ..., memoryN)
#
# Note that when creating an object of the MotherBoard class, you can pass multiple objects of the Memory class,
# up to a maximum of N, which is the number of memory slots on the motherboard (N = 4).
#
# The objects of the classes should have the following instance properties:
#
# For the CPU class: name - the name; fr - clock speed.
# For the Memory class: name - the name; volume - memory size.
# For the MotherBoard class: name - the name; cpu - a reference to an object of the CPU class;
# total_mem_slots = 4 - the total number of memory slots (this attribute is initialized with this value and does
# not change); mem_slots - a list of objects of the Memory class (up to a maximum of total_mem_slots = 4 objects,
# corresponding to the maximum number of memory slots).
#
# The MotherBoard class should have a method get_config(self) to return the current configuration of components on
# the motherboard in the following format as a list of four strings:
#
# ['Motherboard: <name>',
# 'Central Processor: <name>, <clock speed>',
# 'Memory Slots: <total number of memory slots>',
# 'Memory: <name_1> - <size_1>; <name_2> - <size_2>; ...; <name_N> - <size_N>']
#
# Create an object mb of the MotherBoard class with one CPU (an object of the CPU class) and two memory slots (objects
# of the Memory class).

class CPU:
    def __init__(self, name, clock_speed):
        self.name = name
        self.clock_speed = clock_speed
class Memory:
    def __init__(self, name, size):
        self.name = name
        self.size = size
class MotherBoard:
    total_mem_slots = 4
    def __init__(self, name, cpu, *memories ):
        self.name = name
        self.cpu = cpu
        self.mem_slots = list(memories[:MotherBoard.total_mem_slots])

    def get_config(self):
        mem_info = '; '.join([f'{mem.name} - {mem.volume}' for mem in self.mem_slots])
        return [
            f'Motherboard: {self.name}',
            f'Central Processor: {self.cpu.name}, {self.cpu.fr}',
            f'Memory Slots: {MotherBoard.total_mem_slots}',
            f'Memory: {mem_info}'
        ]
# Create CPU, Memory, and MotherBoard objects
cpu = CPU("Intel i7", "3.6 GHz")
mem1 = Memory("Corsair 16GB", "16 GB")
mem2 = Memory("Kingston 8GB", "8 GB")
mb = MotherBoard("ASUS Prime", cpu, mem1, mem2)

# Get the configuration and print it
config = mb.get_config()
for item in config:
    print(item)