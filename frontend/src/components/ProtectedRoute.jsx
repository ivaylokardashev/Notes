import {Navigate} from "react-router-dom"
import {jwtDecode} from "jwt-decode"
import api from "../api"
import { REFRESH_TOKEN, ACCESS_TOKEN } from "../constants"
import { useState, useEffect } from "react"



function ProtectedRoute({children}) {
    const [isAuthorized, setIsAuthorized] = useState(null);
    
    // Check if the user have authorizetion for protected routes
    useEffect(() => {
        auth().catch(() => setIsAuthorized(false))
    }, [])

    // Function for refreshing token
    const refreshToken = async () => {
        const refreshToken = localStorage.getItem(REFRESH_TOKEN);
        try {
            // Ask backend for responce and to take new access token
            const res = await api.post("/api/token/refresh/", {
                refresh: refreshToken,
            });
            // Check if the responce is ok
            if (res.status === 200) {
                localStorage.setItem(ACCESS_TOKEN, res.data.access) // Change the access token with new one
                setIsAuthorized(true)
            } else {
                setIsAuthorized(false)
            }
        } catch (error) {
            console.log(error);
            setIsAuthorized(false);
        }
    }

    // Check if the user access token is expired
    const auth = async () => {
        const token = localStorage.getItem(ACCESS_TOKEN);
        // Check if the user have access token
        if (!token) {
            setIsAuthorized(false);
            return;
        }
        const decoded = jwtDecode(token);   // decode JWT token so we can get its exp parameters
        const tokenExpiration = decoded.exp;
        const now = Date.now() / 1000;

        if (tokenExpiration < now) {
            await refreshToken();
        } else {
            setIsAuthorized(true);
        }
    }

    if (isAuthorized === null) {
        return <div>Loading...</div>
    }
    return isAuthorized ? children : <Navigate to="/login" />;
}

export default ProtectedRoute;