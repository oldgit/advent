import math
import sys
from collections import deque

from util import expected_for_day

DAY = sys.argv[0].split("/")[-1].split(".")[0]

# FLIP_FLOP dict[name, (ON/OFF, destinations)]
FLIP_FLOPS: dict[str, tuple[bool, list[str]]] = {}
# CONJUNCT dict[name, (inputs_saved_pulse, destinations)]
CONJUNCTS: dict[str, tuple[dict[str, bool], list[str]]] = {}
QUEUE = deque()
LOW = 0
HIGH = 0
PT2_CONS: list[str] = []
PT2_COUNTS: list[int] = []

with open(f"data/{DAY}/input.txt") as file:
    for line in file.read().splitlines():
        (module, destinations) = line.split(" -> ")
        first_char = module[0:1]
        match first_char:
            case "b":
                BROADCASTER: list[str] = destinations.split(", ")
            case "%":
                FLIP_FLOPS[module[1:]] = (False, destinations.split(", "))
            case "&":
                CONJUNCTS[module[1:]] = ({}, destinations.split(", "))


def reset():
    global LOW, HIGH
    LOW = 0
    HIGH = 0
    for f in FLIP_FLOPS:
        _, ds = FLIP_FLOPS[f]
        FLIP_FLOPS[f] = (False, ds)
    for c in CONJUNCTS:
        ins, ds = CONJUNCTS[c]
        for in_name in ins:
            ins[in_name] = False


def derive_p2_cons_from_rx():
    for c in CONJUNCTS:
        ins, ds = CONJUNCTS[c]
        for d in ds:
            if d == "rx":
                for in_name in ins:
                    PT2_CONS.append(in_name)


def find_cons_inputs():
    for con in CONJUNCTS:
        for f in FLIP_FLOPS:
            for fd in FLIP_FLOPS[f][1]:
                if fd == con:
                    CONJUNCTS[con][0][f] = False
        for c in CONJUNCTS:
            for cd in CONJUNCTS[c][1]:
                if cd == con:
                    CONJUNCTS[con][0][c] = False


def add_to_queue(in_name, pulse, targets):
    global LOW, HIGH
    for t in targets:
        QUEUE.append((in_name, pulse, t))
        if pulse:
            HIGH += 1
        else:
            LOW += 1


def flip_flop_receive(pulse, name):
    if not pulse:
        on, ds = FLIP_FLOPS[name]
        result = not on
        FLIP_FLOPS[name] = (result, ds)
        add_to_queue(name, result, ds)


def cons_receive(in_name, pulse, name):
    inputs, ds = CONJUNCTS[name]
    inputs[in_name] = pulse
    value_set = set(inputs.values())
    result = not (len(value_set) == 1 and list(value_set)[0] is True)
    add_to_queue(name, result, ds)


def process_queue(index):
    while QUEUE:
        in_name, pulse, destination_name = QUEUE.popleft()
        # Store button count when a high pulse is sent to pt2 end module
        if in_name in PT2_CONS and pulse:
            PT2_COUNTS.append(index + 1)
        if FLIP_FLOPS.get(destination_name) is not None:
            flip_flop_receive(pulse, destination_name)
        if CONJUNCTS.get(destination_name) is not None:
            cons_receive(in_name, pulse, destination_name)


def push_button(index):
    global LOW
    LOW += 1
    for destination_name in BROADCASTER:
        QUEUE.append(("b", False, destination_name))
        LOW += 1
    process_queue(index)


def part_1():
    for i in range(1000):
        push_button(i)
    return HIGH * LOW


def part_2():
    reset()
    derive_p2_cons_from_rx()
    for i in range(5000):
        push_button(i)
    return math.lcm(*PT2_COUNTS)


find_cons_inputs()

p1_result = part_1()
p2_result = part_2()

p1_expected, p2_expected = expected_for_day(DAY)
assert p1_result == p1_expected
assert p2_result == p2_expected
print(f"{DAY} Part 1: {p1_result}")
print(f"{DAY} Part 2: {p2_result}")
