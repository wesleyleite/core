#!/bin/bash

op="$1"

remove() 
{
	local dir="$1"
	local bname="$(cat $dir/__init__.py |
		grep 'Blueprint(' |
		cut -d \= -f1)"
	
	sed -i "/from $dir import/d" imports.py &&
		echo '[ OK ] clean imports.py' ||
		echo '[ NO ] clean imports.py' 
	
	sed -i "/$(echo $bname)/d" blue_register.py && 
		echo '[ OK ] clean blue_register.py' ||
		echo '[ NO ] clean blue_register.py'
}

case $op in
	'add')
		module_dir="$(echo $2 |
			sed 's/\///g')"
		[ -e "$module_dir" ] && {
			blueprint_name="$(cat $module_dir/__init__.py |
				grep 'Blueprint(' |
				cut -d \= -f1 |
				sed 's/ $//')"
			
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
	;;
	'rm')
		directory="$2"
		if [ -z "$directory" ] ; then
			echo -e 'Are you want remove all the modules registered?\npress any key to confirm\nOR CTRL+C to cancel.'
			read -n 1 
			for directory in $( cat imports.py | cut -d ' ' -f 2 );
			do 
				remove "$directory"
			done
		else
			echo -e "remove module $directory.\npress any key to confirm\nOR CTRL+C to cancel"
			read -n 1
			remove "$directory"	
		fi
	;;
esac
