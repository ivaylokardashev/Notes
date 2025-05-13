import Form from "../components/Form"
import { useNavigate } from "react-router-dom";


function Register() {
    return <Form route="/api/user/register/" method="register" />
}

export default Register