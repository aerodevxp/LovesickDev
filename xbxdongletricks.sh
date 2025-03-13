#!/bin/bash

# Define the password
PASSWORD="bazzite"

# Function to set LED brightness using a slider
set_brightness() {
    brightness=$(kdialog --slider "Select brightness level (0-15):" 0 15 5)
    if [[ -z "$brightness" ]]; then
        return  # Exit if user cancels
    fi
    if [[ "$brightness" =~ ^([0-9]|1[0-5])$ ]]; then
        echo "$PASSWORD" | sudo -S tee /sys/class/leds/gip*/brightness <<< "$brightness"
    else
        kdialog --error "Invalid brightness value. Must be between 0 and 15."
    fi
}

# Function to set LED mode using a slider
set_mode() {
    mode=$(kdialog --slider "Select LED mode (0-5):" 0 5 2)
    if [[ -z "$mode" ]]; then
        return  # Exit if user cancels
    fi
    if [[ "$mode" =~ ^[0-5]$ ]]; then
        echo "$PASSWORD" | sudo -S tee /sys/class/leds/gip*/mode <<< "$mode"
    else
        kdialog --error "Invalid mode value. Must be between 0 and 5."
    fi
}

# Function to enable pairing mode only if it's not already enabled
enable_pairing() {
    current_status=$(cat /sys/bus/usb/drivers/xone-dongle/*/pairing 2>/dev/null)
    if [[ "$current_status" == "1" ]]; then
        kdialog --msgbox "Pairing mode is already enabled."
    else
        echo "$PASSWORD" | sudo -S tee /sys/bus/usb/drivers/xone-dongle/*/pairing <<< 1
        kdialog --msgbox "Pairing mode enabled."
    fi
}

# Main menu loop
while true; do
    choice=$(kdialog --title "Xbox Dongle Utilities" --radiolist "Select an option:" \
        1 "Set LED Brightness" off \
        2 "Set LED Mode" off \
        3 "Enable Pairing Mode" off \
        4 "Exit" on)

    # Exit if the user cancels or closes the dialog
    if [[ -z "$choice" ]]; then
        exit 0
    fi

    case $choice in
        1) set_brightness ;;
        2) set_mode ;;
        3) enable_pairing ;;
        4) exit 0 ;;
    esac
done
