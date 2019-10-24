if [[ $EUID -ne 0 ]]; then
   echo "Please run as root" 
   exit 1
fi

apt-get install python3

apt-get install netdiscover