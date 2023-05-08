import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Login from "./pages/Login";
import Home from "./pages/Home";
import Signup from "./pages/Signup";
import Booking from "./pages/Booking";
import NoPage from "./pages/Nopage";
import Addflight from "./pages/Addflight";
import Admin from "./pages/Admin";
import Adminlogin from "./pages/Adminlogin";
import Adminsignup from "./pages/Adminsignup"
export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* <Route path="/" element={<Home />}> */}
          <Route path="/signup" element={<Signup />} />
          <Route path="/login" element={<Login />} />
          <Route path="/booking" element={<Booking />} />
          <Route path="*" element={<NoPage />} />
          <Route path="/home" element={<Home />} />
          <Route path="/admin" element={<Admin />} />
          <Route path="/admin/addflight" element={<Addflight />} />
          <Route path="/admin/login" element={<Adminlogin />} />
          <Route path="/admin/signup" element={<Adminsignup />} />
        {/* </Route> */}
      </Routes>
    </BrowserRouter>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);