from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from pydantic import BaseModel
from database import get_db
from models import Image

app = FastAPI()

class ImageCreate(BaseModel):
    prompt: str
    image_url: str
    style: str

@app.get("/images")
async def get_images(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Image))
    images = result.scalars().all()
    
    return {"images": [{"id": img.id, "prompt": img.prompt, "image_url": img.image_url, "style": img.style} for img in images]}

@app.post("/images")
async def create_image(image: ImageCreate, db: AsyncSession = Depends(get_db)):
    new_image = Image(prompt=image.prompt, image_url=image.image_url, style=image.style)
    db.add(new_image)
    await db.commit()
    await db.refresh(new_image)
    return {"message": "Image created successfully", "image": {"id": new_image.id, "prompt": new_image.prompt, "image_url": new_image.image_url, "style": new_image.style}}

@app.delete("/images/{id}")
async def delete_image(id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Image).where(Image.id == id))
    image = result.scalars().first()

    if not image:
        raise HTTPException(status_code=404, detail="Image not found")

    await db.delete(image)
    await db.commit()
    return {"message": "Image deleted successfully"}


@app.delete("/images/{id}")
async def delete_image(id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Image).where(Image.id == id))
    image = result.scalars().first()

    if not image:
        raise HTTPException(status_code=404, detail="Image not found")

    await db.delete(image)
    await db.commit()
    return {"message": "Image deleted successfully"}
