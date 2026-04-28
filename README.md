# citas-taller
# Descripción

Este proyecto implementa un sistema distribuido de citas médicas utilizando una arquitectura basada en eventos. El sistema permite la creación y cancelación de citas evitando conflictos de concurrencia mediante el uso de Redis, y procesa eventos de manera asíncrona usando RabbitMQ y AsyncIO.

El objetivo es demostrar un sistema desacoplado, concurrente y escalable.

# Arquitectura

El sistema sigue el siguiente flujo:

Cliente → API (FastAPI) → Redis (control de concurrencia) → RabbitMQ → Worker (AsyncIO) → Notificación y Log

# Componentes principales:
FastAPI: Punto de entrada para las solicitudes
Redis: Manejo de bloqueo para evitar citas duplicadas
RabbitMQ: Sistema de mensajería para eventos
Worker: Procesamiento asíncrono de eventos
# Estructura del Proyecto
proyecto/
│── main.py            # API principal
│── worker.py          # Consumidor de eventos
│── redis_client.py    # Conexión a Redis
│── producer.py        # Productor de eventos (RabbitMQ)
│── requirements.txt   # Dependencias
# Requisitos
Python 3.8+
Redis
RabbitMQ

Instalar dependencias:

pip install -r requirements.txt

# Tecnologías utilizadas
FastAPI
Redis
RabbitMQ
AsyncIO
Python
