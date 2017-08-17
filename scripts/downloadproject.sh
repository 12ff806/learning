#!/bin/bash
#
# To download web projects that in the 'webapp_list' file from github
# webapp_list format: 'username/project_name'
# Janus Zhao <JanusKernel@gmail.com>/<Janus_Zhao@163.com>
# Aug 14, 2014

for project in `cat ./webapp_list`
do
    username=`echo $project | awk -F '/' '{print $1}'`
    proj_name=`echo $project | awk -F '/' '{print $2}'`
    url="https://github.com/"$project"/archive/master.zip"

    # download 
    [ -f ../webapp/$username"-"$proj_name".zip" ] && continue
    echo "downloading "$project
    wget $url -O ../webapp/$username"-"$proj_name".zip" >/dev/null 2>&1
    if [ $? -eq 0 ]
    then
        echo "download "$project" finished"
    else
        echo "download "$project" error"
        continue
    fi
    
    # unzip
    echo "unzip "$project
    unzip ../webapp/$username"-"$proj_name".zip" -d ../webapp/$username"-"$proj_name >/dev/null 2>&1
    if [ $? -eq 0 ]
    then
        echo "unzip "$project" finished"
    else
        echo "unzip "$project" error"
    fi
done

echo "done"
