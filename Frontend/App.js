import React from 'react'
import Bookapi_login from './DRF/Bookapi_login'
import Bookapi_register from './DRF/Bookapi_register'
import Bookapi_dashboard from './DRF/Bookapi_dashboard'
import { BrowserRouter as Router,Routes,Route } from 'react-router-dom'

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path='/' element={<Bookapi_login />} />
        <Route path='/register' element={<Bookapi_register />} />
        <Route path='/dashboard' element={<Bookapi_dashboard />} />
      </Routes>
    </Router>
  )
}

export default App
