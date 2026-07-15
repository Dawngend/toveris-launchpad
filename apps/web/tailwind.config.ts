import type { Config } from "tailwindcss";
const config: Config = { content: ["./app/**/*.{ts,tsx}", "./components/**/*.{ts,tsx}"], theme: { extend: { colors: { safety: "#166534", cream: "#f8faf5" } } }, plugins: [] };
export default config;
