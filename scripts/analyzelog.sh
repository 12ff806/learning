#!/bin/bash
#
# Analyze log
# This shell script is released under the WTFPL license
# Janus Zhao <Janus_Zhao@163.com/ JanusKernel@gmail.com>
# December 30, 2014

# variables
sourcedir="/home/janus/test/test1"
targetdir="/home/janus/test/test2"
logname=`date +%F`

# start

#ls -l $sourcedir | grep "tar.gz" | awk -F ' ' '{print $9}' > ./tarfile
#for log in `cat ./tarfile`
#do
    #cp $sourcedir/$log $targetdir
#done

# whether the log file exist or not?
if [ -f $sourcedir/$logname".tar.gz" ]; then
    echo "the log file exist"
else
    echo "the log file does not exist, exit.."
    exit 1
fi

# copy the log file to target dir and decompress
cp $sourcedir/$logname".tar.gz" $targetdir
cd $targetdir
tar -xz -f $logname".tar.gz" 
