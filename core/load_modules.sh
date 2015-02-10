#!/bin/bash

module_dir="$1"
[ -e "$module_dir" ] && {
	blueprint_name="$(cat $module_dir/__init__.py |
		grep 'Blueprint(' |
		cut -d \= -f1)"


	[ ! -z "$blueprint_name" ] && {
		[ -z "$(grep $blueprint_name blue_register.py)" -a \
			-z "$(grep $module_dir imports.py)" ] && {
			echo "app.register_blueprint($blueprint_name)" >> blue_register.py
			echo "from $module_dir import $blueprint_name" >> imports.py
		} || {
			echo "Module or Blueprint already exist!"
		}
	} || {
		echo "$0 MODULE_DIR_NAME"
	}
} || echo "Module dir not found"
