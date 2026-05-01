import React, { useState } from 'react'
import axios from "axios";
import './Bookapi_register.css'
import { useNavigate } from 'react-router-dom';

const Bookapi_register = () => {
  const navigate=useNavigate()
  const [username, setusername] = useState('')
  const [email, setemail] = useState('')
  const [password, setpassword] = useState('')
  const [Role, setRole] = useState('user')

  const Register=async(e)=>{
    e.preventDefault()
    await axios.post('http://127.0.0.1:8000/register/',{
      username,
      email,
      password,
      Role,
    })
    alert("Registeration Successfully")
    navigate('/')
  }

  return (
    <div className='container'>
      <form onSubmit={Register} className='form-box'>
        <input type='text' placeholder='Enter Username' onChange={(e)=>setusername(e.target.value)} />
        <input type='email' placeholder='Enter Email' onChange={(e)=>setemail(e.target.value)} />
        <input type='password' placeholder='Enter Password' onChange={(e)=>setpassword(e.target.value)} />
        <select onChange={(e)=>setRole(e.target.value)}>
          <option value={'user'}>User</option>
          <option value={'admin'}>Admin</option>
        </select>
        <button type='submit'>Register</button>
      </form>
    </div>
  )
}

export default Bookapi_register