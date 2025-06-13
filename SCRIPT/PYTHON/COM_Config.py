WARNING: This message originated outside of the Marelli network 
BE CAREFUL before clicking any link or attachment. 


import serial

# Abre a porta serial (mesma usada no CAPL)
ser = serial.Serial('COM3', baudrate=9600, timeout=1)

print("Aguardando comando...")

while True:
    if ser.in_waiting:
        data = ser.readline().decode().strip()
        print(f"Recebido: {data}")

        if data == "start_test":
            print("Executando teste...")
            # Chamar função de teste, iniciar processo, etc.
