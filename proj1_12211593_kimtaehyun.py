#! /bin/bash

touch temp.sh
cat "$1" > temp.sh

read -p "Enter your SID : " sid
read -p "Enter your name : " name

while true
do
    echo "hi ${sid}_${name}!"
    echo "[ MENU ]"
    echo "1. Enable/disable empty line removal"
    echo "2. Enable/disable comment removal"
    echo "3. Enable/diable duplicate whitespaces among words"
    echo "4. Add the line number"
    echo "5. Change the variable name"
    echo "6. Remove \${} in arithmathic expansion"
    echo "7. Export new file"
    echo "8. Exit"
    echo "---------------------------------"
    read -p "Enter your choice [ 1-8 ] " number

    case ${number} in
    1)
        read -p "Do you want to remove all blank line?(y/n) : " enabled
        
        if [ ${enabled} = "y" ]
        then
            sed -i '/^[[:space:]]*$/d' temp.sh          
            echo "Remove all blank line."
            cat temp.sh
            echo " "
        elif [ ${enabled} = "n" ]
        then
            echo "Nothing changed."
            cat temp.sh
            echo " "
        else
            echo "You should enter y or n! Nothing changed!"
            echo " "
        fi
        ;;
    2)
        read -p "Do you want to remove all command line?(y/n) : " enabled

        if [ ${enabled} = "y" ]
        then
            sed -i -E '/#[^!].*$/d' temp.sh
            echo "Remove all command line."
            cat temp.sh
            echo " "
        elif [ ${enabled} = "n" ]
        then
            echo "Nothing changed."
            cat temp.sh
            echo " "
        else
            echo "You should enter y or n! Nothing changed!"
            echo " "
        fi
        ;;
    3)
        #doesn't working
        read -p "Do you want to remove dublicate whitespaces?(y/n) : " enabled

        if [ ${enabled} = "y" ]
        then
            sed -i -E 's/\>[[:space:]]*\</ /g' temp.sh
            echo "Remove dublicate whitespaces."
            cat temp.sh
            echo " "
        elif [ ${enabled} = "n" ]
        then
            echo "Nothing changed."
            cat temp.sh
            echo " "
        else
            echo "You should enter y or n! Nothing changed!"
            echo " "
        fi
        ;;
    4)
        #doesn't working
        read -p "Where do you want to add whether the start or the end of the line? (s/e) : " where
        if [ ${where} = "s" ]
        then 
            sed '/./=' temp.sh | sed '/./N; s/\n/ /'
            echo "line number added to start of the line"
            cat temp.sh
            echo " "
        elif [ ${where} = "e" ]
        then
            echo "line number added to end of the line"
            echo " "
        else 
            echo "You should enter s or e! Nothing changed!"
            echo " "
        fi
        ;;
    5)
        echo "Enter the variable to be changed and the new variable name."
        read -p "Variable name to be changed: " oldname
        read -p "New variable name: " newname
        
        sed -i "s/$oldname/$newname/g" temp.sh
        echo "${oldname} is changed to ${newname}!"
        cat temp.sh
        echo " "
        ;;
    6)
        #doesn't working
        ;;
    7)
        read -p "Do you want to export a new file?(y/n)" enabled

        if [ ${enabled} = "y" ]
        then
            touch export.sh
            cat temp.sh > export.sh
            echo "file exported to 'export.sh'"
            echo " "
        else
            echo "Nothing changed"
            echo " "
        fi
        ;;
    8)
        echo "Goodbye ${sid}_${name}!"
        break;;
    *)
        echo "Please enter number between [ 1-8 ]"
        continue;;
    esac
done
