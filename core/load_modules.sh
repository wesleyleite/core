#!/bin/bash

module_dir="$1"
blueprint_name="$2"

echo $module_dir $blueprint_name

[ -e "$module_dir" -a \
	! -z "$blueprint_name" ] && {
	echo "app.register_blueprint($blueprint_name)" >> blue_register.py
	echo "from $module_dir import $blueprint_name" >> imports.py
} || {
	echo "$0 MODULE_DIR_NAME BLUEPRINT_NAME"
}


