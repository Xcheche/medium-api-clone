#!/usr/bin/env bash

# A simple countdown timer that can be used in scripts.
countdown(){

    # A simple countdown.
    declare desc="A simple countdown."
    local seconds="${1}"

    local d=$(($(date  +%s) + "${seconds}"))

    while [ "$(date +%s)" -lt "${d}" ]; do
        echo -ne " \r$(($(date +%s) - (${d} - ${seconds})))/${seconds} "
        sleep 1
    done

}

