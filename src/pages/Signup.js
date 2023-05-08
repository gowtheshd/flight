import React, { useState } from 'react'
import "./Signup.css"
import  axios from "axios"
const Signup = () => {
  const handleSubmit=(e)=>{
    // const {data} = await axios.post('/user', document.querySelector('#my-form'), {
    //   headers: {
    //     'Content-Type': 'application/json'
    //   }
    // })
    axios.post('/user', {
      firstName: 'Fred',
      lastName: 'Flintstone'
    })
    .then(function (response) {
      console.log(response);
    })
    .catch(function (error) {
      console.log(error);
    });
  }
  return (
    <div>
        <div class="container">
        <form onSubmit={handleSubmit}>
        <div class="title">Signup</div>
        name<input name="name" type="text"></input>
        <br></br>
        email<input name="email" type="email"></input>
        <br></br>
        phone<input name="phone" type="text"></input>
        <br></br>
        pwd<input name="pwd" type="password"></input>
        <br></br>
        <input type="submit"></input>
        </form>
        </div>
    </div>
  )
}

export default Signup