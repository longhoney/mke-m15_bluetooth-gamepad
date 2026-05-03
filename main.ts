control.onEvent(EventBusSource.MES_DPAD_CONTROLLER_ID, EventBusValue.MICROBIT_EVT_ANY, function () {
    if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_A_DOWN) {
        basic.showArrow(ArrowNames.North)
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_B_DOWN) {
        basic.showArrow(ArrowNames.South)
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_C_DOWN) {
        basic.showArrow(ArrowNames.West)
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_D_DOWN) {
        basic.showArrow(ArrowNames.East)
    } else if (control.eventValue() == 9) {
        basic.showString("1")
    } else if (control.eventValue() == 11) {
        basic.showString("2")
    } else if (control.eventValue() == 13) {
        basic.showString("3")
    } else if (control.eventValue() == 15) {
        basic.showString("4")
    } else {
        basic.clearScreen()
    }
})
bluetooth.startLEDService()
basic.showIcon(IconNames.Ghost)
