#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Victor Calderon
# Created      : 01/25/2018
# Last Modified: 01/25/2018
# Vanderbilt University
from __future__ import print_function, division, absolute_import
__author__     =['Victor Calderon']
__copyright__  =["Copyright 2017 Victor Calderon, "]
__email__      =['victor.calderon@vanderbilt.edu']
__maintainer__ =['Victor Calderon']
"""

"""
# Path to Custom Utilities folder
import os
import sys
import git
from path_variables import *

# Importing Modules
import src.data.utilities_python as cu
import numpy as num
import math
import os
import sys
import pandas as pd
import pickle
import matplotlib
matplotlib.use( 'Agg' )
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
plt.rc('text', usetex=True)
import seaborn as sns
#sns.set()
from progressbar import (Bar, ETA, FileTransferSpeed, Percentage, ProgressBar,
                        ReverseBar, RotatingMarker)

# Extra-modules
from argparse import ArgumentParser
from argparse import HelpFormatter
from operator import attrgetter
from pathlib import Path


## Functions
class SortingHelpFormatter(HelpFormatter):
    def add_arguments(self, actions):
        """
        Modifier for `argparse` help parameters, that sorts them alphabetically
        """
        actions = sorted(actions, key=attrgetter('option_strings'))
        super(SortingHelpFormatter, self).add_arguments(actions)

def _str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def _check_pos_val(val, val_min=0):
    """
    Checks if value is larger than `val_min`

    Parameters
    ----------
    val: int or float
        value to be evaluated by `val_min`

    val_min: float or int, optional (default = 0)
        minimum value that `val` can be

    Returns
    -------
    ival: float
        value if `val` is larger than `val_min`

    Raises
    -------
    ArgumentTypeError: Raised if `val` is NOT larger than `val_min`
    """
    ival = float(val)
    if ival <= val_min:
        msg  = '`{0}` is an invalid input!'.format(ival)
        msg += '`val` must be larger than `{0}`!!'.format(val_min)
        raise argparse.ArgumentTypeError(msg)

    return ival

def get_parser():
    """
    Get parser object for `eco_mocks_create.py` script.

    Returns
    -------
    args: 
        input arguments to the script
    """
    ## Define parser object
    description_msg = 'Description of Script'
    parser = ArgumentParser(description=description_msg,
                            formatter_class=SortingHelpFormatter,)
    ## 
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    ##
    ## Number of weeks
    parser.add_argument('-w', '--weeks',
                        dest='week_n',
                        help='Total number of weeks',
                        type=_check_pos_val,
                        default=14)
    ##
    ##
    parser.add_argument('-coll',
                        dest='col',
                        help='Name of the Collaborator, separated by `_`',
                        nargs='+',
                        default=['John_Hood','Mafe_Senosain','Victor_Calderon'])
    ## Program message
    parser.add_argument('-progmsg',
                        dest='Prog_msg',
                        help='Program message to use throught the script',
                        type=str,
                        default=cu.Program_Msg(__file__))
    ## Parsing Objects
    args = parser.parse_args()

    return args

def param_vals_test(param_dict):
    """
    Checks if values are consistent with each other.

    Parameters
    -----------
    param_dict: python dictionary
        dictionary with `project` variables

    Raises
    -----------
    ValueError: Error
        This function raises a `ValueError` error if one or more of the 
        required criteria are not met
    """
    ##
    ## This is where the tests for `param_dict` input parameters go.

def directory_skeleton(param_dict, proj_dict):
    """
    Creates the directory skeleton for the current project

    Parameters
    ----------
    param_dict: python dictionary
        dictionary with `project` variables

    proj_dict: python dictionary
        dictionary with info of the project that uses the
        `Data Science` Cookiecutter template.

    Returns
    ---------
    proj_dict: python dictionary
        Dictionary with current and new paths to project directories
    """
    ## In here, you define the directories of your project
    ##
    ## Notebooks directory
    notebooks = os.path.join(   proj_dict['base_dir'],
                                'notebooks')
    cu.Path_Folder(notebooks)
    ##
    ## Adding to `param_dict`
    proj_dict['notebooks'] = notebooks

    return proj_dict

def week_dirs(param_dict, proj_dict):
    """
    Creates the list of directories with the Usernames as directories as well

    Parameters
    ----------
    param_dict: python dictionary
        dictionary with `project` variables
    """
    ## Looping over number of weeks
    for kk in range(1,param_dict['week_n']+1):
        ## Looping over collaborator
        for collab_k in param_dict['col']:
            ## Creating directories
            # Week string
            if kk < 10:
                week_str = '0{0}'.format(kk)
            else:
                week_str = '{}'.format(kk)
            ##
            ## Directories
            week_dir = os.path.join(proj_dict['notebooks'],
                                    'Week_{0}'.format(week_str),
                                    collab_k.lower())
            gitkeep_file = os.path.join(week_dir,
                                        '.gitkeep')
            cu.Path_Folder(week_dir)
            Path(gitkeep_file).touch()
            ##
    ##
    ## Creation of folders complete
    print('{0} All directories creates ... Complete!'.format(
        param_dict['Prog_msg']))


def main(args):
    """

    """
    ## Reading all elements and converting to python dictionary
    param_dict = vars(args)
    ## Checking for correct input
    param_vals_test(param_dict)
    ## Program message
    Prog_msg = param_dict['Prog_msg']
    ##
    ## Creating Folder Structure
    # proj_dict  = directory_skeleton(param_dict, cu.cookiecutter_paths(__file__))
    proj_dict  = directory_skeleton(param_dict, cu.cookiecutter_paths('./'))
    ##
    ## Printing out project variables
    print('\n'+50*'='+'\n')
    for key, key_val in sorted(param_dict.items()):
        if key !='Prog_msg':
            print('{0} `{1}`: {2}'.format(Prog_msg, key, key_val))
    print('\n'+50*'='+'\n')
    ##
    ## Creating directories
    week_dirs(param_dict, proj_dict)


# Main function
if __name__=='__main__':
    ## Input arguments
    args = get_parser()
    # Main Function
    main(args)
