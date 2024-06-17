#!/bin/bash

sketchybar --add item btc right \
           --set btc update_freq=900 \
                      script="$PLUGIN_DIR/btc.sh" \
                      click_script="open -a Arc https://www.coinspot.com.au/chart/btc"
