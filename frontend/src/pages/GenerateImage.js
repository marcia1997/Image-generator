import { useState } from "react";
import axios from "axios";
import { useAuth } from "../context/AuthContext";

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
        <div>
            <h2>Generador de Imágenes</h2>
            {user && <p>Bienvenido, {user}!</p>}
            <input type="text" placeholder="Describe la imagen..." value={prompt} onChange={(e) => setPrompt(e.target.value)} />
            <button onClick={generateImage}>Generar</button>
            {imageUrl && <img src={imageUrl} alt="Generado" />}
        </div>
    );
};

export default GenerateImage;
