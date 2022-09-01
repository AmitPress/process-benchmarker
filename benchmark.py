import os
import click
import subprocess
from timeit import default_timer as timer
from tqdm import tqdm
# helpers
def avg_time(batch, process, verbose):
    process_time_elapsed = 0
    for _ in tqdm(range(batch)):
        start = timer()
        if verbose :
            subprocess.call(process)
        else:
            subprocess.call(process, stdout=open(os.devnull, 'wb'))
        process_time_elapsed += timer() - start
    return process_time_elapsed/batch
# main
@click.command()
@click.option('--batch', default=2, help="Number of Batches")
@click.option('--process1', help="The first process")
@click.option('--process2', help="The second process")
@click.option('--verbose', default=False, help="Show output")
def compute(batch, process1, process2, verbose):
    process1 = process1.split()
    process2 = process2.split()
    process1_runtime = avg_time(batch, process1, verbose)
    process2_runtime = avg_time(batch, process2, verbose)
    if process1_runtime < process2_runtime:
        percent = ((process2_runtime - process1_runtime)/process2_runtime)*100
        click.echo(f"Process 1 is the winner\nAnd {percent}% faster than Process2")
    else:
        percent = ((process1_runtime - process2_runtime)/process1_runtime)*100
        click.echo(f"Process 2 is the winner\nAnd {percent}% faster than Process1")

# checking main execution
if __name__ == '__main__':
    compute()