#!/bin/bash
# Colorful prompt in Mac

## Enter current directory

    cd `dirname $0`

## Create .profile if necessary

    PROFILE=$HOME/.profile

    if [ ! -f $PROFILE ]; then
        echo "Creating $PROFILE with colorful config"
        touch $PROFILE
    fi

## Function to make promt colorful

    function colorful() {
        cat >> $PROFILE <<-EOF
        # Colorful command
        export PS1="\[\033[36m\]\u\[\033[m\]@\[\033[32m\]\h:\[\033[33;1m\]\w\[\033[m\]\$ "
        export CLICOLOR=1
        export LSCOLORS=ExFxBxDxCxegedabagacad
        alias ls='ls -GFh'
	EOF
    }

## Add configuration to .profile if needed

    if grep -q "# Colorful command" $PROFILE; then
        MESSAGE="The command is already colorful"
    else
        MESSAGE="Appending coloful config in $PROFILE"
        colorful
    fi

    echo $MESSAGE

### ref: <http://osxdaily.com/2013/02/05/improve-terminal-appearance-mac-os-x/>
