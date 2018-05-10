# My profile.d


## Usage

    ln -s `pwd` ~/.profile.d
    [[ ! `grep '. ~/.profile.d/\*' ~/.zshrc` ]] && echo '. ~/.profile.d/*' >> ~/.zshrc
