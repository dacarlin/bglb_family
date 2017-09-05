#!/bin/bash 

# test the deep mutational scanning protocol

TEST_DIR=example_input 
cp protocol.py $TEST_DIR/protocol.py 
cd $TEST_DIR 
source activate rose 
python protocol.py 
