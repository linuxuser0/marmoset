from capuchin import *
import random

image_sources = ["sets", "sets_a", "sets_b", "sets_c"]

def get_imprinter(imagefeed): 
    return imprinters.Imprinter(imagefeed, "initial", "sorted", num_prototypes=10) 

def print_and_log(text):
    print text
    with open("final_output.log", "a") as f:
        f.write(str(text) + "\n")

def test_genetic(generations, imagefeed_getter, preset):
    population = get_initial_population(preset)    
    best = (None, -1)
    for _ in range(generations):
        print_and_log("Getting fitnesses for generation {0}".format(_))
        fitnesses = [get_fitness(p[:], imagefeed_getter) for p in population]
        if max(fitnesses) > best[1]:
            best_fitness = max(fitnesses)
            best_species = dict(zip(fitnesses, population))[best_fitness]
            best = (best_species, best_fitness)

        population = screen(population, fitnesses) 
        if best[0] is not None: 
            population.append(best[0])
        population = reproduce(population)
        print_and_log("Population: {0} at generation {1}".format(population, _))
        print_and_log("with fitnesses {0}".format(fitnesses))

    print_and_log("{0} => {1}".format(best[0], best[1]))

def get_fitness(string, imagefeed_getter):
    imprinter = get_imprinter(imagefeed_getter())
    monkey = monkeys.GeneticMonkey(imprinter, string)
    values = []
    runs = 0
    for _ in range(10):
        while runs < 10:
            #print "Run {0} begins!".format(runs)
            try:
                runs += monkey.run(remaining=(10-runs))
                values.append(monkey.get_results())
            except Exception, e:
                if "sample" in str(e):
                    print_and_log("Imprinter swap.")
                    monkey.imprinter = get_imprinter(imagefeed_getter())
                else:
                    raise

        return sum(values)/float(len(values))

def get_initial_population(preset=True, size=3):
    """Returns a list of strings of instructions."""
    if not preset:
        instructions_per = 10
        population = []
        for p in range(size): 
            instructions = []
            for i in range(instructions_per):
                keywords = ["rf", "rl", "af", "al", "no"]
                key = random.choice(keywords)
                value = random.randint(1, 5) # fine tune for results 
                instructions.append("{0} {1}".format(key, value))
            population.append(instructions)
    else:
        population =[ ['no 1'] * 10, ['al 1'] * 9 + ['rf 2'], ['af 1'] * 8 + ['rl 1'] * 2, 
                get_initial_population(preset=False, size=1)[0] ]
    
    return population





for source in image_sources:
    utils.print_and_log("SOURCE {0}:".format(source))
    test_genetic(10, lambda: imagefeeds.SortedImageFeed(source, "feed"), False)


