#! /bin/sh -f
# $1 = number of jobs

numberOfJobs=$1
skipEvents=100

for i in `seq 0 $(($numberOfJobs-1))`;
  do
    echo "Processing job $(($i+1))"
    sed -i "s/^JOB.*/JOB=$(($i+1))/" genMCjob.sh
    wait $!
    sed -i "s/^EVTS.*/EVTS=$(($skipEvents*$i))/" genMCjob.sh
    wait $!
    condor_submit condor_config
    wait $!
    sleep 25
  done  
