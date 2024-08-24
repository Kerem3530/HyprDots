if status is-interactive
    neofetch
end

set -gx PATH $PATH /home/kerem/scripts

function pli
    pip3 install --break-system-packages $argv
end
