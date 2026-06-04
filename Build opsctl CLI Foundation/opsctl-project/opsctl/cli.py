#!/usr/bin/env python3
"""
Main CLI entry point for opsctl.
Handles argument parsing and command routing.
"""

import argparse
import sys
from opsctl.version import __version__, __description__
from opsctl.commands import status, deploy, config


def create_parser():
    """
    Create and configure the argument parser.
    
    Returns:
        argparse.ArgumentParser: Configured parser with subcommands
    """
    parser = argparse.ArgumentParser(
        prog='opsctl',
        description=__description__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    # TODO: Add global arguments (--version, --verbose)
    
    # TODO: Create subparsers for commands
    
    # TODO: Add 'status' subcommand with appropriate arguments
    
    # TODO: Add 'deploy' subcommand with required parameters
    
    # TODO: Add 'config' subcommand with set/get operations
    
    return parser


def main():
    """
    Main entry point for the CLI application.
    Parses arguments and executes appropriate commands.
    """
    parser = create_parser()
    args = parser.parse_args()
    
    # TODO: Handle version flag
    
    # TODO: Route to appropriate command handler based on subcommand
    
    # TODO: Handle case when no command is provided
    
    pass


if __name__ == '__main__':
    main()
