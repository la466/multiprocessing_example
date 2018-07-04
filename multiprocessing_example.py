import functions as funcs
import time


def run_linear(input_list):
    '''
    This example will run linearly
    '''

    print("\nRunning linearly...\n")

    t0 = time.time()

    outputs = the_function_to_parallelise(input_list, 3)
    print(outputs)

    t1 = time.time()
    print("Time taken: {0}".format(t1-t0))


def run_parallel(input_list):
    '''
    This will run in parallel
    '''

    print("\nRunning in parallel...\n")

    t0 = time.time()

    processes = funcs.run_in_parallel(input_list, ["foo", 3], the_function_to_parallelise)
    outputs = []
    # you have to retrieve these from the processes, I don't know if this is what its
    # oficially called but it will do
    for process in processes:
        outputs.extend(process.get())

    print(outputs)

    t1 = time.time()
    print("Time taken: {0}".format(t1-t0))


def the_function_to_parallelise(input_list, number_of_times):
    '''
    Your function that you want to parallelise
    arg1 of this function is the list to iterate over, which will be your library
    arg2, ..., argN are any other arguments you want to use
    '''

    outputs = []

    for i, item in enumerate(input_list):
        print("Running sample {0}/{1}".format(i, len(input_list)))
        output = funcs.do_whatever_you_want(item, number_of_times)
        outputs.append(output)

    return outputs


def main():

    # This is where you would read in your library
    input_file = "library.txt"
    input_list = funcs.read_in_file(input_file)

    # these aren't the actual parallelised functions
    # these just show you they are basically the same thing
    # but split over the processes

    # I normally build the function linearly, because parallelisation
    # doesn't always provide useful errors
    # I then just switch to parallel when im ready

    run_linear(input_list)
    run_parallel(input_list)



if __name__ == "__main__":
    main()
