import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css';

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false);

  const toggleMenu = () => {
    setIsOpen(!isOpen);
  };

  return (
    <nav className="navbar">
      <div className="navbar-brand">
        <Link to="/">TodoApp</Link>
      </div>
      <div className="menu-toggle" onClick={toggleMenu}>
        <div className={isOpen ? "hamburger open" : "hamburger"}></div>
      </div>
      <ul className={isOpen ? "navbar-nav open" : "navbar-nav"}>
        <li>
          <Link to="/" onClick={toggleMenu}>Home</Link>
        </li>
        <li>
          <Link to="/features" onClick={toggleMenu}>Features</Link>
        </li>
        <li>
          <Link to="/how-it-works" onClick={toggleMenu}>How It Works</Link>
        </li>
        <li>
          <Link to="/dashboard" onClick={toggleMenu}>Dashboard</Link>
        </li>
        <li>
          <Link to="/about" onClick={toggleMenu}>About</Link>
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;
