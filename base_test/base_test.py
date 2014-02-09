from capuchin import *

image_sources = ["sets_a", "sets_b", "sets_c"]

for source in image_sources:
    utils.print_and_log("SOURCE {0}:".format(source))
    for size in range(10, 201, 10):
        utils.print_and_log("SIZE {0}:".format(size))
        for trial in range(10):
            utils.print_and_log("TRIAL {0}:".format(trial))
            imagefeed = imagefeeds.SortedImageFeed(source, "feed")
            imprinter = imprinters.Imprinter(imagefeed, "initial", "sorted", num_prototypes=size)
            monkey = monkeys.BasicMonkey(imprinter, num_prototypes=size)
            points = []
            for run in range(10):
                monkey.run()
                utils.print_and_log(monkey.get_results())
            utils.print_and_log("---------------")


                

                

