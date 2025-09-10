import { Routes, Route } from 'react-router-dom';
import { UserProvider } from './Contexts/UserContexts';
import { UiProvider } from './Contexts/UiContext';
import { NavBar } from './Components/NavBar';
import { Register } from './Pages/Register';
import { Login } from './Pages/Login';
import { Home } from './Pages/Home';
import { About } from './Pages/About';
import { Vacations } from './Pages/Vacations';
import { AddVacation } from './Pages/AddVacation';
import { EditVacation } from './Pages/EditVacation';
import { Profile } from './Pages/Profile';
import { AdminPanel } from './Pages/AdminPanel';

function App() {
  return (
    <UiProvider>
      <UserProvider>
        <NavBar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/register" element={<Register />} />
          <Route path="/login" element={<Login />} />
          <Route path="/about" element={<About />} />
          <Route path="/vacations" element={<Vacations />} />
          <Route path="/vacations/add" element={<AddVacation />} />
          <Route path="/vacations/edit/:id" element={<EditVacation />} />
          <Route path="/profile" element={<Profile />} />
          <Route path="/admin" element={<AdminPanel />} />
        </Routes>
      </UserProvider>
    </UiProvider>
  );
}

export default App;
