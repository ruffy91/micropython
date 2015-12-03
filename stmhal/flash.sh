arm-none-eabi-objcopy -Iihex -Obinary build-STM32F7DISC/firmware.hex build-STM32F7DISC/firmware.bin
st-flash --reset write /home/fabian/micropython/stmhal/build-STM32F7DISC/firmware.bin 0x8000000
