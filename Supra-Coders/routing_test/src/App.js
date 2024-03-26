import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

const Home = () => (
  <h1>Home</h1>
)
const Profile = () => (
  <h1>User Profile</h1>
)
const SignUp = () => (
  <h1>Sign Up</h1>
)

const App = () => (
  <Router>
    <Routes>
      <Route path='/home' element={<Home />}/>
      <Route path='/profile' element={<Profile />}/>
      <Route path='/signup' element={<SignUp />}/>
    </Routes>
  </Router>
)

export default App;
