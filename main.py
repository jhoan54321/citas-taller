from fastapi import FastAPI, HTTPException
import asyncio

from redis_client import r
from producer import enviar_evento

app = FastAPI()

# Crear cita
@app.post("/crear_cita")
async def crear_cita(horario: str):
    if not horario:
        raise HTTPException(status_code=400, detail="Horario requerido")

    # Lock en Redis (evita duplicados)
    lock = r.set(f"cita:{horario}", "ocupado", nx=True, ex=60)

    if not lock:
        raise HTTPException(status_code=400, detail="Horario ocupado")

    print(f"Cita creada para {horario}")

    enviar_evento(f"Cita creada {horario}")

    await asyncio.sleep(1)

    return {"mensaje": f"Cita creada para {horario}"}


# Cancelar cita
@app.delete("/cancelar_cita")
async def cancelar_cita(horario: str):
    if not r.exists(f"cita:{horario}"):
        raise HTTPException(status_code=404, detail="Cita no existe")

    r.delete(f"cita:{horario}")

    enviar_evento(f"Cita cancelada {horario}")

    return {"mensaje": f"Cita cancelada {horario}"}


# Ver horarios ocupados
@app.get("/horarios")
def ver_horarios():
    keys = r.keys("cita:*")
    horarios = [k.split(":")[1] for k in keys]
    return {"horarios_ocupados": horarios}