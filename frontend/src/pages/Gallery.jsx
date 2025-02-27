import { useEffect, useState } from "react";
import axios from "axios";

const Gallery = () => {
    const [images, setImages] = useState([]);

    useEffect(() => {
        axios.get("http://127.0.0.1:8000/images").then((res) => setImages(res.data.images));
    }, []);

    const Gallery = () => {
        return (
            <div className="bg-gray-900 min-h-screen text-white p-10">
                <h2 className="text-3xl font-bold mb-6 text-center">Galería de Imágenes</h2>
                <div className="grid grid-cols-3 gap-6">
                    <img src="https://example.com/image.jpg" className="rounded-lg shadow-lg transform hover:scale-105 transition duration-300" />
                    <img src="https://example.com/image2.jpg" className="rounded-lg shadow-lg transform hover:scale-105 transition duration-300" />
                    <img src="https://example.com/image3.jpg" className="rounded-lg shadow-lg transform hover:scale-105 transition duration-300" />
                </div>
            </div>
        );
    };
    
};

export default Gallery;
