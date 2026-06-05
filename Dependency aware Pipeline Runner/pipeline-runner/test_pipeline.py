#!/usr/bin/env python3
"""Test script for pipeline runner"""

import os
import sys

def test_successful_pipeline():
    """Test pipeline with all successful jobs"""
    print("\n" + "="*60)
    print("TEST 1: Successful Pipeline")
    print("="*60)
    os.system("python3 pipeline_runner.py pipeline_config.yaml")

def test_failed_pipeline():
    """Test pipeline with job failure"""
    print("\n" + "="*60)
    print("TEST 2: Pipeline with Failure")
    print("="*60)
    os.system("python3 pipeline_runner.py pipeline_config_fail.yaml")

if __name__ == "__main__":
    test_successful_pipeline()
    test_failed_pipeline()
