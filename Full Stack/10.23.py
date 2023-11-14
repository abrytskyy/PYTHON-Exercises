
#Declare the following classes in the program:
# CPU - a class to describe processors;
# Memory - a class to describe memory;
# MotherBoard - a class to describe motherboards.

# Ensure the ability to create objects of each class using the following commands:
# cpu = CPU(name, clock speed)
# mem = Memory(name, memory size)
# mb = MotherBoard(name, CPU, memory1, memory2, ..., memoryN)
# Note that when creating an object of the MotherBoard class, you can pass multiple objects of the Memory class,
# up to a maximum of N slots (N = 4, representing the number of memory slots on the motherboard).
# The objects of the classes should have the following instance properties:
# for the CPU class: name - name; fr - clock speed;
# for the Memory class: name - name; volume - memory size;
# for the MotherBoard class: name - name; cpu - a reference to an object of the CPU class; total_mem_slots = 4 - the
# total number of memory slots (this attribute is initialized with this value and remains constant); mem_slots - a list
# of objects of the Memory class (up to a maximum of total_mem_slots = 4 slots).
# The MotherBoard class should have a get_config(self) method to return the current configuration of components on the
# motherboard as a list of four strings:
# ['Motherboard: <name>',
# 'Central Processor: <name>, <clock speed>',
# 'Memory Slots: <total number of memory slots>',
# 'Memory: <name_1> - <volume_1>; <name_2> - <volume_2>; ...; <name_N> - <volume_N>']
# Create an object mb of the MotherBoard class with one CPU (an object of the CPU class) and two memory slots
# (objects of the Memory class).

class CPU:
    def __init__(self, name, clock_speed):

class Mamory:
class MotherBoard:
