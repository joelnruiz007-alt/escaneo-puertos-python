#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para verificar si el puerto 80 está abierto en localhost
Autor: Tutorial para principiantes
"""

# Importamos la librería 'socket' que viene incluida en Python
# Esta librería nos permite trabajar con conexiones de red
import socket

# ============================================
# CONFIGURACIÓN
# ============================================

# Definimos el host que queremos revisar
# 'localhost' es tu propia computadora (también podría ser '127.0.0.1')
HOST = 'localhost'

# Definimos el puerto que queremos verificar
# El puerto 80 es el puerto estándar para servidores web (HTTP)
PUERTO = 80

# Tiempo máximo de espera en segundos antes de rendirse
# Si no hay respuesta en 3 segundos, asumimos que está cerrado
TIEMPO_ESPERA = 3

# ============================================
# FUNCIÓN PRINCIPAL
# ============================================

def verificar_puerto(host, puerto, timeout):
    """
    Esta función verifica si un puerto está abierto.
    
    Parámetros:
        host: La dirección del servidor (ej: 'localhost')
        puerto: El número de puerto a verificar (ej: 80)
        timeout: Segundos máximos de espera
    
    Retorna:
        True si el puerto está abierto
        False si el puerto está cerrado
    """
    
    # Creamos un objeto socket
    # AF_INET = Usamos IPv4 (el protocolo de internet más común)
    # SOCK_STREAM = Usamos TCP (conexión confiable)
    mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Establecemos el tiempo máximo de espera
    # Si no hay respuesta en este tiempo, se cancela el intento
    mi_socket.settimeout(timeout)
    
    try:
        # Intentamos conectarnos al host y puerto especificados
        # Si la conexión es exitosa, el puerto está ABIERTO
        resultado = mi_socket.connect_ex((host, puerto))
        
        # connect_ex() devuelve 0 si la conexión fue exitosa
        # Cualquier otro número significa que hubo un error
        if resultado == 0:
            return True   # ¡Puerto abierto!
        else:
            return False  # Puerto cerrado o bloqueado
            
    except socket.timeout:
        # Si se agota el tiempo de espera
        print(f"⏱️  Tiempo de espera agotado ({timeout} segundos)")
        return False
        
    except socket.error as error:
        # Si ocurre cualquier otro error de red
        print(f"❌ Error de conexión: {error}")
        return False
        
    finally:
        # IMPORTANTE: Siempre cerramos el socket al terminar
        # Esto libera los recursos del sistema
        mi_socket.close()


# ============================================
# EJECUCIÓN DEL SCRIPT
# ============================================

# Esta condición verifica que el script se ejecute directamente
# (y no sea importado como módulo desde otro archivo)
if __name__ == "__main__":
    
    # Mostramos un encabezado bonito
    print("=" * 50)
    print("🔌 VERIFICADOR DE PUERTO")
    print("=" * 50)
    print(f"📍 Host: {HOST}")
    print(f"🚪 Puerto: {PUERTO}")
    print("-" * 50)
    print("🔄 Verificando conexión...")
    print()
    
    # Llamamos a nuestra función y guardamos el resultado
    puerto_abierto = verificar_puerto(HOST, PUERTO, TIEMPO_ESPERA)
    
    # Mostramos el resultado final
    if puerto_abierto:
        print("✅ RESULTADO: El puerto 80 está ABIERTO")
        print("   (Hay un servidor web escuchando en localhost)")
    else:
        print("❌ RESULTADO: El puerto 80 está CERRADO")
        print("   (No hay ningún servidor web activo en localhost)")
    
    print()
    print("=" * 50)
