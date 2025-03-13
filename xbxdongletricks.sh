#!/bin/bash

# Define the password
PASSWORD="bazzite"

# Force sudo authentication at the beginning of the script
echo "$PASSWORD" | sudo -S -v > /dev/null

# Function to set LED brightness using a slider
set_brightness() {
    brightness=$(kdialog --slider "Select brightness level (0-15):" 0 15 5)
    if [[ -z "$brightness" ]]; then
        return  # Exit if user cancels
    fi
    if [[ "$brightness" =~ ^([0-9]|1[0-5])$ ]]; then
        echo "$PASSWORD" | sudo -S tee /sys/class/leds/gip*/brightness <<< "$brightness" > /dev/null
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
        echo "$PASSWORD" | sudo -S tee /sys/class/leds/gip*/mode <<< "$mode" > /dev/null
    else
        kdialog --error "Invalid mode value. Must be between 0 and 5."
    fi
}

# Function to toggle pairing mode and show current state
toggle_pairing() {
    current_status=$(cat /sys/bus/usb/drivers/xone-dongle/*/pairing 2>/dev/null)

    if [[ "$current_status" == "1" ]]; then
        # If pairing is enabled, display the current state and then disable it
        echo "$PASSWORD" | sudo -S tee /sys/bus/usb/drivers/xone-dongle/*/pairing <<< 0 > /dev/null
    elif [[ "$current_status" == "0" ]]; then
        # If pairing is disabled, display the current state and then enable it
        echo "$PASSWORD" | sudo -S tee /sys/bus/usb/drivers/xone-dongle/*/pairing <<< 1 > /dev/null
    else
        # If unable to read the current status, show an error message
        kdialog --error "Unable to determine the current pairing mode state."
    fi
}

# Function to get the current pairing state
get_pairing_state() {
    current_status=$(cat /sys/bus/usb/drivers/xone-dongle/*/pairing 2>/dev/null)
    if [[ "$current_status" == "1" ]]; then
        echo "Enabled"
    elif [[ "$current_status" == "0" ]]; then
        echo "Disabled"
    else
        echo "Unknown"
    fi
}

# Main menu loop
while true; do
    # Get current pairing state to display in the menu
    pairing_state=$(get_pairing_state)

    # Display the menu with the current pairing state
    choice=$(kdialog --radiolist "Select an option:" \
        1 "Set LED Brightness" off \
        2 "Set LED Mode" off \
        3 "Toggle Pairing Mode ($pairing_state)" off \
        4 "Exit" on)

    # Exit if the user cancels or closes the dialog
    if [[ -z "$choice" ]]; then
        exit 0
    fi

    case $choice in
        1) set_brightness ;;
        2) set_mode ;;
        3) toggle_pairing ;;
        4) exit 0 ;;
    esac
done
