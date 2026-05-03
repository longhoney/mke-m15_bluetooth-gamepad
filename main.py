def reTrai():
    l9110.control_motor(l9110.Motor.MOTOR_A, l9110.Rotate.FORWARD, 50)
    l9110.control_motor(l9110.Motor.MOTOR_B, l9110.Rotate.FORWARD, 75)
def Lui():
    l9110.control_motor(l9110.Motor.MOTOR_A, l9110.Rotate.BACKWARD, 50)
    l9110.control_motor(l9110.Motor.MOTOR_B, l9110.Rotate.BACKWARD, 50)
def Tien():
    l9110.control_motor(l9110.Motor.MOTOR_A, l9110.Rotate.FORWARD, 75)
    l9110.control_motor(l9110.Motor.MOTOR_B, l9110.Rotate.FORWARD, 75)

def on_mes_dpad_controller_id_microbit_evt():
    if control.event_value() == EventBusValue.MES_DPAD_BUTTON_A_DOWN:
        # Tiến tới
        basic.show_string("A")
        Tien()
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_B_DOWN:
        # Lùi về
        basic.show_string("B")
        Lui()
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_C_DOWN:
        # Rẽ trái
        basic.show_string("C")
        reTrai()
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_D_DOWN:
        # Rẽ phải
        basic.show_string("D")
        rePhai()
    elif control.event_value() == 9:
        basic.show_string("1")
    elif control.event_value() == 11:
        basic.show_string("2")
    elif control.event_value() == 13:
        basic.show_string("3")
    elif control.event_value() == 15:
        basic.show_string("4")
    else:
        Stop()
control.on_event(EventBusSource.MES_DPAD_CONTROLLER_ID,
    EventBusValue.MICROBIT_EVT_ANY,
    on_mes_dpad_controller_id_microbit_evt)

def rePhai():
    l9110.control_motor(l9110.Motor.MOTOR_A, l9110.Rotate.FORWARD, 75)
    l9110.control_motor(l9110.Motor.MOTOR_B, l9110.Rotate.FORWARD, 50)
def Stop():
    l9110.pause_motor(l9110.Motor.MOTOR_A)
    l9110.pause_motor(l9110.Motor.MOTOR_B)
Stop()
bluetooth.start_led_service()
basic.show_icon(IconNames.GHOST)