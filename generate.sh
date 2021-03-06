#!/bin/bash

{
    # command which may fail and give an error 
    scriptDir=$(dirname -- "$(readlink -f -- "$BASH_SOURCE")")
    #DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
    #echo("$(DIR)")

    python3 $scriptDir/pytest.py
} || {
       # command which should be run instead of the above failing command
       echo "Command exited with an error."
       exit 1
}

echo "Test script executed."