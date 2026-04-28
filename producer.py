import pika

def enviar_evento(mensaje: str):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters("localhost")
    )
    channel = connection.channel()

    # Cola
    channel.queue_declare(queue="eventos")

    # Publicar evento
    channel.basic_publish(
        exchange="",
        routing_key="eventos",
        body=mensaje
    )

    print("Evento enviado:", mensaje)

    connection.close()