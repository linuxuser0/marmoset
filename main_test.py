from capuchin.utils import *
from capuchin.imagefeeds import * 
from capuchin.imprinters import *
from capuchin.monkeys import *

PROTOTYPES = range(2, 31)
WINDOWS = range(4, 61, 4)
NUM_TRIALS = 5 
GENERATIONS = 5 

print_and_log("TEST ONE")
double_test(test_baseline, PROTOTYPES)
print_and_log("TEST TWO")
double_test(test_window, WINDOWS)

print_and_log("TEST THREE")
test_genetic(GENERATIONS, get_imagefeed, False)
print_and_log("--------------------------------------------")
print_and_log("TEST FOUR")
test_genetic(GENERATIONS, get_imagefeed, True)
print_and_log("--------------------------------------------")
print_and_log("TEST FIVE")
test_genetic(GENERATIONS, get_sorted_imagefeed, False)
print_and_log("--------------------------------------------")
print_and_log("FINAL TEST (SIX)")
test_genetic(GENERATIONS, get_sorted_imagefeed, True)

