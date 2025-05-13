import axios from "axios"
import { ACCESS_TOKEN } from "./constants" // This is the our token

const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL
})

// This is for pass JWT token
api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem(ACCESS_TOKEN);
        if (token) {
            config.headers.Authorization = `Bearer ${token}`
        }
        return config
    },
    (error) => {
        return Promise.reject(error)
    }
)

// We will use this object instead default axios
export default api