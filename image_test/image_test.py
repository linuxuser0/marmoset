import os
from capuchin import *

images_location = "sets"
feed_location = "feed"
sorted_location = "sorted"
initial_location = "initial"
NP = 10

def test_images(path):
    monkey = get_baseline_monkey(path)
    for _ in range(25):
        monkey.run()
        utils.print_and_log(monkey.get_results())

def get_baseline_monkey(path):
    imagefeed = imagefeeds.ImageFeed(path, feed_location, reuse=True)
    imprinter = imprinters.Imprinter(imagefeed, initial_location, sorted_location, num_prototypes=NP) 
    monkey = monkeys.BasicMonkey(imprinter, NP)
    return monkey

for image_location in sorted(os.listdir(images_location)):
    full_path = os.path.join(images_location, image_location)
    utils.print_and_log(image_location)
    test_images(full_path)
