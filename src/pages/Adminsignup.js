import React from 'react'
import "./Signup.css"
const Adminsignup = () => {
  return (
    <div>
        <div class="container">
        <form action="#">
        <div class="title">Signup</div>
        <div class="input-box underline">
            <input type="text" id="uname" placeholder="Enter Your Username" required/>
            <div class="underline"></div>
          </div>
        
        <div class="input-box">
          <input type="password" id="password1" placeholder="Enter Your Password" required/>
          <div class="underline"></div>
        </div>
        
        <div class="input-box button">
          <input type="submit" name="" value="Signup"/>
        </div>
        </form>
        </div>
    </div>
  )
}

export default Adminsignup