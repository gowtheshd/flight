import React from 'react'
import "./Addflight.css"
const Addflight = () => {
  return (
    <div>
        <div class="container">
        <form action="#">
        <div class="title">Ticket Booking</div>
        <div class="input-box underline">
            <input type="text" id="flightno" placeholder="Enter Flight Number" required/>
            <div class="underline"></div>
          </div>
        <div class="input-box underline">
            <input type="text" id="fromto" placeholder="From" required/>
            <div class="underline"></div>
        </div>
        <div class="input-box underline">
            <input type="text" id="to" placeholder="To" required/>
            <div class="underline"></div>
        </div>
        <div class="input-box underline">
            <input type="date" id="date" placeholder="Date" required/>
            <div class="underline"></div>
        </div>
        <div class="input-box underline">
            <input type="number" id="charge" placeholder="Ticket charges" required/>
            <div class="underline"></div>
        </div>

        <div class="input-box button">
          <input type="submit" name="" value="Add Flight"/>
        </div>
        </form>
        </div>
    </div>
  )
}

export default Addflight