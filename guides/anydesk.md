# Conserto Anydesk

Para abrir o `Anydesk` digite no terminal:

    anydesk

Veridique qual é o ID de seu computador. Se ele começar com `684626` por favor execute as instruções a seguir: 

    sudo rm /etc/anydesk/service.conf

Depois digite no terminal:

    wget -qO - https://raw.githubusercontent.com/Insper/404/master/desktop%20ssd/patchs/patch_0_anydesk_chrome.sh | bash

Depois *reinicie o computador*:

    sudo reboot
