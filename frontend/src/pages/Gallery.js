import { useEffect, useState } from "react";
import axios from "axios";

const Gallery = () => {
    const [images, setImages] = useState([]);

    useEffect(() => {
        axios.get("http://127.0.0.1:8000/images").then((res) => setImages(res.data.images));
    }, []);

    return (
        <div>
            <h2>Galería</h2>
            {images.map((img) => (
                <img key={img.id} src={img.image_url} alt={img.prompt} />
            ))}
        </div>
    );
};

export default Gallery;
