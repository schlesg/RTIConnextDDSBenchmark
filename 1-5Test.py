import subprocess
import os

msgLen =  '10000'

commandList = []
commandList.append("bin/x64Linux3gcc5.4.0/release/perftest_cpp03 -sub -bestEffort -numPublishers 1 -noPrintIntervals -sidMultiSubTest 0 -dataLen " + msgLen)
commandList.append("bin/x64Linux3gcc5.4.0/release/perftest_cpp03 -sub -bestEffort -numPublishers 1 -noPrintIntervals -sidMultiSubTest 1 -dataLen " + msgLen)
commandList.append("bin/x64Linux3gcc5.4.0/release/perftest_cpp03 -sub -bestEffort -numPublishers 1 -noPrintIntervals -sidMultiSubTest 2 -dataLen " + msgLen)
commandList.append("bin/x64Linux3gcc5.4.0/release/perftest_cpp03 -sub -bestEffort -numPublishers 1 -noPrintIntervals -sidMultiSubTest 3 -dataLen " + msgLen)
commandList.append("bin/x64Linux3gcc5.4.0/release/perftest_cpp03 -sub -bestEffort -numPublishers 1 -noPrintIntervals -sidMultiSubTest 4 -dataLen " + msgLen)

commandList.append("bin/x64Linux3gcc5.4.0/release/perftest_cpp03 -pub -bestEffort -latencyTest -numIter 1000 -noPrintIntervals -numSubscribers 5 -dataLen " + msgLen)


for command in commandList:
    subprocess.Popen(command.split(), cwd="../rtiperftest-2.4")


input("Press Enter to shutdown...\n")
os.system("pkill -f perftest")
