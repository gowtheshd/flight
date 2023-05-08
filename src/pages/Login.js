import React from 'react'
import "./Login.css"
const Login = () => {
  return (
    <div>
        <div class="container">
      <form action="#">
        <div class="title">Login</div>
        <div class="input-box underline">
            <input type="text" id="uname" placeholder="Enter Your Username" required/>
            <div class="underline"></div>
          </div>
        <div class="input-box">
          <input type="password" id="password" placeholder="Enter Your Password" required/>
          <div class="underline"></div>
        </div>
        <div class="input-box button">
          <input type="submit" name="" value="Login"/>
        </div>
      </form>
    </div>
    </div>
  )
}

export default Login