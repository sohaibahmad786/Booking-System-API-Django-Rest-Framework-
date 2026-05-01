import React, { useState } from 'react'
import axios from "axios";
import './Bookapi_dashboard.css'
import { useNavigate } from 'react-router-dom';

const Bookapi_dashboard = () => {
  const navigate=useNavigate()
  const [name, setname] = useState('')
  const [slots, setslots] = useState([])
  const [date, setdate] = useState('')
  const [time, settime] = useState('')

  const token=localStorage.getItem('token')
  
  const Available_slots=async()=>{
    const res=await axios.get(`http://127.0.0.1:8000/available/?date=${date}`,{
      headers:{
        Authorization:`Bearer ${token}`
      }
    })
    setslots(res.data.available_slot)
  }

const Booking=async()=>{
  await axios.post('http://127.0.0.1:8000/book/',{
    name,
    date,
    time,
  },{
    headers:{
      Authorization:`Bearer ${token}`
    }
  }
)
alert('Booking Done')
if(time != slots){
  alert('Sorry this time is not available for Booking')
}
}

const logout=()=>{
  localStorage.removeItem('token')
  navigate('/')
}

  return (
    <div className='dashboard'>
         <input type='text' placeholder='Enter Booking Name' onChange={(e)=>setname(e.target.value)} />
        <input type='date' onChange={(e)=>setdate(e.target.value)} />  
        <input type='time' placeholder='Select Time' onChange={(e)=>settime(e.target.value)} />
        <button onClick={Available_slots}>Check slots</button>
        <ul>
        {slots && slots.map((slot,index)=>(
          <li key={index} onClick={()=>settime(slot)}>{slot}</li>
        ))}
        </ul>
        <button onClick={Booking}>Book now</button>
        <button onClick={logout}>Logout</button>
    </div>
  )
}

export default Bookapi_dashboard