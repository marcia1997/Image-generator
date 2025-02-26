from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from pydantic import BaseModel
from database import get_db
from models import User, Image
from auth import hash_password, verify_password, create_access_token
from fastapi.security import OAuth2PasswordRequestForm

# Init FastAPI
app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Schemas
class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str

class ImageCreate(BaseModel):
    prompt: str
    image_url: str
    style: str

### --- AUTH --- ###

@app.post("/register")
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    """ Registra un nuevo usuario con contraseña encriptada. """
    result = await db.execute(select(User).where(User.username == user.username))
    existing_user = result.scalars().first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Username already taken")

    hashed_password = hash_password(user.password)
    new_user = User(username=user.username, hashed_password=hashed_password)
    
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return {"message": "User created successfully"}

@app.post("/login", response_model=TokenResponse)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db),
):
    """ Inicia sesión usando `x-www-form-urlencoded`. """
    print(f"📥 Received form-data: username={form_data.username}, password={form_data.password}")

    result = await db.execute(select(User).where(User.username == form_data.username))
    user = result.scalars().first()

    if not user:
        print("❌ Usuario no encontrado.")
        raise HTTPException(status_code=401, detail="Invalid username or password")

    if not verify_password(form_data.password, user.hashed_password):
        print(f"❌ Contraseña incorrecta. Ingresada: {form_data.password}, En BD: {user.hashed_password}")
        raise HTTPException(status_code=401, detail="Invalid username or password")

    access_token = create_access_token({"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/login-json", response_model=TokenResponse)
async def login_json(user_data: UserLogin, db: AsyncSession = Depends(get_db)):
    """ Inicia sesión con JSON (Content-Type: application/json). """
    print(f"📥 Received JSON: {user_data}")

    result = await db.execute(select(User).where(User.username == user_data.username))
    user = result.scalars().first()

    if not user:
        print("❌ Usuario no encontrado.")
        raise HTTPException(status_code=401, detail="Invalid username or password")

    if not verify_password(user_data.password, user.hashed_password):
        print(f"❌ Contraseña incorrecta. Ingresada: {user_data.password}, En BD: {user.hashed_password}")
        raise HTTPException(status_code=401, detail="Invalid username or password")

    access_token = create_access_token({"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

### --- Images --- ###

@app.get("/images")
async def get_images(db: AsyncSession = Depends(get_db)):
    """ Obtiene todas las imágenes almacenadas. """
    result = await db.execute(select(Image))
    images = result.scalars().all()
    
    return {"images": [{"id": img.id, "prompt": img.prompt, "image_url": img.image_url, "style": img.style} for img in images]}

@app.post("/images")
async def create_image(image: ImageCreate, db: AsyncSession = Depends(get_db)):
    """ Guarda una nueva imagen en la base de datos. """
    new_image = Image(prompt=image.prompt, image_url=image.image_url, style=image.style)
    db.add(new_image)
    await db.commit()
    await db.refresh(new_image)
    return {"message": "Image created successfully", "image": {"id": new_image.id, "prompt": new_image.prompt, "image_url": new_image.image_url, "style": new_image.style}}

@app.delete("/images/{id}")
async def delete_image(id: int, db: AsyncSession = Depends(get_db)):
    """ Elimina una imagen por ID si existe. """
    result = await db.execute(select(Image).where(Image.id == id))
    image = result.scalars().first()

    if not image:
        raise HTTPException(status_code=404, detail="Image not found")

    await db.delete(image)
    await db.commit()
    return {"message": "Image deleted successfully"}
