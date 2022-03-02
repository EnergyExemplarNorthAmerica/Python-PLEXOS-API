# -*- coding: utf-8 -*-
"""
Created on Mon Jun 05 11:36:46 2017

@author: Steven
"""

from connect_utility import PlexosConnect

def main():
    pc = PlexosConnect()
    print(pc.get_connection_string())
    pass

if __name__ == '__main__':
    main()