#!/usr/bin/env bash

cd ..

layout_ui_path='resources/layout_ui'
layout_path='GaleriaViewer/view/layout'

# Updating layouts.
# iterating over all files in layout_ui directory
for file in ${layout_ui_path}/*.ui; do

    # cutting out name of desired file
    name=`echo "$file" | rev | cut -d '/' -f1 | rev | cut -d '.' -f1`;

    # generating name for new py file
    destination="$layout_path/$name.py";

    # checking if this file exists and echoing appropriate message
    if [[ -e ${destination} ]]
    then
        echo "Updated layout: $name.py";
    else
        echo "Created layout: $name.py";
    fi;

    # creating file
    echo "$(pyuic5 ${file})" > ${destination};
done

# Removing old layouts.
# iterating over all files in layout directory
for file in ${layout_path}/*.py; do

    # cutting out name of desired file
    name=`echo "$file" | rev | cut -d '/' -f1 | rev | cut -d '.' -f1`;

    # generating name of file which we are gonna check for it existence
    destination="$layout_ui_path/$name.ui";

    # checking if this file exists and if not then removing obsolete layout
    if [[ ! -e ${destination} ]]
    then
        "$(rm ${file})";
        echo "Removed layout: $name.py";
    fi;
done