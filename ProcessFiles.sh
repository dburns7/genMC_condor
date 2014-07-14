#!/bin/sh
#$1 = target directory
#$2 = event name

rm out*

mv final* $1

#pushd $1
#if [ -e "all_$2.root" ]
#then
#  rm all_$2.root
#fi
#hadd all_$2.root *.root
#cp all_$2.root ..
#popd

