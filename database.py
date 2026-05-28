
from supabase import create_client

SUPABASE_URL = "https://kplcpanukoibdslteyfl.supabase.co"
SUPABASE_KEY = "sb_publishable_dBFl-nkZjqjMeCW305J1DQ_NrRFUqSP"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def obtener_tareas(user_id):
    response = supabase.table("tareas").select("*").eq("user_id", user_id).order("id").execute()
    return response.data

def agregar_tarea(titulo, user_id):
    supabase.table("tareas").insert({"titulo": titulo, "user_id": user_id}).execute()

def completar_tarea(id):
    tarea = supabase.table("tareas").select("completada").eq("id", id).execute().data[0]
    nuevo_estado = not tarea["completada"]
    supabase.table("tareas").update({"completada": nuevo_estado}).eq("id", id).execute()

def eliminar_tarea(id):
    supabase.table("tareas").delete().eq("id", id).execute()