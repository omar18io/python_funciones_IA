import subprocess

nombre_wifi = "WIFI-JERRY"

try:
    result = subprocess.run(
        ["netsh", "wlan", "show", "profile", nombre_wifi, "key=clear"],
        stdout=subprocess.PIPE,
        check=True,  # Esto generará una excepción si el comando falla
    )
    salida = result.stdout.decode("latin1")

    for linea in salida.split("\n"):
        if "Key Content" in linea or "Contenido de la clave" in linea:
            print("La contraseña de la red es : ", linea.split(":")[1].strip())

except subprocess.CalledProcessError as e:
    print(f"Error al ejecutar el comando netsh: {e}")
