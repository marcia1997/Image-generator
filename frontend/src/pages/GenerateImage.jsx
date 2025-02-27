import { useState } from "react";
import axios from "axios";
import { useAuth } from "../context/AuthContext.jsx";

const GenerateImage = () => {
    const { user } = useAuth();
    const [prompt, setPrompt] = useState("");
    const [imageUrl, setImageUrl] = useState("");

    const generateImage = async () => {
        try {
            const response = await axios.post("http://127.0.0.1:8000/images", { prompt, image_url: "", style: "realistic" });
            setImageUrl(response.data.image.image_url);
        } catch (error) {
            alert("Error al generar la imagen.");
        }
    };

        return (
            <div className="flex flex-col items-center justify-center h-screen bg-gray-900 text-white">
                <h2 className="text-3xl font-bold mb-6">Generador de Imágenes AI</h2>
                <input type="text" placeholder="Describe la imagen..." className="w-80 p-3 rounded-lg bg-gray-800 text-white mb-4 outline-none" />
                <button className="bg-blue-500 hover:bg-blue-400 text-white font-semibold p-3 rounded-lg transition">
                    Generar Imagen
                </button>
                <div className="mt-6">
                    <img src="https://example.com/image.jpg" alt="Imagen Generada" className="rounded-lg shadow-lg" />
                </div>
            </div>
        );
    
};

export default GenerateImage;
