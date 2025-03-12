import React, { useEffect, useState } from "react";
import axios from "axios";

const Gallery = () => {
  const [galleryImages, setGalleryImages] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/images")
      .then((res) => setGalleryImages(res.data.images))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div className="min-h-screen flex flex-col items-center bg-[#0D0D2B] px-4 py-10">
      <h2 className="text-2xl sm:text-3xl font-bold text-center mb-6 bg-gradient-to-r from-fuchsia-500 to-violet-500 text-transparent bg-clip-text">
      Images Gallery 
      </h2>
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6 w-full max-w-5xl">
        {galleryImages.map((img) => (
          <div key={img.id} className="overflow-hidden rounded-lg shadow-lg border border-fuchsia-500">
            <img
              src={img.image_url}
              alt={img.prompt}
              className="w-full h-48 sm:h-64 object-cover transform hover:scale-105 transition duration-300"
            />
          </div>
        ))}
      </div>
    </div>
  );
};

export default Gallery;