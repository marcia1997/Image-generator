import { useState } from "react";
import axios from "axios";
import "../styles/globals.css";
import "../index.css";

const GenerateImage = () => {
  const [prompt, setPrompt] = useState("");
  const [generatedUrl, setGeneratedUrl] = useState("");

  const handleGenerate = async () => {
    try {
      const response = await axios.post("http://127.0.0.1:8000/generate", { prompt, style: "cyberpunk" });
      setGeneratedUrl(response.data.image.url);
    } catch (error) {
      console.error("Error generating image", error);
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-[#0D0D2B] text-white p-6">
      <h2 className="text-2xl sm:text-3xl font-bold text-center mb-6">
        ✨ AI Image Generator ✨
      </h2>
      <input
        type="text"
        placeholder="Describe the image..."
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        className="w-80 p-3 rounded-lg bg-[#191946] text-white mb-4 outline-none border border-transparent focus:border-fuchsia-500 hover:border-fuchsia-500 transition"
      />
      <button 
        onClick={handleGenerate} 
        className="bg-fuchsia-600 hover:bg-fuchsia-700 text-white font-semibold p-3 rounded-lg transition"
      >
        Generate Image
      </button>
      {generatedUrl && (
        <div className="mt-6">
          <img src={generatedUrl} alt="Generated" className="rounded-lg shadow-lg border border-fuchsia-500" />
        </div>
      )}
    </div>
  );
};

export default GenerateImage;
