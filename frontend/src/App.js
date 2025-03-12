import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./pages/Login";     
import Register from "./pages/Register"; 
import Generate from "./pages/GenerateImage"; 
import Gallery from "./pages/Gallery";   

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/generate" element={<Generate />} />
        <Route path="/gallery" element={<Gallery />} />
        <Route path="*" element={<h1>Page not found</h1>} />
      </Routes>
    </Router>
  );
}

export default App;
