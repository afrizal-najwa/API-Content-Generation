import os
from openai import OpenAI
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field 
from dotenv import load_dotenv

# ----------------------------------------------------
# 1. SETUP & INISIALISASI
# ----------------------------------------------------

load_dotenv()

app_description = """
🚀 **API Generator Konten Otomatis**

API ini memungkinkan Anda untuk menghasilkan berbagai jenis konten teks secara dinamis menggunakan model AI canggih dari OpenAI.

Anda bisa membuat:
* Artikel Blog
* Caption Media Sosial
* Teks Iklan (Copywriting)
* Dan banyak lagi!
"""

app = FastAPI(
    title="API Generator Konten Otomatis",
    description=app_description, 
    version="1.1.0",
    contact={ 
        "name": "Afrizal Najwa Syauqi",
        "email": "najwaafrizal@gmail.com",
    },
)

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY tidak ditemukan.")
client = OpenAI(api_key=api_key)


# ----------------------------------------------------
# 2. DEFINISI MODEL DATA (Pydantic)
# ----------------------------------------------------

class ContentRequest(BaseModel):
    topic: str = Field(..., description="Topik utama dari konten yang ingin dibuat.", example="Manfaat AI dalam Edukasi")
    tone: str = Field("profesional", description="Gaya bahasa yang diinginkan untuk konten.", example="Informatif")
    target_platform: str = Field("artikel blog", description="Platform target untuk konten (misal: 'artikel blog', 'postingan linkedin').", example="Artikel Blog")
    max_tokens: int = Field(500, description="Panjang maksimal konten dalam satuan token.", example=500)

class ContentResponse(BaseModel):
    generated_content: str
    model_used: str

# ----------------------------------------------------
# 3. LOGIKA INTI & PROMPT ENGINEERING
# ----------------------------------------------------
def create_system_prompt(request: ContentRequest) -> str:
    prompt = f"""
    Anda adalah seorang penulis konten AI yang ahli. Tugas Anda adalah membuat konten berdasarkan permintaan pengguna.
    Instruksi:
    1. Topik Utama: '{request.topic}'
    2. Gaya Bahasa (Tone): '{request.tone}'
    3. Target Platform: '{request.target_platform}'
    4. Panjang Maksimal: Sekitar {request.max_tokens} token atau kurang.
    Pastikan hasil tulisan Anda terstruktur dengan baik, relevan dengan topik, dan sesuai dengan gaya bahasa yang diminta.
    """
    return prompt.strip()


# ----------------------------------------------------
# 4. ENDPOINT API
# ----------------------------------------------------

@app.get("/", tags=["Status"])
def read_root():
    """Endpoint dasar untuk mengecek status API."""
    return {"status": "API Generator Konten Aktif"}

@app.post(
    "/generate/content",
    response_model=ContentResponse,
    tags=["Content Generation"], 
    summary="Menghasilkan Konten Teks Dinamis", 
    description="Endpoint utama untuk menghasilkan konten. Kirim topik dan parameter lain untuk mendapatkan teks yang dibuat oleh AI." 
)
async def generate_content_endpoint(request: ContentRequest):
    system_prompt = create_system_prompt(request)
    model_to_use = "gpt-4o"
    try:
        completion = client.chat.completions.create(
            model=model_to_use,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Tolong buatkan kontennya sekarang."}
            ],
            max_tokens=request.max_tokens,
            temperature=0.7
        )
        generated_text = completion.choices[0].message.content.strip()
        return ContentResponse(
            generated_content=generated_text,
            model_used=model_to_use
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
