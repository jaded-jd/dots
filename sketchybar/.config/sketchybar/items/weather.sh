#!/bin/bash

sketchybar --add item weather right \
           --set weather update_freq=60 \
                      script="$PLUGIN_DIR/weather.sh" \
                      click_script="open -a Weather"
