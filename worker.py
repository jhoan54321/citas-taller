import pika
import asyncio

# Funciones async
async def notificar(mensaje):
    await asyncio.sleep(1)
    print("Notificación enviada:", mensaje)

async def registrar_log(mensaje):
    await asyncio.sleep(1)
    print("Log registrado:", mensaje)

async def procesar_evento(mensaje):
    await asyncio.gather(
        notificar(mensaje),
        registrar_log(mensaje)
    )

# Callback RabbitMQ
def callback(ch, method, properties, body):
    mensaje = body.decode()
    print("Evento recibido:", mensaje)

    asyncio.run(procesar_evento(mensaje))


# Conexión RabbitMQ
connection = pika.BlockingConnection(
    pika.ConnectionParameters("localhost")
)

channel = connection.channel()

channel.queue_declare(queue="eventos")

channel.basic_consume(
    queue="eventos",
    on_message_callback=callback,
    auto_ack=True
)

print("Worker escuchando eventos...")

channel.start_consuming()