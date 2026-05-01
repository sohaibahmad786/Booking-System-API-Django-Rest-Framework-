import React, { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import axios from "axios";
import './Bookapi_login.css'

const Bookapi_login = () => {
    const [username, setusername] = useState('')
    const [password, setpassword] = useState('')
    const navigate=useNavigate()
    
    const Login=async(e)=>{
        e.preventDefault()
        const res=await axios.post('http://127.0.0.1:8000/login/',{
            username,
            password,
        })
        localStorage.setItem('token',res.data.access)
        navigate('/dashboard')
    }

  return (
    <div className='container'>
        <form onSubmit={Login} className='form-box'>
            <input type='text' placeholder='Enter Your Username' onChange={(e)=>setusername(e.target.value)} />
            <input type='password' placeholder='Enter Your Passowrd' onChange={(e)=>setpassword(e.target.value)} />
            <button type='submit'>Login</button>
            <p>if you don't have account then,<Link to={'/register'}>Sign up</Link> </p>
        </form>
    </div>
  )
}

export default Bookapi_login