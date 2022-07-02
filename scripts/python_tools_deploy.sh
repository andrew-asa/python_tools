#!/bin/sh
basePath=$(cd `dirname $0`;pwd)
cd $basePath
cd ..
python setup.py install