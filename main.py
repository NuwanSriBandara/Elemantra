from distutils.command.config import config
import click
import os

from executor import executor
from utility import set_logger, parse_config

@click.command()
@click.argument("config_file", type=str, default="config.yml")
@click.option('--task', default='seismic', help='Task to be implemented. Options: <seismic> or <bee-modify>.')

def main(task, config_file):

    ####--------------- Configuration ---------------#####
    click.echo(config_file)
    logger = set_logger("./log/main.log") # set logger

    # Load config file
    config = parse_config(config_file)

    # Load configs for data
    data_config = config["main"]["data"]  # load file
    logger.info(f"config:{config['main']}") 


    if task == 'seismic':
        # Load configs for seismic
        data_path = config["main"]["seismic"]["data_path"]
        datapath = os.path.join(data_config, data_path)

        # Execute
        executor(task, datapath) # execute seismic algo

    elif task == 'bee-modify':
        # Load configs for bee-modify
        data_path = config["main"]["bee-modify"]["data_path"]
        datapath = os.path.join(data_config, data_path)

        # Execute
        executor(task, datapath) # execute bee-modify algo


if __name__ == "__main__":
    main()
