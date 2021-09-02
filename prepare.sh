#!/bin/bash

apt-get update
apt-get -q -y install curl zip unzip git
curl -s https://get.sdkman.io | bash
source "$HOME/.sdkman/bin/sdkman-init.sh"
