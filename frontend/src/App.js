import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import About from './pages/About';
import Features from './pages/Features'; // New import
import HowItWorks from './pages/HowItWorks'; // New import
import Dashboard from './pages/Dashboard'; // New import (replaces Todo)
import Footer from './components/Footer'; // Import Footer component
import BackToTopButton from './components/BackToTopButton'; // Import BackToTopButton component
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <main>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/features" element={<Features />} /> {/* New Route */}
            <Route path="/how-it-works" element={<HowItWorks />} /> {/* New Route */}
            <Route path="/dashboard" element={<Dashboard />} /> {/* New Route (replaces Todo) */}
            <Route path="/about" element={<About />} />
          </Routes>
        </main>
        <Footer /> {/* Add Footer component here */}
        <BackToTopButton /> {/* Add BackToTopButton here */}
      </div>
    </Router>
  );
}

export default App;
