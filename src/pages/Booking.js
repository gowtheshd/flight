import React from 'react'
import "./Booking.css"
const Booking = () => {
  return (
    <div>
      <div class="container">
        <form action="#">
        <div class="title">Ticket Booking</div>
        <div class="input-box underline">
            <input type="text" id="pname" placeholder="Enter Passenger Name" required/>
            <div class="underline"></div>
          </div>
        <div class="input-box underline">
            <input type="text" id="gender" placeholder="Gender" required/>
            <div class="underline"></div>
        </div>
        <div class="input-box underline">
            <input type="number" id="age" placeholder="Enter Age" required/>
            <div class="underline"></div>
        </div>
        <div class="input-box underline">
            <input type="number" id="adhaarnumber" placeholder="Enter the passenger Adhaar Nummber" required/>
            <div class="underline"></div>
        </div>

        <div class="input-box button">
          <input type="submit" name="" value="Book"/>
        </div>
        </form>
        </div>
    </div>
  )
}

export default Booking