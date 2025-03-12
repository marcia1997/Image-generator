import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import "../styles/globals.css";
import "../index.css";

const Register = () => {
    const [email, setEmail] = useState("");
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const navigate = useNavigate();

    const handleRegister = async (e) => {
        e.preventDefault();
        try {
            await axios.post("http://127.0.0.1:8000/register", {
                email,
                username,
                password,
            });
            alert("User registered successfully. Now log in.");
            navigate("/login");
        } catch (error) {
            alert("Registration error: " + error.response?.data?.detail || "Try again");
        }
    };

    return (
        <div className="min-h-screen flex items-center justify-center bg-[#0D0D2B] px-4">
            <div className="bg-[#0D0D2B] border-4 border-fuchsia-500 p-6 sm:p-8 shadow-md rounded-md w-full max-w-sm">
                <h2 className="text-xl sm:text-2xl font-bold text-center mb-3 bg-gradient-to-r from-fuchsia-500 to-violet-500 text-transparent bg-clip-text">
                    Create an Account
                </h2>
                <p className="text-gray-300 text-center mb-4 text-sm sm:text-base">
                    Sign up to get started.
                </p>
                <form onSubmit={handleRegister}>
                    <input
                        type="email"
                        placeholder="Email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        className="w-full px-4 py-3 border border-transparent rounded-md mb-3 bg-[#191946] text-white placeholder-gray-400 focus:border-fuchsia-500 focus:outline-none hover:border-fuchsia-500 transition"
                        required
                    />
                    <input
                        type="text"
                        placeholder="Username"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        className="w-full px-4 py-3 border border-transparent rounded-md mb-3 bg-[#191946] text-white placeholder-gray-400 focus:border-fuchsia-500 focus:outline-none hover:border-fuchsia-500 transition"
                        required
                    />
                    <input
                        type="password"
                        placeholder="Password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        className="w-full px-4 py-3 border border-transparent rounded-md mb-4 bg-[#191946] text-white placeholder-gray-400 focus:border-fuchsia-500 focus:outline-none hover:border-fuchsia-500 transition"
                        required
                    />
                    <button
                        type="submit"
                        className="w-full bg-fuchsia-600 text-white py-3 rounded-md hover:bg-fuchsia-700 transition text-sm sm:text-base"
                    >
                        Sign Up
                    </button>
                </form>
            </div>
        </div>
    );
};

export default Register;
