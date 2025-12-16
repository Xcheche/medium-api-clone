# messages.sh - helper functions for printing formatted terminal messages
#!/usr/bin/env bash

# Common notes:
#   - All functions use echo -e to interpret ANSI escape sequences.
#   - Each function accepts arbitrary arguments (passed as ${@}) to form the
#     message body.
#   - ANSI color/formatting codes are used for human-readable terminal output
#     and require a terminal that supports ANSI escape sequences.
#--------------------------------------------------------------------------------------------------

# message_newline()
#   Print a single blank line to stdout.
message_newline(){
    echo
}
 
# message_debug()
#   Print a debug message to stdout. Prefixes the output with "DEBUG: " and
#   interprets escape sequences (uses echo -e). Accepts any number of arguments. 
message_debug(){
    echo -e "DEBUG: ${@}"
}

# message_welcome()
#   Print the provided arguments in bold (ANSI escape sequence \e[1m...\e[0m)
#   to stdout and then emit an extra blank line by calling message_newline().
message_welcome(){
    echo  -e "\e[1m${@}\e[0m"
    message_newline
}


# message_warning()
#   Print a warning message to stdout. Prefixes the output with "WARNING: "
#   and colors the prefix/message in yellow (ANSI \e[33m), then resets color.
message_warning(){
    echo -e "\e[33mWARNING: ${@}\e[0m"
}


# message_error()
#   Print an error message to stderr. Prefixes the output with "ERROR: "
#   and colors the prefix/message in red (ANSI \e[31m). Uses stderr redirection.
message_error(){
    echo -e "\e[31mERROR: ${@}\e[0m" >&2
}


# message_info()
#   Print an informational message to stdout. Prefixes the output with "INFO"
#   styled in white (ANSI \e[37m) followed by the provided arguments.
message_info(){
    echo -e "\e[37mINFO\e[0m: ${@}"
}


# message_suggestion()
#   Print a suggestion message to stdout. Prefixes the output with "SUGGESTION"
#   styled in yellow (ANSI \e[33m) followed by the provided arguments.
message_suggestion(){
    echo -e "\e[33mSUGGESTION\e[0m: ${@}"
}

# message_success()
#   Print a success message to stdout. Prefixes the output with "SUCCESS"
#   styled in green (ANSI \e[32m) followed by the provided arguments.
message_success(){
    echo -e "\e[32mSUCCESS\e[0m: ${@}"
}