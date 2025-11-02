# teste de uma possivel interacao com o usuario
import os, sys
from scr.config_reader import read_config, create_config
from scr.simulator import Simulator


class SystemInterface:
    def __init__(self):
        self.default_file = "config/priop.txt"

    def main_menu():
        print("--- SimuladorOS ---\n")
        